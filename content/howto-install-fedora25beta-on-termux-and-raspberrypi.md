Title: 在 Termux 与 Raspberry Pi 上安装 Fedora 25 Beta
Date: 2016-10-27 14:43:00
Author: lovenemesis
Category: tutorials
Tags: fedora, termux, raspberrypi
Slug: howto-install-fedora25beta-on-termux-and-raspberrypi

除了[一如既往的更新](https://linuxtoy.org/archives/fedora-25-beta.html)以外，Fedora 25 在还带来了平台支持上的一个里程碑：首次正式支持 aarch64 和 Raspberry Pi。

<!-- PELICAN_END_SUMMARY -->

### Raspberry Pi 定制版

得宜于 Raspberry Pi 合并入 Linux Kernel 4.7 内核主线，Fedora 对于 Raspbery Pi 的官方主持逐渐成为可能。不过毕竟 Raspberry Pi 有不少独特的地方，所以在内核之外还是有许多用户态的工具需要调整，最终这些变化在 Fedora 25 Beta 首次与公众见面。

经过一段时间的使用，Fedora 25 Beta 当下在 Raspberry Pi 下的状态为：

* 基于 Kernel 4.8 的 32 位 ARM 内核，适用于 Raspberry Pi 2/3
* 全部使用开源组件和允许自由分发的固件，VC4 GPU 通过 Mesa 实现 3D 加速，但是没有媒体硬件解码
* 提供 Worksatation, Server, Cloud 等多个不同版本
* 常见操作与 X86 的无异，更新无忧，无需特别屏蔽某个软件包
* 默认启用 SELinux
* 由于固件分发协议问题，暂不支持 Raspberry Pi 3 的内置 Wifi 和蓝牙模块，不过支持包括 USB 无线网卡在内的各类 USB 设备
* HAT 等传感器由于需要固件模块及其自由分发协议，也是暂不支持的

个人在测试中使用 Server 版本，首次启动后按照终端提示可以完成初步配置，尚不清楚这些步骤是否可在不连接 HDMI 显示的情况下完成，不过系统默认开启 SSH 服务的，应该可以。此外由于是 Server 版本，它启用 Cockpit 服务，可以方便的在浏览器中完成系统管理操作。

当做无头服务器使用初步体验良好，软件包方面比 Raspbian 要新很多。根据邮件列表的反馈来看，其 XFCE 版本的桌面非 3D 应用体验尚可。这下 Raspberry Pi 用户又多了一个选择。

[镜像下载与项目 Wiki](https://fedoraproject.org/wiki/Raspberry_Pi)

*消息来源*：[Fedora Magzine](https://fedoramagazine.org/raspberry-pi-support-fedora-25-beta/)

### 利用 Termux 在非 Root Android 系统上运行 Fedora

如果您还没有听过 [Termux](https://linuxtoy.org/archives/termux-032.html)的话，它是一款适用于 Android 系统的 Linux 终端模拟器和精简 Linux 环境，具有高度的可定制性。令（hou）人（zhi）惊（hou）喜（jue）的是，它打包了 `proot` 工具，可以 chroot 至其他 Linux 系统。

再说回 Fedora。其实早有[博文](https://nmilosev.svbtle.com/fedora-on-nonrooted-android-phones-2016-update)给出使用 GNURoot 以移花接木的方式在非 Root Android 手机上运行 Fedora 的方式。在下以此为参考，的确运行起了当时的 Fedora 23，但是由于设备是 aarch64 架构的，dnf 拒绝运行，呃……之后发觉了提供 aarch64 的 Termux，于是接下来的以它为主，不过其软件包有限，且不支持图形环境，所以总有那么一些不便。

最近该博主，现在亦是 Fedora 项目大使，再次[发文](https://nmilosev.svbtle.com/termuxfedora-install-fedora-on-your-phone-with-termux)，运用 Termux 打包的 `proot` 成功运行起来 Fedora。在下经过小幅改进，成功的在 Xperia Z4 Tablet 上运行起了 Fedora 25 Beta aarch64 版本。

说了这么多，其实操作起来很简单：
1. 在 Android 手机或平板上安装好 Termux
2. 前往 Github 下载[脚本](https://github.com/nmilosev/termux-fedora/raw/master/termux-fedora.sh) 放到 Termux 主目录，内含执行帮助，支持 armhfp 和 aarch64 版本
3. 取决于网速，耐心等待完成
4. 敲入 `startfedora` 开始使用

有了 Fedora 的一大好处就是可以弥补 Termux 没有图形环境的不足，于是可以安装你偏好的桌面环境（推荐使用无需 3D 加速的）即可，然后配合使用 [XServer XSDL](https://play.google.com/store/apps/details?id=x.org.server)即可。对于 Xperia Z4 Tablet 来说，合适的比例为 1280x800, 字体倍率0.7。过大或过小的倍率会导致 LXDE 的一些应用看不到菜单。

经测试，尽管在安装过程中有一两个软件包异常，不过 **LXDE 及 LibreOffice** 基本可用。遗憾的是另一款在下常用的软件 R 则由于 `gcc` 安装失败，尽管成功了但是基本无法实际使用。中文输入法尚未搞定，原因不明…

对于朝内用户来说，aarch64 作为次级架构，国内并没有镜像同步，于是 dnf 速度较慢，需要科学解决。此外毕竟是次级架构，有些软件包可能存在安装异常的问题（比如常见的 `unzip` 和 `gcc`）。不过若是你的 Android 手机使用了 ARMv8 指令集的较新 SoC 的话，这只能是一个必须忍受的痛苦，ARMv7 的用户则不受此条困扰。

另外在下修改过的安装脚本已经被原作者收录，现在支持 Fedora 24 和 Fedora 25 Beta 两个版本的 armv7l 和 aarch64 架构。

[博客原文](https://nmilosev.svbtle.com/termuxfedora-install-fedora-on-your-phone-with-termux)
