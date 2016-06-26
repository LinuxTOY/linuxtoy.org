Title: Debian 即将支持 ZFS 文件系统
Author: lovenemesis
Date: 2016-05-16 16:35:00
Category: News
Tags: zfs, debian
Slug: zfs-to-be-included-in-debian

经过一年多的工作，Debian 即将完成对于 ZFS 文件系统支持，以一个正确且合法的方式。

<!-- PELICAN_END_SUMMARY --> 

上周末[Petter Reinholdtsen](http://people.skolelinux.org/pere/blog/Debian_now_with_ZFS_on_Linux_included.html)宣布了 Debian 对于 ZFS 文件系统的支持已经基本就绪，其相关的软件包将被包含在 `contrib` 仓库中，其内核模块**以且仅以源代码形式**存在，由 `dkms` 在用户安装后自行编译。

这种方式与常见的显卡闭源驱动类似，得到了 Software Freedom Law Center 的法律认可，并没有违背相关的 GPL 或者 CDDL 协议。**注意**这与 Ubuntu 对于 ZFS 的支持完全不同，后者采取二进制形式分发预编译 ZFS 内核模块，[明显违反了 Linux 内核所用 GPLv2 协议](https://www.fsf.org/licensing/zfs-and-linux)。

[消息来源](https://bits.debian.org/2016/05/what-does-it-mean-that-zfs-is-in-debian.html?utm_source=twitterfeed&utm_medium=twitter&utm_campaign=bits.debian.org)
