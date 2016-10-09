Title: Pine64 评测
Date: 2016-10-09 17:17:00
Author: lovenemesis
Category: Embedded
Tags: pine64
Slug: pine64-review

笔者半年前分享了这块[廉价 64 位 ARM SBC PINE64 的初体验](https://linuxtoy.org/archives/pine64-preview.html)。两周前笔者的一块 RPi2 不幸寿终正寝，于是抱着试一试的心态再次看了下这块板子，没想到随着这半年的发展，这块廉价的板子的硬件软件生态环境有了可喜的进步。

<!-- PELICAN_END_SUMMARY --> 

### 购买渠道

相比官方商城的令人无语的“美金价格人民币服务”体验，终于有了一些 [PINE64 的国内分销商出没于某宝](https://shop122470551.taobao.com/category-1205316626.htm?search=y&catName=Pine+A64)，价格上还算亲民，至少能体现出相对于 RPi3 的价格优势。

笔者再次与以上渠道购买了一块 [PINE64+ 2G 版本](https://item.taobao.com/item.htm?id=529150082445)并配备了价格合理的 [ABS 外壳](https://item.taobao.com/item.htm?id=536287898438)，换掉了先前的 DIY 纸盒。

### Android 软件支持

[官方的 Android 5.1.1 v1.2.6 版本](http://wiki.pine64.org/index.php/Pine_A64_Software_Release#Android_5.1.1_Image_.28HDMI_Video_Output.29_Release_20160711)已经相当稳定了，常用的软件都可以正常运行，值得一提的特性有：

* 包含了 exfat 和 ext4 文件系统支持，只是受限于 Android 5.1 的系统，除了文件管理器以外的应用软件不能直接写入 OTG USB 存储设备
* HDMI 版本具备输出分辨率调整和丽画图像增强模式
* 支持 USB UVC 摄像头及 PINE64 专用的 5M 摄像头
* 可以安装 [Termux](https://linuxtoy.org/archives/termux-032.html) 将其变成小型下载及网络服务器，64 位软件包，支持 SSH 远程登录
* Android 版本 Kodi 运行良好
* 镜像下载提供了 BT、HTTP 和 BaiduYun 方式
* 缺陷是 DD 镜像的分区格式有问题，用户可用空间小且难以用诸如 `gparted` 之类的工具扩展

另外其社区的 Android 开发更是大胆激进，已经有 [Android 7.0 Beta 版本](https://github.com/ayufan-pine64/android-7.0/releases)了：

* 提供标准及 Android TV 两个版本
* 有限的 DRM 支持，可进行 YouTube 1080P 回放，但不可以用 Netflix
* 支持LCD触摸屏、红外控制、摄像头等都一并支持
* **HDMI CEC 支持**，不完美，不过可用
* Android 版本 Kodi 运行良好，通过 HDMI CEC 可以使用电视遥控器操作
* 简单分区格式，用户可用空间会在第一次启动时自动扩展

不过在实际使用过程中会遇到某些涉及网络操作的应用卡死的情况，尚未确定是应用本身对于 Android 7.0 的兼容问题还是 PINE64 的有线网络驱动问题。

### Linux 软件支持

还记得上一次提到的那些问题呢？一个个说：

#### Mali 3D 加速

根据[论坛的进展](http://forum.pine64.org/showthread.php?tid=587)来看，已经有社区成员借助 Mali 的二进制固件成功启用了 3D 加速，意味着在 Linux 环境下将会有效的 OpenGL ES 和 Framebuffer 加速了，不过这一实现似乎受制于全志一方的固件分发方式，有一些法律上面的问题需要解决，所以短时间内无法将成功集成到任何公开发布的系统镜像中。

由于涉及法律，所以完全无法预计这个问题什么时候能得到解决……不过好在只是 Mali 部分有这个问题，2D 加速及视频硬解码并不受影响

#### 主线内核支持

得益于 Linux 主线在 ARM64 架构上支持融合，现在已经有支持 **PINE64 的 Linux 4.7 内核**可以测试使用了。不过该版本内核缺失一些依赖二进制固件才能实现的功能，比如 HDMI 和 DSI 图形输出等，而且在网卡驱动上也需要改善（性能仅能发挥5成，MAC 地址不固定），所以现实中若想桌面 Linux 应用的话，还需要依赖有二进制固件的 3.10.105 内核。

#### Linux 发行版支持

不得不说官方在 Linux 发行版支持上做的不够好，主要还是依靠社区的力量。在官方 Wiki 上提供的 Linux 发行版下载要不是太老，要不是不符合使用场景，举例说比如其不包含 GUI 环境的 Debian Base 镜像竟然要求要有显示设备连接才能开机……

经过翻越论坛，笔者尝试了 [armbian](http://www.armbian.com/pine64/)，感觉是个非常适用无头服务器场景的 Debian Jessie 镜像，其特点有：

* 提供 3.10.105 的经典内核及 4.7 纯净内核两个版本，各自提供 Debian Jessie 和 Ubuntu Xenial 两个版本
* 与 Debian 和 Ubuntu 仓库兼容，可以配置使用国内镜像
* 自动扩展 SD 可用空间，默认开启 SSH 服务
* **64 位用户态应用环境**，比 RPi3 好很多。不过在享用 64 位带来的好处之外，在安装仓库之外的软件也需要多留心下，比如在[配置 resilio-sync 的时候](http://forum.odroid.com/viewtopic.php?f=135&t=18806#p132607)。
* 预置各种终端脚本方便远程监控

与笔者手上的使用 OSMC 的 RPi2 对比，搭载 armbian 的 PINE64 在执行相近任务时速度明显快很多，而且**发热要少很多**，若是和 RPi3 比较的话可能更明显。

此外还有人推荐 [DietPi](http://dietpi.com/)近期也增加了 PINE64 支持，感兴趣可以尝试。

#### 总结

经过半年多的发展，PINE64 的生态圈得到长足进展，无论是作用媒体娱乐的 Android 系统还是用作服务器的 Linux 系统都有不少亮点，其国内分销渠道的改善，使得其成为 RPi3 之外一个不错的 ARM64 SBC 选择。

