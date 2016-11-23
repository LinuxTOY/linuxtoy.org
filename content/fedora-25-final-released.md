Title: Fedora 25 正式发布
Date: 2016-11-23 21:20:00
Author: lovenemesis
Category: distro
Tags: fedora
Slug: fedora-25-final-released

经过意料之中的数次延期，Fedora 25 正式发布，带来了包含默认 Wayland 环境和容器化应用程序分发 Flatpak 在内的诸多开源领域新进展。 

<!-- PELICAN_END_SUMMARY -->

本次发布主要的变化有：

* 引入 Fedora Atomic 替代过去的 Fedora Cloud，提供基于 OSTree 原子性的系统滚动升级，方便在遇到升级问题时快速回滚至先前版本
* 使用 Fedora Media Writer 作为主要的下载媒体获取方式。Fedora Media Writer 是一款使用 PyQt5 构建的跨平台 Fedora LiveUSB 创建工具，通过向导式的操作实现下载、校验及创建 USB 的一系列操作，且支持包括 Spin 在内的多种 Fedora 发布方式。
* Unicode 更新至 9.0 版本
* 对于 Workstation 版本默认使用 Wayland 显示服务协议，不过依然提供 X11 的经典方案。
* Ibus 现在可以通过 `CTRL + SHIFT + E` 的方式输入表情符号
* 更新 Ruby on Rails 5.0, Go 1.7, glibc 2.24，Rust 1.12， Erlang 19，GHC 7.10。

参考[过往 Beta 版本的报道](https://linuxtoy.org/archives/fedora-25-beta.html)获取更多详情。

除此之外，您还可以在[ Raspberry Pi 2/3 或者 Android 手机/平板/机顶盒上安装并使用 Fedora 25](https://linuxtoy.org/archives/howto-install-fedora25beta-on-termux-and-raspberrypi.html)

[官方发布摘要](https://docs.fedoraproject.org/en-US/Fedora/25/html-single/Release_Notes/index.html)