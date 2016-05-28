Title: Pacman Hooks 简介
Date: 2016-05-28 18:16:28
Authors: Felix Yan
Category: Tips
Tags: pacman, archlinux
Slug: a-brief-introduction-to-pacman-hooks
Via: Felix Yan|https://blog.felixc.at/2016/05/a-brief-introduction-to-pacman-hooks/

Pacman 5.0 带来了 Hooks 支持，但在大规模应用前，我们留出了一个多月的时间来让用户先升级到 Pacman 5.0（因为同时升级 pacman 和有定义 hooks 的包会导致无法正常执行这些 hooks）。现在距离 Hooks 正式投入使用已经过去了一个月，我觉得是时候介绍一下 Hooks 和如何使用它了。

<!-- PELICAN_END_SUMMARY -->

先来看一个简单的 Hook:

```
[Trigger]
Type = File
Operation = Install
Operation = Upgrade
Target = usr/lib/tmpfiles.d/*.conf
 
[Action]
Description = Creating temporary files...
When = PostTransaction
Exec = /bin/sh -c 'while read -r f; do /usr/bin/systemd-tmpfiles --create "/$f"; done'
NeedsTargets
```

这个 Hook 的作用是：当检测到安装或更新的包文件中存在 `usr/lib/tmpfiles.d/*.conf` 时，在更新后对每个文件调用 `systemd-tmpfiles --create` 方法。前面的检测部分定义在 `[Trigger]` 部分，后面执行的操作定义在 `[Action]` 部分。下面我们分别了解一下这两部分。

**一、[Trigger] 部分**

首先需要了解的是可以用于触发的条件类别（Type）。上面的例子里使用了文件（File），即当操作中的包中存在对应文件时触发。另一个可选的 Type 是软件包名（Package），即直接匹配操作中的包名。

接下来，操作（Operation）选项限制了对软件包的操作类别。可以选择的操作有安装（Install）、更新（Upgrade）和删除（Remove）。一个 Hook 需要在多种操作执行时，如例子中那样写成多行即可。常用的组合有三种全部写上（更新缓存、数据库等）、写 Install+Upgrade（执行安装时的一次性操作）及与之对应的 Upgrade+Remove（卸载时的一次性操作）。

最后，我们需要定义具体的目标（Target）。如果目标是文件，这里需要写其相对根目录的完整路径，但需要去掉开头的 / 字符。通配符（\*、?）可以使用，具体匹配时会使用 fnmatch 方法。同样的，在一个 Hook 中可以定义多个目标，类似例子中的 Operation 那样写成多行即可。

**二、[Action] 部分**

先看看 Hooks 的执行时机：

![pacman hooks]({filename}/images/pacman-hooks.png)

可以看到，有两类明显不同的 Hooks: Pre-transaction Hooks 和 Post-transaction Hooks。

Pre-transaction Hook 在具体操作发生前执行，此时待升级的软件包还未被升级，待删除的软件包还未被删除，还可以让它们来绽放最后的光芒。因此，这种 Hook 通常和上面 [Trigger] 部分的 Upgrade、Remove 操作搭配使用。如 gconf 包的 gconf-remove Hook，会在 gconf schema 被删除前调用 `gconfpkg --uninstall` 命令来卸载对应的 schema。

Post-transaction Hook 则与它相反，是在操作完成后执行。如上面的 tmpfiles Hook。

这两种不同的类型被定义在 When 选项中，分别写作 `PreTransaction` 和 `PostTransaction`。

Description 选项仅包含一个供人类阅读的描述信息。目前的通用做法是用动词进 行时作为开头，英文省略号作为结束。显示在终端中会成为这样的效果：

    (1/1) Creating temporary files...

Exec 选项定义了具体执行的命令。和上面 Target 选项不同，这里不但需要写出待执行命令的完整路径，还需要保留最前方的 / 字符。如果在命令中需要用到前面 Trigger 得到的具体结果（如上面例子），你还需要在 [Action] 部分写一行 NeedsTargets 来让被匹配到的目标成为 Exec 选项的 stdin 输入，一行一个。值得注意的是如果匹配到的目标是文件，我们在对它进行操作前也需要补上最前方的 / 字符，如上面例子中使用的 `"/$f"`。

此外，[Action] 部分还有一些其他选项：

+ Depends 选项：定义 Hook 运行时需要的依赖。如果触发时对应依赖关系不满足，Hook 会拒绝运行。可以定义多次。
+ AbortOnFail 选项：当 Hook 执行失败时终止整个操作。这个仅对 Pre-transaction Hook 有效，毕竟 Post-transaction 发生在操作之后，定义这个选项没有意义。这个选项和 NeedsTargets 选项一样不需要任何参数。

**总结**

姗姗来迟的 Hooks 功能替代了许多原本在 .install 文件中定义的操作，大幅减少了在每个包中重复写这些操作的困扰，也节省了大量重复执行操作浪费的时间。目前有很多常见操作已经采用了 Hooks，但还有很多仍然在完善中。如果你在用的 AUR 包还没有采用这些 Hooks，请不要犹豫，赶快改改拍在维护者脸上吧！

关于哪些通用操作已经采用了 Hooks，可以参考[这个 Wiki 页面][w]。此外，如果想找更多 Hooks 的例子来研究，可以打开本地的 `/usr/share/libalpm/hooks/` 目录，你已经安装的 Hooks 都在这里。

参考资料：上文中的 Wiki 页面，以及 [pacman 源码][p]。

[w]: https://wiki.archlinux.org/index.php/DeveloperWiki:Pacman_Hooks
[p]: https://git.archlinux.org/pacman.git/tree/lib/libalpm/hook.c
