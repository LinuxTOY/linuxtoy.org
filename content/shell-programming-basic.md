Title: Shell 编程之语法基础
Date: 2016-05-16 21:47:45
Authors: Zorro
Category: Featured
Tags: bash, shell, programming
Slug: shell-programming-basic
Via: zorro|http://liwei.life/2016/05/16/69/

本系列文章由 Zorro 倾情撰写，征得作者同意，现刊登于此以飨读者。Zorro 为我前同事，跟他共事使我受益匪浅。谢啦，Zorro！-- *toy*

<!-- PELICAN_END_SUMMARY -->

+ [前言](#id1)
+ [if 分支结构](#id2)
+ [“当”、“直到”循环结构](#id3)
+ [case 分支结构和 for 循环结构](#id4)
    + [case 分支结构](#id5)
    + [for 循环结构](#id6)
+ [select 和第二种 for 循环](#id7)
+ [continue 和 break](#id8)
+ [最后](#id9)

### 前言 {#id1}

在此需要特别注明一下，本文叫做 shell 编程其实并不准确，更准确的说法是 bash 编程。考虑到 bash 的流行程度，姑且将 bash 编程硬说成 shell 编程也应没什么不可，但是请大家一定要清楚， shell 编程绝不仅仅只是 bash 编程。

通过本文可以帮你解决以下问题：

1. if 后面的中括号 `[]` 是语法必须的么？
2. 为什么 bash 编程中有时 `[]` 里面要加空格，有时不用加？如 `if [ -e /etc/passwd ]` 或 `ls [abc].sh`。
3. 为什么有人写的脚本这样写： `if [ x$test = x"string" ]`？
4. 如何用 `*` 号作为通配符对目录树递归匹配？
5. 为什么在 `for` 循环中引用 `ls` 命令的输出是可能有问题的？就是说： `for i in $(ls /)` 这样用有问题？

除了以上知识点以外，本文还试图帮助大家用一个全新的角度对 bash 编程的知识进行体系化。介绍 shell 编程传统的做法一般是要先说明什么是 shell ？什么是 bash ？这是种脚本语言，那么什么是脚本语言？不过这些内容真的太无聊了，我们快速掠过，此处省略 3 万字……作为一个实践性非常强的内容，我们直接开始讲语法。所以，这并不是一个入门内容，我们的要求是在看本文之前，大家至少要学会 Linux 的基本操作，并知道 bash 的一些基础知识。

### if 分支结构 {#id2}

组成一个语言的必要两种语法结构之一就是分支结构，另一种是循环结构。作为一个编程语言， bash 也给我们提供了分支结构，其中最常用的就是 `if`。用来进行程序的分支逻辑判断。其原型声明为：

```bash
if list; then list; elif list; then list; ... else list; fi
```

bash 在解析字符的时候，对待“`;`”跟看见回车是一样的行为，所以这个语法也可以写成：

```bash
if list
then
	list
elif list
then
	list
...
else
	list
fi
```

对于这个语法结构，需要重点说明的是 **`list`**。对于绝大多数其他语言， `if` 关键字后面一般跟的是一个表达式，比如 C 语言或类似语言的语法， `if` 后面都是跟一个括号将表达式括起来，如： `if (a > 0)`。这种认识会对学习 bash 编程造成一些误会，很多初学者都认为 bash 编程的 `if` 语法结构是： `if [ ];then...`，但实际上这里的中括号 `[]` 并不是 C 语言中小括号 `()` 语法结构的类似的关键字。这里的中括号其实就是个 shell 命令，是 `test` 命令的另一种写法。严谨的叙述， `if` 后面跟的就应该是个 `list` 。那么什么是 bash 中的 `list` 呢？根据 bash 的定义， `list` 就是若干个使用管道，`;`，`&`，`&&`，`||` 这些符号串联起来的 shell 命令序列，结尾可以 `;`，`&` 或换行结束。这个定义可能比较复杂，如果暂时不能理解，大家直接可以认为，**`if` 后面跟的就是个 shell 命令**。换个角度说， bash 编程仍然贯彻了 C 程序的设计哲学，即：*一切皆表达式*。

一切皆表达式这个设计原则，确定了 shell 在执行任何东西（注意是任何东西，不仅是命令）的时候都会有一个返回值，因为根据表达式的定义，任何表达式都必须有一个值。在 bash 编程中，这个返回值也限定了取值范围： `0-255` 。跟 C 语言含义相反， bash 中 `0` 为真（ true ），非 `0` 为假（ false ）。这就意味着，任何给 bash 之行的东西，都会返回一个值，在 bash 中，我们可以使用关键字 `$?` 来查看上一个执行命令的返回值：

```bash
[zorro@zorrozou-pc0 ~]$ ls /tmp/
plugtmp  systemd-private-bfcfdcf97a4142e58da7d823b7015a1f-colord.service-312yQe  systemd-private-bfcfdcf97a4142e58da7d823b7015a1f-systemd-timesyncd.service-zWuWs0  tracker-extract-files.1000
[zorro@zorrozou-pc0 ~]$ echo $?
0
[zorro@zorrozou-pc0 ~]$ ls /123
ls: cannot access '/123': No such file or directory
[zorro@zorrozou-pc0 ~]$ echo $?
2
```

可以看到， `ls /tmp` 命令执行的返回值为 `0` ，即为真，说明命令执行成功，而 `ls /123` 时文件不存在，返回值为 `2` ，命令执行失败。我们再来看个更极端的例子：

```bash
[zorro@zorrozou-pc0 ~]$ abcdef
bash: abcdef: command not found
[zorro@zorrozou-pc0 ~]$ echo $?
127
```

我们让 bash 执行一个根本不存在的命令 `abcdef` 。返回值为 `127` ，依然为假，命令执行失败。复杂一点：

```bash
[zorro@zorrozou-pc0 ~]$ ls /123|wc -l
ls: cannot access '/123': No such file or directory
0
[zorro@zorrozou-pc0 ~]$ echo $?
0
```

这是一个 `list` 的执行，其实就是两个命令简单的用管道串起来。我们发现，这时 shell 会将整个 `list` 看作一个执行体，所以整个 `list` 就是一个表达式，那么最后只返回一个值 `0` ，这个值是整个 `list` 中最后一个命令的返回值，第一个命令执行失败并不影响后面的 `wc` 统计行数，所以逻辑上这个 `list` 执行成功，返回值为真。

理解清楚这一层意思，我们才能真正理解 bash 的语法结构中 `if` 后面到底可以判断什么？事实是，判断什么都可以，因为 bash 无非就是把 `if` 后面的无论什么当成命令去执行，并判断其返回值是真还是假？如果是真则进入一个分支，为假则进入另一个。基于这个认识，我们可以来思考以下这个程序两种写法的区别：

```bash
#!/bin/bash

DIR="/etc"
＃第一种写法
ls -l $DIR &> /dev/null
ret=$?

if [ $ret -eq 0 ]
then
		echo "$DIR is exist!" 
else
    	echo "$DIR is not exist!"
fi

#第二种写法
if ls -l $DIR &> /dev/null
then
        echo "$DIR is exist!" 
else
        echo "$DIR is not exist!"
fi
```

我曾经在无数的脚本中看到这里的第一种写法，先执行某个命令，然后记录其返回值，再使用 `[]` 进行分支判断。我想，这样写的人应该都是没有真正理解 `if` 语法的语义，导致做出了很多脱了裤子再放屁的事情。当然，**`if` 语法中后面最常用的命令就是 `[]`**。请注意我的描述中就是说 `[]` 是一个命令，而不是别的。实际上这也是 bash 编程新手容易犯错的地方之一，尤其是有其他编程经验的人，在一开始接触 bash 编程的时候都是将 `[]` 当成 `if` 语句的语法结构，于是经常在写 `[]` 的时候里面不写空格，即：

```bash
#正确的写法
if [ $ret -eq 0 ]
＃错读的写法
if [$ret -eq 0]
```

同样的，当我们理解清楚了 `[]` 本质上是一个 shell 命令的时候，大家就知道这个错误是为什么了：命令加参数要用空格分隔。我们可以用 `type` 命令去检查一个命令：

```bash
[zorro@zorrozou-pc0 bash]$ type [
[ is a shell builtin
```

所以，实际上 `[]` 是一个内建命令，等同于 `test` 命令。所以上面的 `if` 语句也可以写成：

```bash
if test $ret -eq 0
```

这样看，形式上就跟第二种写法类似了。至于 `if` 分支怎么使用的其它例子就不再这废话了。重要的再强调一遍：**`if` 后面是一个命令(严格来说是 `list`)**，并且记住一个原则：**一切皆表达式**。

### “当”、“直到”循环结构 {#id3}

一般角度的讲解都会在讲完 `if` 分支结构之后讲其它分支结构，但是从执行特性和快速上手的角度来看，我认为先把跟 `if` 特性类似的 `while` 和 `until` 交代清楚更加合理。从字面上可以理解， `while` 就是“当”型循环，指的是当条件成立时执行循环。而 `until` 是直到型循环，其实跟 `while` 并没有实质上的区别，只是条件取非，逻辑变成循环到条件成立，或者说条件不成立时执行循环体。他们的语法结构是：

```bash
while list-1; do list-2; done
until list-1; do list-2; done
```

同样，分号可以理解为回车，于是常见写法是：

```bash
while list-1
do
	list-2
done

until list-1
do
	list-2
done
```

还是跟 `if` 语句一样，我们应该明白对于 `while` 和 `until` 的条件的含义，仍然是 `list` 。其判断条件是 `list` ，其执行结构也是 `list`。理解了上面 `if` 的讲解，我想这里应该不用复述了。我们用 `while` 和 `unitl` 来产生一个 `0-99` 的数字序列： 

`while` 版：

```bash
#!/bin/bash

count=0

while [ $count -le 100 ]
do
	echo $count
	count=$[$count+1]
done
```

`until` 版：

```bash
#!/bin/bash

count=0

until ! [ $count -le 100 ]
do
	echo $count
	count=$[$count+1]
done
```

我们通过这两个程序可以再次对比一下 `while` 和 `until` 到底有什么不一样？其实它们从形式上完全一样。这里另外说明两个知识点：

1. 在 bash 中，叹号（`!`）代表对命令(表达式)的返回值取反。就是说如果一个命令或 `list` 或其它什么东西如果返回值为真，加了叹号之后就是假，如果是假，加了叹号就是真。

2. 在 bash 中，使用 `$[]` 可以得到一个算数运算的值。可以支持常用的 `5` 则运算（`+-/%`）。用法就是 `$[3+7]` 类似这样，而且要注意，**这里的 `$[]` 里面没有空格分隔，因为它并不是个 shell 命令，而是特殊字符**。

常见运算例子：

```bash
[zorro@zorrozou-pc0 bash]$ echo $[213+456]
669
[zorro@zorrozou-pc0 bash]$ echo $[213+456+789]
1458
[zorro@zorrozou-pc0 bash]$ echo $[213*456]
97128
[zorro@zorrozou-pc0 bash]$ echo $[213/456]
0
[zorro@zorrozou-pc0 bash]$ echo $[9/3]
3
[zorro@zorrozou-pc0 bash]$ echo $[9/2]
4
[zorro@zorrozou-pc0 bash]$ echo $[9%2]
1
[zorro@zorrozou-pc0 bash]$ echo $[144%7]
4
[zorro@zorrozou-pc0 bash]$ echo $[7-10]
-3
```

注意这个运算只支持整数，并且对于小数只取其整数部分（没有四舍五入，小数全舍）。这个计算方法是 bash 提供的基础计算方法，如果想要实现更高级的计算可以使用 `let` 命令。如果想要实现浮点数运算，我一般使用 `awk` 来处理。

上面的例子中仍然使用 `[]` 命令（ `test` ）来作为检查条件，我们再试一个别的。假设我们想写一个脚本检查一台服务器是否能 `ping` 通？如果能 `ping` 通，则每隔一秒再看一次，如果发现 `ping` 不通了，就报警。如果什么时候恢复了，就再报告恢复。就是说这个脚本会一直检查服务器状态， `ping` 失败则触发报警， `ping` 恢复则通告恢复。脚本内容如下：

```bash
#!/bin/bash

IPADDR='10.0.0.1'
INTERVAL=1

while true
do
	while ping -c 1 $IPADDR &> /dev/null
	do
		sleep $INTERVAL
	done

	echo "$IPADDR ping error! " 1>&2

	until ping -c 1 $IPADDR &> /dev/null
	do
		sleep $INTERVAL
	done

	echo "$IPADDR ping ok!"
done
```

这里关于输出重定向的知识我就先不讲解了，后续会有别的文章专门针对这个主题做出说明。以上就是 `if` 分支结构和 `while` 、 `until` 循环结构。掌握了这两种结构之后，我们就可以写出几乎所有功能的 bash 脚本程序了。这两种语法结构的共同特点是，使用 `list` 作为“判断条件”，这种“风味”的语法特点是“一切皆表达式”。 bash 为了使用方便，还给我们提供了另外一些“风味”的语法。下面我们继续看：

### case 分支结构和 for 循环结构 {#id4}

#### case 分支结构 {#id5}

我们之所以把 `case` 分支和 `for` 循环放在一起讨论，主要是因为它们所判断的不再是“表达式”是否为真，而是去匹配字符串。我们还是通过其语法和例子来理解一下。 `case` 分支的语法结构：

```bash
case word in [ [(] pattern [ | pattern ] ... ) list ;; ] ... esac
```

与 `if` 语句是以 `fi` 标记结束思路相仿， `case` 语句是以 `esac` 标记结束。其常见的换行版本是：

```bash
case $1 in
        pattern)
        list
        ;;
        pattern)
        list
        ;;
        pattern)
        list
        ;;
esac
```

举几个几个简单的例子，并且它们实际上是一样的：

例 1:

```bash
#!/bin/bash

case $1 in
	(zorro)
	echo "hello zorro!"
	;;
	(jerry)
	echo "hello jerry!"
	;;
	(*)
	echo "get out!"
	;;
esac
```

例 2:

```bash
#!/bin/bash

case $1 in
	zorro)
	echo "hello zorro!"
	;;
	jerry)
	echo "hello jerry!"
	;;
	*)
	echo "get out!"
	;;
esac
```

例 3:

```bash
#!/bin/bash

case $1 in
	zorro|jerry)
	echo "hello $1!"
	;;
	*)
	echo "get out!"
	;;
esac
```

这些程序的执行结果都是一样的：

```bash
[zorro@zorrozou-pc0 bash]$ ./case.sh zorro
hello zorro!
[zorro@zorrozou-pc0 bash]$ ./case.sh jerry
hello jerry!
[zorro@zorrozou-pc0 bash]$ ./case.sh xxxxxx
get out!
```

这些程序应该不难理解，无非就是几个语法的不一样之处，大家自己可以看到哪些可以省略，哪些不能省略。这里需要介绍一下的有两个概念：

1. `$1` 在脚本中表示传递给脚本命令的第一个参数。关于这个变量以及其相关系列变量的使用，我们会在后续其它文章中介绍。
2. `pattern` 就是 bash 中“通配符”的概念。常用的 bash 通配符包括星号(`*`)、问号(`?`)和其它一些字符。相信如果对 bash 有一定了解的话，对这些符号并不陌生，我们在此简单说明一下。

最常见的通配符有三个：

`?` 表示任意一个字符。这个没什么可说的。

`*` 表示任意长度任意字符，包括空字符。在 bash 4.0 以上版本中，如果 bash 环境开启了 `globstar` 设置，那么两个连续的 `**` 可以用来递归匹配某目录下所有的文件名。我们通过一个实验测试一下：

一个目录的结构如下：

```bash
[zorro@zorrozou-pc0 bash]$ tree test/
test/
├── 1
├── 2
├── 3
├── 4
├── a
│   ├── 1
│   ├── 2
│   ├── 3
│   └── 4
├── a.conf
├── b
│   ├── 1
│   ├── 2
│   ├── 3
│   └── 4
├── b.conf
├── c
│   ├── 5
│   ├── 6
│   ├── 7
│   └── 8
└── d
    ├── 1.conf
    └── 2.conf

4 directories, 20 files
```

使用通配符进行文件名匹配：

```bash
[zorro@zorrozou-pc0 bash]$ echo test/*
test/1 test/2 test/3 test/4 test/a test/a.conf test/b test/b.conf test/c test/d
[zorro@zorrozou-pc0 bash]$ echo test/*.conf
test/a.conf test/b.conf
```

这个结果大家应该都熟悉。我们再来看看下面：

查看当前 `globstar` 状态：

```bash
[zorro@zorrozou-pc0 bash]$ shopt globstar
globstar       	off
```

打开 `globstar`：

```bash
[zorro@zorrozou-pc0 bash]$ shopt -s globstar
[zorro@zorrozou-pc0 bash]$ shopt globstar
globstar       	on
```

使用 `**` 匹配：

```bash
[zorro@zorrozou-pc0 bash]$ echo test/**
test/ test/1 test/2 test/3 test/4 test/a test/a/1 test/a/2 test/a/3 test/a/4 test/a.conf test/b test/b/1 test/b/2 test/b/3 test/b/4 test/b.conf test/c test/c/5 test/c/6 test/c/7 test/c/8 test/d test/d/1.conf test/d/2.conf
[zorro@zorrozou-pc0 bash]$ echo test/**/*.conf
test/a.conf test/b.conf test/d/1.conf test/d/2.conf
```

关闭 `globstart` 并再次测试 `**`：

```bash
[zorro@zorrozou-pc0 bash]$ shopt -u globstar
[zorro@zorrozou-pc0 bash]$ shopt  globstar
globstar       	off

[zorro@zorrozou-pc0 bash]$ echo test/**/*.conf
test/d/1.conf test/d/2.conf
[zorro@zorrozou-pc0 bash]$ 
[zorro@zorrozou-pc0 bash]$ echo test/**
test/1 test/2 test/3 test/4 test/a test/a.conf test/b test/b.conf test/c test/d
```

`[...]` 表示这个范围中的任意一个字符。比如 `[abcd]`，表示 `a` 或 `b` 或 `c` 或 `d` 。当然这也可以写成 `[a-d]`。`[a-z]` 表示任意一个小写字母。还是刚才的 `test` 目录，我们再来试试：

```bash
[zorro@zorrozou-pc0 bash]$ ls test/[123]
test/1  test/2  test/3
[zorro@zorrozou-pc0 bash]$ ls test/[abc]
test/a:
1  2  3  4

test/b:
1  2  3  4

test/c:
5  6  7  8
```

以上就是简单的三个通配符的说明。当然，关于通配符以及 `shopt` 命令还有很多相关知识。我们还是会在后续的文章中单独把相关知识点拿出来讲，再这里大家先理解这几个。另外需要强调一点，**千万不要把 bash 的通配符和正则表达式搞混了，它们完全没有关系！**

简要理解了 `pattern` 的概念之后，我们就可以更加灵活的使用 `case` 了，它不仅仅可以匹配一个固定的字符串，还可以利用 `pattern` 做到一定程度的模糊匹配。但是无论怎样， `case` 都是去比较字符串是否一样，这跟使用 `if` 语句有本质的不同， `if` 是判断表达式。当然，我们在 `if` 中使用 `test` 命令同样可以做到 `case` 的效果，区别仅仅是程序代码多少的区别。还是举个例子说明一下，我们想写一个身份验证程序，大家都知道，一个身份验证程序要判断用户名及其密码是否都匹配某一个字符串，如果两个都匹配，就通过验证，如果有一个不匹配就不能通过验证。分别用 `if` 和 `case` 来实现这两个验证程序内容如下：

`if` 版：

```bash
#!/bin/bash

if [ $1 = "zorro" ] && [ $2 = "zorro" ]
then
	echo "ok"
elif [ $1$2 = "jerryjerry" ]
then
	echo "ok"
else
	echo "auth failed!"
fi
```

`case` 版：

```bash
#!/bin/bash

case $1$2 in
	zorrozorro|jerryjerry)
	echo "ok!"
	;;
	*)
	echo "auth failed!"
	;;
esac
```

两个程序一对比，直观看起来 `case` 版的要少些代码，表达力也更强一些。但是，这两个程序都有 bug ，如果 `case` 版程序给的两个参数是 `zorro zorro` 可以报 `ok` 。如果是 `zorroz orro` 是不是也可以报 `ok` ？如果只给一个参数 `zorrozorro` ，另一个参数为空，是不是也可以报 `ok` ？同样， `if` 版的 `jerry` 判断也有类似问题。当你的程序要跟用户或其它程序交互的时候，一定要谨慎仔细的检查输入，一般写程序很大工作量都在做各种异常检查上，尤其是需要跟人交互的时候。我们看似用一个合并字符串变量的技巧，将两个判断给合并成了一个，但是这个技巧却使程序编写出了错误。对于这个现象，我的意见是，**如果不是必要，请不要在编程中玩什么“技巧”，重剑无锋，大巧不工。**当然，这个 bug 可以通过如下方式解决：

`if` 版：

```bash
#!/bin/bash

if [ $1 = "zorro" ] && [ $2 = "zorro" ]
then
	echo "ok"
elif [ $1:$2 = "jerry:jerry" ]
then
	echo "ok"
else
	echo "auth failed!"
fi
```

`case` 版：

```bash
#!/bin/bash

case $1x$2 in
	zorro:zorro|jerry:jerry)
	echo "ok!"
	;;
	*)
	echo "auth failed!"
	;;
esac
```

我加的是个 `:` 字符，当然，也可以加其他字符，原则是这个字符不要再输入中能出现。我们在其他人写的程序里也经常能看到类似这样的判断处理：

```bash
if [ x$1 = x"zorro" ] && [ x$2 = x"zorro" ]
```

相信你也能明白为什么要这么处理了。仅对某一个判断来说这似乎没什么必要，但是如果你养成了这样的习惯，那么就能让你避免很多可能出问题的环节。这就是编程经验和编程习惯的重要性。当然，很多人只有“经验”，却也不知道这个经验是怎么来的，那也并不可取。

#### for 循环结构 {#id6}

bash 提供了两种 `for` 循环，一种是类似 C 语言的 `for` 循环，另一种是让某变量在一系列字符串中做循环。在此，我们先说后者。其语法结构是：

```bash
for name [ [ in [ word ... ] ] ; ] do list ; done
```

其中 `name` 一般是一个变量名，后面的 `word ...` 是我们要让这个变量分别赋值的字符串列表。这个循环将分别将 `name` 变量每次赋值一个 `word` ，并执行循环体，直到所有 `word` 被遍历之后退出循环。这是一个非常有用的循环结构，其使用频率可能远高于 `while` 、 `until` 循环。我们来看看例子：

```bash
[zorro@zorrozou-pc0 bash]$ for i in 1 2 3 4 5;do echo $i;done
1
2
3
4
5
```

再看另外一个例子：

```bash
[zorro@zorrozou-pc0 bash]$ for i in aaa bbb ccc ddd eee;do echo $i;done
aaa
bbb
ccc
ddd
eee
```

再看一个：

```bash
[zorro@zorrozou-pc0 bash]$ for i in /etc/* ;do echo $i;done
/etc/adjtime
/etc/adobe
/etc/appstream.conf
/etc/arch-release
/etc/asound.conf
/etc/avahi
......
```

这种例子举不胜举，可以用 `for` 遍历的东西真的很多，大家可以自己发挥想象力。这里要提醒大家注意的是当你学会了 \`\` 或 `$()` 这个符号之后， `for` 的范围就更大了。于是很多人喜欢这样搞：

```bash
[zorro@zorrozou-pc0 bash]$ for i in `ls`;do echo $i;done
auth_case.sh
auth_if.sh
case.sh
if_1.sh
ping.sh
test
until.sh
while.sh
```

乍看起来这好像跟使用 `*` 没啥区别：

```bash
[zorro@zorrozou-pc0 bash]$ for i in *;do echo $i;done
auth_case.sh
auth_if.sh
case.sh
if_1.sh
ping.sh
test
until.sh
while.sh
```

但可惜的是并不总是这样，请对比如下两个测试：

```bash
[zorro@zorrozou-pc0 bash]$ for i in `ls /etc`;do echo $i;done
adjtime
adobe
appstream.conf
arch-release
asound.conf
avahi
bash.bash_logout
bash.bashrc
bind.keys
binfmt.d
......


[zorro@zorrozou-pc0 bash]$ for i in /etc/*;do echo $i;done
/etc/adjtime
/etc/adobe
/etc/appstream.conf
/etc/arch-release
/etc/asound.conf
/etc/avahi
/etc/bash.bash_logout
/etc/bash.bashrc
/etc/bind.keys
/etc/binfmt.d
......
```

看到差别了么？

其实这里还会隐含很多其它问题，像 `ls` 这样的命令很多时候是设计给人用的，它的很多显示是有特殊设定的，可能并不是纯文本。比如可能包含一些格式化字符，也可能包含可以让终端显示出颜色的标记字符等等。当我们在程序里面使用类似这样的命令的时候要格外小心，说不定什么时候在什么不同环境配置的系统上，你的程序就会有意想不到的异常出现，到时候排查起来非常麻烦。所以这里我们应该尽量避免使用 `ls` 这样的命令来做类似的行为，用通配符可能更好。当然，如果你要操作的是多层目录文件的话，那么 `ls` 就更不能帮你的忙了，它遇到目录之后显示成这样：

```bash
[zorro@zorrozou-pc0 bash]$ ls /etc/*
/etc/adobe:
mms.cfg

/etc/avahi:
avahi-autoipd.action  avahi-daemon.conf  avahi-dnsconfd.action  hosts  services

/etc/binfmt.d:

/etc/bluetooth:
main.conf

/etc/ca-certificates:
extracted  trust-source
```

所以遍历一个目录还是要用刚才说到的 `**`，如果不是 bash 4.0 之后的版本的话，可以使用 `find` 。我推荐用 `find` ，因为它更通用。有时候你会发现，使用 `find` 之后，绝大多数原来需要写脚本解决的问题可能都用不着了，一个 `find` 命令解决很多问题。

### select 和第二种 for 循环 {#id7}

我之所以把这两种语法放到一起讲，主要是这两种语法结构在 bash 编程中使用的几率可能较小。这里的第二种 `for` 循环是相对于上面讲的第一种 `for` 循环来说的。实际上这种 `for` 循环就是 C 语言中 `for` 循环的翻版，其语义基本一致，区别是括号 `()` 变成了双括号 `(())`，循环标记开始和结束也是 bash 风味的 `do` 和 `done` ，其语法结构为：

```bash
for (( expr1 ; expr2 ; expr3 )) ; do list ; done
```

看一个产生 `0-99` 数字的循环例子：

```bash
#!/bin/bash

for ((count=0;count<100;count++))
do
	echo $count
done
```

我们可以理解为， bash 为了对数学运算作为条件的循环方便我们使用，专门扩展了一个 `for` 循环来给我们使用。跟 C 语言一样，这个循环本质上也只是一个 `while` 循环，只是把变量初始化，变量比较和循环体中的变量操作给放到了同一个 `(())` 语句中。这里不再废话。

最后是 `select` 循环，实际上 `select` 提供给了我们一个构建交互式菜单程序的方式，如果没有 `select` 的话，我们在 shell 中写交互的菜单程序是比较麻烦的。它的语法结构是：

```bash
select name [ in word ] ; do list ; done
```

还是来看看例子：

```bash
#!/bin/bash

select i in a b c d
do
	echo $i
done
```

这个程序执行的效果是：

```bash
[zorro@zorrozou-pc0 bash]$ ./select.sh 
1) a
2) b
3) c
4) d
#? 
```

你会发现 `select` 给你构造了一个交互菜单，索引为 1 ， 2 ， 3 ， 4 。对应的名字就是程序中的 a ， b ， c ， d 。之后我们就可以在后面输入相应的数字索引，选择要 `echo` 的内容：

```bash
[zorro@zorrozou-pc0 bash]$ ./select.sh 
1) a
2) b
3) c
4) d
#? 1
a
#? 2
b
#? 3
c
#? 4
d
#? 6

#? 
1) a
2) b
3) c
4) d
#? 
1) a
2) b
3) c
4) d
#? 
```

如果输入的不是菜单描述的范围就会 `echo` 一个空行，如果直接输入回车，就会再显示一遍菜单本身。当然我们会发现这样一个菜单程序似乎没有什么意义，实际程序中， `select` 大多数情况是跟 `case` 配合使用的。

```bash
#!/bin/bash

select i in a b c d
do
	case $i in
		a)
		echo "Your choice is a"
		;;
		b)
		echo "Your choice is b"
		;;
		c)
		echo "Your choice is c"
		;;
		d)
		echo "Your choice is d"
		;;
		*)
		echo "Wrong choice! exit!"
		exit
		;;
	esac
done
```

执行结果为：

```bash
[zorro@zorrozou-pc0 bash]$ ./select.sh 
1) a
2) b
3) c
4) d
#? 1
Your choice is a
#? 2
Your choice is b
#? 3
Your choice is c
#? 4
Your choice is d
#? 5
Wrong choice! exit!
```

这就是 `select` 的常见用法。

### continue 和 break {#id8}

对于 bash 的实现来说， `continue` 和 `break` 实际上并不是语法的关键字，而是被作为内建命令来实现的。不过我们从习惯上依然把它们看作是 bash 的语法。在 bash 中， `break` 和 `continue` 可以用来跳出和进行下一次 `for` ， `while` ， `until` 和 `select` 循环。

### 最后 {#id9}

我们在本文中介绍了 bash 编程的常用语法结构： `if` 、 `while` 、 `until` 、 `case` 、两种 `for` 和 `select` 。我们在详细分析它们语法的特点的过程中，也简单说明了使用时需要注意的问题。希望这些知识和经验对大家以后在 bash 编程上有帮助。

通过 bash 编程语法的入门，我们也能发现， bash 编程是一个上手容易，但是精通困难的编程语言。任何人想要写个简单的脚本，掌握几个语法结构和几个 shell 命令基本就可以干活了，但是想写出高质量的代码却没那么容易。通过语法的入门，我们可以管中窥豹的发现，讲述的过程中有无数个可以深入探讨的细节知识点，比如通配符、正则表达式、 bash 的特殊字符、 bash 的特殊属性和很多 shell 命令的使用。我们的后续文章会给大家分块整理这些知识点，如果你有兴趣，请持续关注。

> 版权声明：
> 
> 本文章内容在非商业使用前提下可无需授权任意转载、发布。
> 转载、发布请务必注明作者和其微博、微信公众号地址，以便读者询问问题和甄误反馈，共同进步。
> 微博 ID ： [orroz](http://weibo.com/orroz) 
> 微信公众号： Linux 系统技术 (扫描以下二维码关注)

![zorro]({filename}/images/zorro-wechat.jpg)
