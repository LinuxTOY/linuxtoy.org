Title: Shell 编程之执行过程
Date: 2016-05-23 17:16:30
Authors: Zorro
Category: Featured
Tags: shell, bash, programming
Slug: shell-programming-execute
Via: Zorro|http://liwei.life

本文是 shell 编程系列的第二篇，主要介绍 bash 脚本是如何执行命令的。

<!-- PELICAN_END_SUMMARY -->

**目录**

+ [前言](#id1)
+ [以魔法 `#!` 开始](#id2)
+ [bash 如何执行 shell 命令？](#id3)
    + [别名 alias](#id4)
    + [关键字：keyword](#id5)
    + [函数：function](#id6)
    + [内建命令：built in](#id7)
    + [哈希索引：hash](#id8)
    + [外部命令：command](#id9)
+ [脚本的退出](#id10)
+ [最后](#id11)
	
### 前言 {#id1}

本文是 shell 编程系列的第二篇，主要介绍 bash 脚本是如何执行命令的。通过本文，您应该可以解决以下问题：

1. 脚本开始的 `#!` 到底是怎么起作用的？
2. bash 执行过程中的字符串判断顺序究竟是什么样？
3. 如果我们定义了一个函数叫 `ls`，那么调用 `ls` 的时候，到底 bash 是执行 `ls` 函数还是 `ls` 命令？
4. 内建命令和外建命令到底有什么差别？
5. 程序退出的时候要注意什么？

### 以魔法 `#!` 开始 {#id2}

一个脚本程序的开始方式都比较统一，它们几乎都开始于一个 `#!` 符号。这个符号的作用大家似乎也都知道，叫做声明解释器。脚本语言跟编译型语言的不一样之处主要是脚本语言需要解释器。因为脚本语言主要是文本，而系统中能够执行的文件实际上都是可执行的二进制文件，就是编译好的文件。文本的好处是人看方便，但是操作系统并不能直接执行，所以就需要将文本内容传递给一个可执行的二进制文件进行解析，再由这个可执行的二进制文件根据脚本的内容所确定的行为进行执行。可以做这种解析执行的二进制可执行程序都可以叫做解释器。

脚本开头的 `#!` 就是用来声明本文件的文本内容是交给哪个解释器进行解释的。比如我们写 bash 脚本，一般声明的方法是 `#!/bin/bash` 或 `#!/bin/sh`。如果写的是一个 Python 脚本，就用 `#!/usr/bin/python`。当然，在不同环境的系统中，这个解释器放的路径可能不一样，所以固定写一个路径的方式就可能造成脚本在不同环境的系统中不通用的情况，于是就出现了这样的写法：

	 #!/usr/bin/env 脚本解释器名称

这就利用了 `env` 命令可以得到可执行程序执行路径的功能，让脚本自行找到在当前系统上到底解释器在什么路径。让脚本更具通用性。但是大家有没有想过一个问题，大多数脚本语言都是将 `#`后面出现的字符当作是注释，在脚本中并不起作用。这个 `#!` 和这个注释的规则不冲突么？

这就要从 `#!` 符号起作用的原因说起，其实也很简单，这个功能是由操作系统的程序载入器做的。在 Linux 操作系统上，除了 1 号进程以外，我们可以认为其它所有进程都是由父进程 `fork` 出来的。所以对 bash 来说，所谓的载入一个脚本执行，无非就是父进程调用 `fork()`、`exec()` 来产生一个子进程。这 `#!` 就是在内核处理 `exec` 的时候进行解析的。

> 内核中整个调用过程如下（Linux 4.4），内核处理 `exec` 族函数的主要实现在 `fs/exec.c` 文件的 `do_execveat_common()` 方法中，其中调用 `exec_binprm()` 方法处理执行逻辑，这函数中使用 `search_binary_handler()` 对要加载的文件进行各种格式的判断，脚本（script）只是其中的一种。确定是 script 格式后，就会调用 script 格式对应的 `load_binary` 方法：`load_script()` 进行处理， `#!` 就是在这个函数中解析的。解析到了 `#!` 以后，内核会取其后面的可执行程序路径，再传递给 `search_binary_handler()` 重新解析。这样最终找到真正的可执行二进制文件进行相关执行操作。

因此，**对脚本第一行的 `#!` 解析，其实是内核给我们变的魔术**。`#!` 后面的路径内容在起作用的时候还没有交给脚本解释器。很多人认为 `#!` 这一行是脚本解释器去解析的，然而并不是。了解了原理之后，也顺便明白了为什么 `#!` 一定要写在第一行的前两个字符，因为这是在内核里写死的，它就只检查前两个字符。当内核帮你选好了脚本解释器之后，后续的工作就都交给解释器做了。脚本的所有内容也都会原封不动的交给解释器再次解释，是的，包括 `#!`。但是由于对于解释器来说，`#` 开头的字符串都是注释，并不生效，所以解释器自然对 `#!` 后面所有的内容无感，继续解释对于它来说有意义的字符串去了。

我们可以用一个自显示脚本来观察一下这个事情，什么是自显示脚本？无非就是 `#!/bin/cat`，这样文本的所有内容包括 `#!` 行都会交给 `cat` 进行显示：

	[zorro@zorrozou-pc0  bash ]$ cat cat.sh 
	#!/bin/cat

	echo "hello world!"
	[zorro@zorrozou-pc0  bash ]$ ./cat.sh 
	#!/bin/cat

	echo "hello world!"

或者自删除脚本：

	[zorro@zorrozou-pc0  bash ]$ cat rm.sh 
	#!/bin/rm

	echo "hello world!"
	[zorro@zorrozou-pc0  bash ]$ chmod +x rm.sh 
	[zorro@zorrozou-pc0  bash ]$ ./rm.sh 
	[zorro@zorrozou-pc0  bash ]$ cat rm.sh
	cat: rm.sh: No such file or directory

这就是 `#!` 的本质。

### bash 如何执行 shell 命令？ {#id3}

刚才我们从 `#!` 的作用原理讲解了一个 bash 脚本是如何被加载的。就是说当 `#!/bin/bash` 的时候，实际上内核给我们启动了一个 bash 进程，然后把脚本内容都传递给 bash 进行解析执行。实际上，无论在脚本里还是在命令行中，bash 对文本的解析方法大致都是一样的。首先，bash 会以一些特殊字符作为分隔符，将文本进行分段解析。最主要的分隔符无疑就是回车，类似功能的分隔符还有分号"`;`"。所以在 bash 脚本中是以回车或者分号作为一行命令结束的标志的。这基本上就是第一层级的解析，主要目的是将大段的命令行进行分段。

之后是第二层级解析，这一层级主要是区分所要执行的命令。这一层级主要解析的字符是管道"`|`"，`&&`、`||`这样的可以起到连接命令作用的特殊字符。这一层级解析完后，bash 就能拿到最基本的一个个的要执行的命令了。

当然拿到命令之后还要继续第三层解析，这一层主要是区分出要执行的命令和其参数，主要解析的是空格和 tab 字符。这一层次解析完之后，bash 才开始对最基本的字符串进行解释工作。当然，绝大多数解析完的字符串，bash 都是在 `fork` 之后将其传递给 `exec` 进行执行，然后 `wait` 其执行完毕之后再解析下一行。这就是 bash 脚本也被叫做批处理脚本的原因，主要执行过程是一个一个指令串行执行的，上一个执行完才执行下一个。以上这个过程并不能涵盖 bash 解释字符串的全过程，实际情况要比这复杂。

bash 在解释命令的时候为了方便一些操作和提高某些效率做了不少特性，包括 `alias` 功能和外部命令路径的 `hash` 功能。bash 还因为某些功能不能做成外部命令，所以必须实现一些内建命令，比如 `cd`、`pwd` 等命令。当然除了内建命令以外，bash 还要实现一些关键字，比如其编程语法结构的 `if` 或是 `while` 这样的功能。实际上作为一种编程语言，bash 还要实现函数功能，我们可以理解为，bash 的函数就是将一堆命令做成一个命令，然后调用执行这个名字，bash 就是去执行事先封装好的那堆命令。

好吧，问题来了：我们已知有一个内建命令叫做 `cd`，如果此时我们又建立一个 `alias` 也叫 `cd`，那么当我在 bash 中敲入 `cd` 并回车之后，bash 究竟是将它当成内建命令解释还是当成 `alias` 解释？同样，如果 `cd` 又是一个外部命令能？如果又是一个 `hash` 索引呢？如果又是一个关键字或函数呢？

实际上 bash 在做这些功能的时候已经安排好了它们在名字冲突的情况下究竟该先以什么方式解释。优先顺序是：

1. 别名：alias
2. 关键字：keyword
3. 函数：function
4. 内建命令：built in
5. 哈希索引：hash
6. 外部命令：command

这些 bash 要判断的字符串类型都可以用 `type` 命令进行判断，如：

	[zorro@zorrozou-pc0  bash ]$ type egrep
	egrep is aliased to `egrep --color=auto'
	[zorro@zorrozou-pc0  bash ]$ type if
	if is a  shell  keyword
	[zorro@zorrozou-pc0  bash ]$ type pwd
	pwd is a  shell  builtin
	[zorro@zorrozou-pc0  bash ]$ type passwd
	passwd is /usr/bin/passwd

#### 别名 alias {#id4}

bash 提供了一种别名(alias)功能，可以将某一个字符串做成另一个字符串的别名，使用方法如下：

	[zorro@zorrozou-pc0  bash ]$ alias cat='cat -n'
	[zorro@zorrozou-pc0  bash ]$ cat /etc/passwd
	     1	root:x:0:0:root:/root:/bin/ bash 
	     2	bin:x:1:1:bin:/bin:/usr/bin/nologin
	     3	daemon:x:2:2:daemon:/:/usr/bin/nologin
	     4	mail:x:8:12:mail:/var/spool/mail:/usr/bin/nologin
	     ......

于是我们再使用 `cat` 命令的时候，bash 会将其解释为 `cat -n`。

这个功能在交互方式进行 bash 操作的时候可以提高不少效率。如果我们发现我们常用到某命令的某个参数的时候，就可以将其做成 `alias`，以后就可以方便使用了。交互 bash 中，我们可以用 `alias` 命令查看目前已经有的 `alias` 列表。可以用 `unalias` 取消这个别名设置：

	[zorro@zorrozou-pc0  bash ]$ alias 
	alias cat='cat -n'

	[zorro@zorrozou-pc0  bash ]$ unalias cat

`alias` 功能在交互打开的 bash 中是默认开启的，但是在 bash 脚本中是默认关闭的。

	#!/bin/ bash 
	
	#shopt -s expand_aliases
	
	alias ls='ls -l'
	ls /etc

此时本程序输出：

	[zorro@zorrozou-pc0  bash ]$ ./alias.sh 
	adjtime		  cgconfig.conf			docker	     group	    ifplugd	    libao.conf	    mail.rc	     netconfig	     passwd	  request-key.conf   shell s	       udisks2
	adobe		  cgrules.conf			drirc	...
	
使用注释行中的 `shopt -s expand_aliases` 命令可以打开 `alias` 功能支持，我们将这行注释取消掉之后的执行结果为：

	[zorro@zorrozou-pc0  bash ]$ ./alias.sh 
	total 1544
	-rw-r--r-- 1 root    root        44 11月 13 19:53 adjtime
	drwxr-xr-x 2 root    root      4096 4月  20 09:34 adobe
	-rw-r--r-- 1 root    root       389 4月  18 22:19 appstream.conf
	-rw-r--r-- 1 root    root         0 10月  1 2015 arch-release
	-rw-r--r-- 1 root    root       260 7月   1 2014 asound.conf
	drwxr-xr-x 3 root    root      4096 3月  11 10:09 avahi

这就是 bash 的 `alias` 功能。

#### 关键字：keyword {#id5}

关键字的概念很简单，主要就是 bash 提供的语法。比如 `if`，`while`，`function` 等等。对这些关键字使用 `type` 命令会显示：

    [zorro@zorrozou-pc0  bash ]$ type function
    function is a  shell  keyword

说明这是一个 keyword。我想这个概念没什么可以解释的了，无非就是 bash 提供的一种语法而已。只是要注意，bash 会在判断 `alias` 之后才来判断字符串是不是个 keyword。就是说，我们还是可以创建一个叫 `if` 的 `alias`，并且在执行的时候，bash 只把它当成 `alias` 看。

	[zorro@zorrozou-pc0  bash ]$ alias if='echo zorro'
	[zorro@zorrozou-pc0  bash ]$ if
	zorro
	[zorro@zorrozou-pc0  bash ]$ unalias if

#### 函数：function {#id6}

bash 在判断完字符串不是一个关键字之后，将会检查其是不是一个函数。在 bash 编程中，我们可以使用关键字 function 来定义一个函数，当然这个关键字其实也可以省略：

    name () compound-command [redirection]
    function name [()] compound-command [redirection]

语法结构中的 `compound-command` 一般是放在 `{}` 里的一个命令列表（list）。定义好的函数其实就是一系列 shell 命令的封装，并且它还具有很多 bash 程序的特征，比如在函数内部可以使用 `$1`，`$2` 等这样的变量来判断函数的参数，也可以对函数使用重定向功能。

关于函数的更细节讨论我们会在后续的文章中展开说明，在这里我们只需要知道它对于 bash 来说是第几个被解释的即可。

#### 内建命令：built in {#id7}

在判断完函数之后，bash 将查看给的字符串是不是一个内建命令。内建命令是相对于外建命令来说的。其实我们在 bash 中执行的命令最常见的是外建（外部）命令。比如常见的 `ls`，`find`，`passwd` 等。这些外建命令的特点是，它们是作为一个可执行程序放在 `$PATH` 变量所包含的目录中的。bash 在执行这些命令的时候，都会进行 `fork()`,`exec()`并且`wait()`。就是用标准的打开子进程的方式处理外部命令。但是内建命令不同，这些命令都是 bash 自身实现的命令，它们不依靠外部的可执行文件存在。只要有 `bash`，这些命令就可以执行。典型的内建命令有 `cd`、`pwd` 等。大家可以直接 `help cd` 或者任何一个内建命令来查看它们的帮助。大家还可以 `man bash` 来查看 bash 相关的帮助，当然也包括所有的内建命令。

其实内建命令的个数并不会很多，一共大概就这些：

	:,  ., [, alias, bg, bind, break, builtin, caller, cd, command, compgen, complete, compopt, continue, declare, dirs, disown, echo, enable, eval, exec, exit, export, false, fc,
       fg, getopts, hash, help, history, jobs, kill, let, local, logout, mapfile, popd, printf, pushd, pwd, read, readonly, return, set, shift, shopt, source, suspend,  test,  times,  trap,
       true, type, typeset, ulimit, umask, unalias, unset, wait

我们在后续的文章中会展开讲解这些命令的功能。

#### 哈希索引：hash {#id8}

hash 功能实际上是针对外部命令做的一个功能。刚才我们已经知道了，外部命令都是放在 `$PATH` 变量对应的路径中的可执行文件。bash 在执行一个外部命令时所需要做的操作是：如果发现这个命令是个外部命令就按照 `$PATH` 变量中按照目录路径的顺序，在每个目录中都遍历一遍，看看有没有对应的文件名。如果有，就 `fork`、`exec`、`wait`。我们系统上一般的 `$PATH` 内容如下：

	[zorro@zorrozou-pc0  bash ]$ echo $PATH
	/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/lib/jvm/default/bin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl:/home/zorro/.local/bin:/home/zorro/bin

当然，很多系统上的 `$PATH` 变量包含的路径可能更多，目录中的文件数量也可能会很多。于是，遍历这些目录去查询文件名的行为就可能比较耗时。于是 bash 提供了一种功能，就是建立一个 hash 表，在第一次找到一个命令的路径之后，对其命令名和对应的路径建立一个 hash 索引。这样下次再执行这个命令的时候，就不用去遍历所有的目录了，只要查询索引就可以更快的找到命令路径，以加快执行程序的速度。

我们可以使用内建命令 `hash` 来查看当前已经建立缓存关系的命令和其命中次数：

	[zorro@zorrozou-pc0  bash ]$ hash
	hits	command
	   1	/usr/bin/flock
	   4	/usr/bin/chmod
	  20	/usr/bin/vim
	   4	/usr/bin/cat
	   1	/usr/bin/cp
	   1	/usr/bin/mkdir
	  16	/usr/bin/man
	  27	/usr/bin/ls

这个命令也可以对当前的 `hash` 表进行操作，`-r` 参数用来清空当前 `hash` 表。手工创建一个 `hash`：

	[root@zorrozou-pc0  bash ]# hash -p /usr/sbin/passwd psw
	[root@zorrozou-pc0  bash ]# psw
	Enter new UNIX password: 
	Retype new UNIX password: 

此时我们就可以通过执行 `psw` 来执行 `passwd` 命令了。查看更详细的 `hash` 对应关系：

	[root@zorrozou-pc0  bash ]# hash -l
	builtin hash -p /usr/bin/netdata netdata
	builtin hash -p /usr/bin/df df
	builtin hash -p /usr/bin/chmod chmod
	builtin hash -p /usr/bin/vim vim
	builtin hash -p /usr/bin/ps ps
	builtin hash -p /usr/bin/man man
	builtin hash -p /usr/bin/pacman pacman
	builtin hash -p /usr/sbin/passwd psw
	builtin hash -p /usr/bin/ls ls
	builtin hash -p /usr/bin/ss ss
	builtin hash -p /usr/bin/ip ip

删除某一个 `hash` 对应：

	[root@zorrozou-pc0  bash ]# hash -d psw
	[root@zorrozou-pc0  bash ]# hash -l
	builtin hash -p /usr/bin/netdata netdata
	builtin hash -p /usr/bin/df df
	builtin hash -p /usr/bin/chmod chmod
	builtin hash -p /usr/bin/vim vim
	builtin hash -p /usr/bin/ps ps
	builtin hash -p /usr/bin/man man
	builtin hash -p /usr/bin/pacman pacman
	builtin hash -p /usr/bin/ls ls
	builtin hash -p /usr/bin/ss ss
	builtin hash -p /usr/bin/ip ip
	
显示某一个 `hash` 对应的路径：

	[root@zorrozou-pc0  bash ]# hash -t chmod
	/usr/bin/chmod

在交互式 bash 操作和 bash 编程中，hash 功能总是打开的，我们可以用 `set +h` 关闭 hash 功能。

	[zorro@zorrozou-pc0  bash ]$ cat hash.sh 
	#!/bin/ bash 

	#set +h

	hash

	hash -p /usr/bin/useradd uad

	hash -t uad

	uad

默认打开 hash 的脚本输出：

	[zorro@zorrozou-pc0  bash ]$ ./hash.sh 
	hash: hash table empty
	/usr/bin/useradd
	Usage: uad [options] LOGIN
	       uad -D
	       uad -D [options]

	Options:
	  -b, --base-dir BASE_DIR       base directory for the home directory of the
                                new account
	  -c, --comment COMMENT         GECOS field of the new account
	  -d, --home-dir HOME_DIR       home directory of the new account
	  -D, --defaults                print or change default useradd configuration
	  -e, --expiredate EXPIRE_DATE  expiration date of the new account
	  -f, --inactive INACTIVE       password inactivity period of the new account
	  -g, --gid GROUP               name or ID of the primary group of the new
                                account
	  -G, --groups GROUPS           list of supplementary groups of the new
                                account
	  -h, --help                    display this help message and exit
	  -k, --skel SKEL_DIR           use this alternative skeleton directory
	  -K, --key KEY=VALUE           override /etc/login.defs defaults
	  -l, --no-log-init             do not add the user to the lastlog and
                                faillog databases
	  -m, --create-home             create the user's home directory
	  -M, --no-create-home          do not create the user's home directory
	  -N, --no-user-group           do not create a group with the same name as
                                the user
	  -o, --non-unique              allow to create users with duplicate
                                (non-unique) UID
	  -p, --password PASSWORD       encrypted password of the new account
	  -r, --system                  create a system account
	  -R, --root CHROOT_DIR         directory to chroot into
	  -s, --shell SHELL             login shell of the new account
	  -u, --uid UID                 user ID of the new account
	  -U, --user-group              create a group with the same name as the user

关闭 hash 之后的输出：

	[zorro@zorrozou-pc0  bash ]$ ./hash.sh 
	./hash.sh: line 5: hash: hashing disabled
	./hash.sh: line 7: hash: hashing disabled
	./hash.sh: line 9: hash: hashing disabled
	./hash.sh: line 11: uad: command not found

#### 外部命令：command {#id9}

除了以上说明之外的命令都会当作外部命令处理。执行外部命令的固定动作就是在 `$PATH` 路径下找命令，找到之后 `fork`、`exec`、`wait`。如果没有这个可执行文件名，就报告命令不存在。这也是 bash 最后去判断的字符串类型。

外建命令都是通过 `fork` 调用打开子进程执行的，所以 bash 单纯只用外建命令是不能实现部分功能的。比如大家都知道 `cd` 命令是用来修改当前进程的工作目录的，如果这个功能使用外部命令实现，那么进程将 `fork` 打开一个子进程，子进程通过 `chdir()` 进行当前工作目录的修改时，实际上只改变了子进程本身的当前工作目录，而父进程 bash 的工作目录没变。之后子进程退出，返回到父进程的交互操作环境之后，用户会发现，当前的 bash 的 `pwd` 还在原来的目录下。所以大家应该可以理解，虽然我们的**原则是尽量将所有命令都外部实现**，但是还是有一些功能不能以创建子进程的方式达到目的，那么这些功能就必须内部实现。这就是内建命令必须存在的原因。另外要注意：**bash 在正常调用内部命令的时候并不会像外部命令一样产生一个子进程**。

### 脚本的退出 {#id10}

一个 bash 脚本的退出一般有多种方式，比如使用 `exit` 退出或者所有脚本命令执行完之后退出。无论怎么样退出，脚本都会有个返回码，而且返回码可能不同。

任何命令执行完之后都有返回码，主要用来判断这个命令是否执行成功。在交互 bash 中，我们可以使用 `$?` 来查看上一个命令的返回码：

	[zorro@zorrozou-pc0  bash ]$ ls /123
	ls: cannot access '/123': No such file or directory
	[zorro@zorrozou-pc0  bash ]$ echo $?
	2
	[zorro@zorrozou-pc0  bash ]$ ls /
	bin  boot  cgroup  data  dev  etc  home  lib  lib64  lost+found  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
	[zorro@zorrozou-pc0  bash ]$ echo $?
	0

返回码逻辑上有两类，0 为真，非零为假。就是说，返回为 0 表示命令执行成功，非零表示执行失败。返回码的取值范围为 0-255。其中错误返回码为 1-255。bash 为我们提供了一个内建命令 `exit`，通过这个命令可以人为指定退出的返回码是多少。这个命令的使用是一般进行 bash 编程的运维人员所不太注意的。我们在上一篇的 bash 编程语法结构的讲解中说过，`if`、`while` 语句的条件判断实际上就是判断命令的返回值，如果我们自己写的 bash 脚本不注意规范的使用脚本退出时的返回码的话，那么这样的 bash 脚本将可能不可以在别人编写脚本的时候，直接使用 `if` 将其作为条件判断，这可能会对程序的兼容性造成影响。因此，请大家注意自己写的 bash 程序的返回码状态。**如果我们的 bash 程序没有显示的以一个 exit 指定返回码退出的话，那么其最后执行命令的返回码将成为整个 bash 脚本退出的返回码。**

当然，一个 bash 程序的退出还可能因为被中间打断而发生，这一般是因为进程接收到了一个需要程序退出的信号。比如我们日常使用的 `Ctrl＋c` 操作，就是给进程发送了一个 2 号 `SIGINT` 信号。考虑到程序退出可能性的各种可能，系统将错误返回码设计成 1-255，这其中还分成两类：

1. 程序退出的返回码：1-127。这部分返回码一般用来作为给程序员自行设定错误退出用的返回码，比如：如果一个文件不存在，`ls` 将返回 2。如果要执行的命令不存在，则 bash 统一返回 127。返回码 125 和 126 有特殊用处，一个是程序命令不存在的返回码，另一个是命令的文件在，但是不可执行的返回码。
2. 程序被信号打断的返回码：128-255。这部分系统习惯上是用来表示进程被信号打断的退出返回码的。一个进程如果被信号打断了，其退出返回码一般是 128+信号编号的数字。

比如说，如果一个进程被 2 号信号打断的话，其返回码一般是 128+2=130。如：

	[zorro@zorrozou-pc0  bash ]$ sleep 1000
	^C
	[zorro@zorrozou-pc0  bash ]$ echo $?
	130

在执行 `sleep` 命令的过程中，我使用 `Ctrl+c` 中断了进程的执行。此时返回值为 130。可以用内建命令 `kill -l` 查看所有信号和其对应的编号：

	[zorro@zorrozou-pc0  bash ]$ kill -l
	 1) SIGHUP	 2) SIGINT	 3) SIGQUIT	 4) SIGILL	 5) SIGTRAP
	 6) SIGABRT	 7) SIGBUS	 8) SIGFPE	 9) SIGKILL	10) SIGUSR1
	11) SIGSEGV	12) SIGUSR2	13) SIGPIPE	14) SIGALRM	15) SIGTERM
	16) SIGSTKFLT	17) SIGCHLD	18) SIGCONT	19) SIGSTOP	20) SIGTSTP
	21) SIGTTIN	22) SIGTTOU	23) SIGURG	24) SIGXCPU	25) SIGXFSZ
	26) SIGVTALRM	27) SIGPROF	28) SIGWINCH	29) SIGIO	30) SIGPWR
	31) SIGSYS	34) SIGRTMIN	35) SIGRTMIN+1	36) SIGRTMIN+2	37) SIGRTMIN+3
	38) SIGRTMIN+4	39) SIGRTMIN+5	40) SIGRTMIN+6	41) SIGRTMIN+7	42) SIGRTMIN+8
	43) SIGRTMIN+9	44) SIGRTMIN+10	45) SIGRTMIN+11	46) SIGRTMIN+12	47) SIGRTMIN+13
	48) SIGRTMIN+14	49) SIGRTMIN+15	50) SIGRTMAX-14	51) SIGRTMAX-13	52) SIGRTMAX-12
	53) SIGRTMAX-11	54) SIGRTMAX-10	55) SIGRTMAX-9	56) SIGRTMAX-8	57) SIGRTMAX-7
	58) SIGRTMAX-6	59) SIGRTMAX-5	60) SIGRTMAX-4	61) SIGRTMAX-3	62) SIGRTMAX-2
	63) SIGRTMAX-1	64) SIGRTMAX	

在我们编写 bash 脚本的时候，一般可以指定的返回码范围是 1-124。建议大家养成编写返回码的编程习惯，但是系统并不对这做出限制，作为程序员你依然可以使用 0-255 的所有返回码。但是如果你滥用这些返回码，很可能会给未来程序的扩展造成不必要的麻烦。

### 最后 {#id11}

本文中我们描述了一个脚本的执行过程，从 `#!` 开始，到中间的解析过程，再到最后的退出返回码。希望这些对大家深入理解 bash 的执行过程和编写更高质量的脚本有帮助。通过本文我们明确了以下知识点：

1. 脚本开始的 `#!` 的作用原理。
2. bash 的字符串解析过程。
3. 什么是 alias。
4. 什么是关键字。
5. 什么是 function。
6. 什么是内建命令，hash 和外建命令以及它们的执行方法。
7. 如何退出一个 bash 脚本以及返回码的含义。

希望这些内容会对大家以后的 bash 编程有所帮助。如果有相关问题，可以在我的微博、微信或者博客上联系我。

> 版权声明：
> 
> 本文章内容在非商业使用前提下可无需授权任意转载、发布。
>
> 转载、发布请务必注明作者和其微博、微信公众号地址，以便读者询问问题和甄误反馈，共同进步。
>
> 微博 ID ： [orroz](http://weibo.com/orroz) 
>
> 微信公众号： Linux 系统技术 (扫描以下二维码关注)
>
> ![zorro]({filename}/images/zorro-wechat.jpg)
