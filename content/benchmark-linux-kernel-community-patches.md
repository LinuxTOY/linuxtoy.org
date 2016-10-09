Title: Linux 内核社区补丁对比
Date: 2016-10-09 15:02:00
Author: lovenemesis
Category: Review
Tags: kernel
Slug: benchmark-linux-kernel-community-patches

Linux 内核主线总体而言兼具了性能、稳定和安全于一身，不过总有些 Geek 不满足主线中的种种限制，使用各自社区的补丁为它添砖加瓦。

*感谢 [Houge_Langley](https://twitter.com/Houge_Langley) 来稿*

<!-- PELICAN_END_SUMMARY -->

### 概述

* pf内核，这算是一个非常为人熟知的内核。包含了ck补丁（兼容4.8版本将是最后一个版本），详见：[MuQSS - The Multiple Queue Skiplist Scheduler](https://ck-hack.blogspot.kr/2016/10/muqss-multiple-queue-skiplist-scheduler.html)；bfq补丁和graysky gcc 优化CPU补丁。该内核没有为 Debian 系打包。
* zen内核，这是一群 Geek 修改的内核，包括了 pf 内核在内的所有优化补丁，另外还加上 aufs 补丁。这个补丁的具体内容可以参见这里：[aufs wiki](https://en.wikipedia.org/wiki/Aufs)。
* grsecurity/pax内核，这个内核基本就是内核主线和 grsecurity/pax 补丁，因为其它补丁很难或者说极难打上。这个补丁主要目的在于安全强化，所以内核性能就放在第二位。更多内容可以参考：[官方主页](https://grsecurity.net/index.php)。


### 测试平台及社区内核

我自己使用的台式机，配置如下图：

![benchmark-linux-kernel-community-patches-testing-platform](/images/benchmark-linux-kernel-community-patches-testing-platform.png)

使用测试的四个内核，分别是pf内核4.8.0.pf2版本，zen内核4.7.6版本，两个grsecurity/pax（下文简称GP，GP内核在图中都是带有-grsec的版本）内核版本，其中之一使用主线内核和GP补丁，另一个使用主线、GP补丁和Graysky2补丁。详见下图：


![benchmark-linux-kernel-community-patches-testing-kernels](/images/benchmark-linux-kernel-community-patches-testing-kernels.png)

### 测试

#### C-Ray测试

![benchmark-linux-kernel-community-patches-cray](/images/benchmark-linux-kernel-community-patches-cray.png)

从 C-Ray 的测试中，可以发现 GP 内核表现基本一致。4.7.7是GP+Graysky2的版本，如果说这个是比GP原生有所提升，这个微小的差距人类是无法感觉到的。另外，zen内核和pf内核虽然大版本不同，但差距非常小。

#### Parallel BZIP2 Compression 测试

![benchmark-linux-kernel-community-patches-bzip2](/images/benchmark-linux-kernel-community-patches-bzip2.png)

这项测试的结果与上一个基本类似。

#### 7-Zip Compression 测试

![benchmark-linux-kernel-community-patches-7zip](/images/benchmark-linux-kernel-community-patches-7zip.png)

这项测试的结果也在预料之中。不过从以上三项测试，不难看出 GP 内核的性能确实较另外两个差些。

#### Loopback TCP Network Performance 测试

![benchmark-linux-kernel-community-patches-tcp](/images/benchmark-linux-kernel-community-patches-tcp.png)

这个测试中对比两个 GP 和其它两个内核，发现GP几乎完败。 

#### IOzone 测试

![benchmark-linux-kernel-community-patches-iozone](/images/benchmark-linux-kernel-community-patches-iozone.png)

这项测试中除了 zen 内核明显领先，其他都差不多。

#### SQLite 测试

![benchmark-linux-kernel-community-patches-sqlite](/images/benchmark-linux-kernel-community-patches-sqlite.png)

这项测试中 GP 内核有小幅领先，但差距不大。

#### Apache 测试

![benchmark-linux-kernel-community-patches-apache](/images/benchmark-linux-kernel-community-patches-apache.png)

关于GP+graysky2的版本为什么跑下来还不如不优化的GP，猜测原因有可能是我后来将 `kernel.grsecurity.harden_ipc` 设置为0有关，待到后面总结详谈。

#### PostgreSQL pgbench 测试

![benchmark-linux-kernel-community-patches-pgbench](/images/benchmark-linux-kernel-community-patches-pgbench.png)

这个测试中缺失GP原始版本的跑分，推测也和上一个测试中的异常得分有关。不过神奇的是在这个版本中，GP+graysky2的GP版本跑分超过了两个优化的内核。

### 总结

鱼和熊掌不可兼得，社区版本中，最注重安全的 Grsecurity/PaX 内核补丁的使用，提升的安全性却降低了性能，但是就降低的程度来说，除了TCP那个测试，其它降低的并不多，个人认为这个程度完全不影响正常使用。

就 Zen 内核，和 pf 内核而言，两者因为大版本号的不同，对比意义不大，不过总的来说，除了 Apache 那个测试，Zen 完胜 pf 之外，它们基本上都差不多，各有千秋。

一些其它需要注意的小插曲：

1. Zen 内核测试时，我将TCP无意间修改成 YeAH，而不是 pf 内核测试时的 Westwood，或许这个也是 TCP 测试中两个微小差距的原因！？
2. 关于 `kernel.grsecurity.harden_ipc` 问题。关于 Grsecurity/PaX 内核的编译，我基本上完全参考了 [《面向桌面的 PaX/Grsecurity 内核配置注释与评论》](http://hardenedlinux.org/system-security/2016/08/10/grsec-kernel-full-commentary.html) 一文，该文中提到关于 IPC 的问题，将该选项开启后，“让 PaX 禁止权限宽松到离谱的 IPC 被访问，以免 buggy 的 IPC 程序被攻击，但同时允许有 `CAP_IPC_OWNER` 权限的进程这么做。我从没见过这个特性导致问题，推荐编译时开启，运行时可以用 sysctl 关闭”。不过随着我开启该选项，大量 ipc 内容填充 dmesg 日志，目前我没有追踪到问题本质，随后的工作将更新到这里。

最后，我在 Ubuntu 论坛的编译打包板块为各位发烧友制作最新的 Zen 和 Grsecurity/PaX 内核，没有提供源，需要自行下载用 dpkg 安装，详见[这里](https://forum.ubuntu.org.cn/viewtopic.php?f=56&t=480634)。


