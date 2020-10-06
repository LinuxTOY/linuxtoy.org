Title: Pine64 轻量级便携电脑
Date: 2020-10-06 22:43
Category: Howto
Tags: android, armbian, pine64
Slug: lightweight-portable-desktop-with-pine64
Authors: lovenemesis

随着 Pine64 逐步得到主流内核的支持和 Linux ARM 生态圈的发展，这块廉价的 ARMv8 单片机的可玩性相比多了起来，官方也在基于此 SoC 推出了诸如 PineTab 和 PineBook 的衍生品。然而由于开源硬件天生的小众和 COVID-19 的影响，本来就吃紧的产能让这两款产品一货难求，笔者遍寻渠道仍然在待发货状态。定价 $120 的 [PineTab](https://www.pine64.org/pinetab/)硬件配置跟已经停产的 [$90 的 Amazon Fire 8 HD](https://www.amazon.com/dp/B07TMJ1R3X) 比较接近，主频甚至还要更低一些，与 [$49 的 Amazon Fire 7](https://www.amazon.com/dp/B07JQRDX52)差不多。笔者恰好都用过这两款基于 Android 的廉价平板，可用但绝对说不上流畅。在 2020 年推出这样一款配置的设备，是否能借着主线内核和 Linux ARM 更低资源要求的优势实现一定的可用性呢？且允许笔者借用手头的现有设备，组建一套类似的方案先行体验下。

<!-- PELICAN_END_SUMMARY -->

### 组件设备 ###

[PineTab](https://www.pine64.org/pinetab/)的硬件配置跟已经停产的 [$90 的 Amazon Fire 8 HD](https://www.amazon.com/dp/B07TMJ1R3X) 比较接近，主频甚至还要更低一些，与 [$49 的 Amazon Fire 7](https://www.amazon.com/dp/B07JQRDX52)差不多。笔者恰好都用过这两款基于 Android 的廉价平板，可用但绝对说不上流畅，于是在 2020 年这样一款配置的设备是否能借着主线内核和 Linux ARM 更低资源要求的优势实现一定的可用性，是这次软件体验的主要目的。基于这个目的，选择了以下设备：

* [Pine64+ 2GB SBC](https://store.pine64.org/product/pine-a64-board-2gb/)，第一批 Kickstarter 版本，与 PineTab 所用的 [Pine64 LTS](https://store.pine64.org/product/pine-a64-lts/) 仅是内存模块不同（DDR3 vs LPDDR3）；
* [Pine64 801/11BGN + BT4.0 模块](https://store.pine64.org/product/wifi-802-11bgn-bluetooth-4-0-module/)，与 PineTab 配置一致；
* [Pine64 ABS 外壳](https://store.pine64.org/product/pine64-abs-enclosure/)，某宝购得相近款，缺少散热开孔；
* [GoBigger ZB156UTF 便携式显示器](http://www.gobiggerclub.com/pd.jsp?id=20#_jcp=2)，配置高于 PineTab 所配 10 寸 720P 屏幕，但手头也就这一个便携式带触摸的屏幕了，实际中会调整桌面分辨率为 720P 保持一致；
* [HP CS750 双模键鼠套装](https://post.smzdm.com/p/a4wmk4lx/)，入门级产品中难得的剪刀脚结构，比罗技的同类产品中巧克力手感和便携性好多了；
* [Sony CP-SC10](https://www.sony.com.cn/products/rme/b2c/usb/cp-sc10.htm)，双头 Type-C 输出且支持 PD，带动便携式显示器必需，容量高于 PineTab 一些；
* 绿联低阻抗双头 Type-C 电源线和转接头；
* SanDisk Extreme 32G SD UHS-1 存储卡，容量和读写速度应该比 PineTab 所用的 eMMC 慢，可惜手头 Pine64+ 并不支持 eMMC 扩展。

### 软件体验 ###

尽管核心 SoC 一致，但目前 [PineTab 的软件还处于相当早期对于硬件的适配阶段](https://wiki.pine64.org/index.php?title=PineTab/Early-Adopter)，最终的形态应该与 Pine64 一致，于是选择搭载 Linux Kernel 5.8 的 [Armbian 20.08 Buster Desktop 版本](https://www.armbian.com/pine64/)是相当合适的。在经过软件仓库和中文字体技术输入法的简单配置之后，从下面几个角度看看它跟廉价 Android 版本相比如何。

* 硬件支持：得益于[主线内核](https://linux-sunxi.org/Linux_mainlining_effort)和 Debian 稳定版的支持，硬件的支持还算不错。网络扩展卡无需额外配置即可持续稳定的使用 WiFi，蓝牙则遗憾的不可用。HDMI 视频可以稳定输出 4K 分辨率，不过在 Xfce 桌面下应用还是降低分辨率至 720P 可用性更高一些。HDMI 音频亦仅需在 PulseAudio 面板小控件中切换下即可。最令人惊喜的是触摸屏直接可用，只是 Xfce 桌面并非针对触摸屏优化，诸如右键等手势缺失使得可用性提升有限。**略逊**
* 网页浏览：在 Xfce 的桌面下默认预装了 Chromium 浏览器且启用了 `--enable-low-end-device-mode` 模式，亦可从仓库下载 Firefox ESR 版本。Chromium 的启动速度稍快些，内存占用方面两者则不相上下，在仅开启浏览器默认内置主页的情况下，内存已然达到 800MB 左右，稍微复杂些的网站 4 个基本就逼近 2GB 内存的上限了，比廉价 Fire 平板上的 Silk 稍微好一些。但两款浏览器的桌面版本在扩展组件的支持上面比与其相对移动版要好上太多了，且桌面版的 User Agent 不会被朝内的视频网站被处处“穿小鞋”，也可算个优势吧…… **略优**
* 生产力工具：办公用途如果预装的 LibreOffice 办公套件不能满足，亦可下载安装[原生支持 ARMv8 的 WPS Office for Linux 版本](https://linux.wps.cn/)。编程工具从 Python、Go 到 R、Rust 一应俱全，甚至 [VS Code 亦从 1.50 Insider 版本开始原生支持 ARMv8 架构](https://code.visualstudio.com/insiders/)。这些比在 Android 平台下使用诸如 [Termux 的体验](https://linuxtoy.org/archives/howto-install-fedora25beta-on-termux-and-raspberrypi.html)还是要好上太多了。**大幅领先**
* 多媒体娱乐：Pine64 所用 A64 SoC 的 [Mali GPU](https://linux-sunxi.org/Mali)和[视频引擎](https://linux-sunxi.org/Video_Engine)在内核态的支持已经合并入 Linux 主线内核且包含在 Armbian 分发的 Kernel 5.8.X 中，但受限于 [Debian Buster 较老的用户态软件版本]((https://gitlab.freedesktop.org/lima/web/blob/master/README.md))，目前并没有 3D 加速（OpenGL ES）和硬件解码功能。于是在纯软件解码的情况下，A64 的四核 CPU 在播放本地和网络 720P 视频的时有些许丢帧，尚可接受，1080P 则完全不行。此外，所有基于 OpenGL ES 的应用也无法正确执行。值得提醒的是，目前网上依然能搜到关于 Mali 400 和 Pine64 在开启 3D 加速和硬件解码方面的教程，这些几乎都是基于早些非主线内核和 Mali 闭源驱动的，在当下已经不再适用了，无需费时折腾。基于目前的现状，**暂时落后** 于相近配置的廉价平板，不过明年待 Debian Bulleye 发布时，状态应该会有大幅度改观。
* 功耗：新版本内核已经具备良好的 PWM 支持，在室温 20 度的环境中搭配被动散热片空闲时温控报告 34 度，长时间高负载的 720P 视频播放则飙升至接近 58 度。相比低负载都要 54 度 Raspberry Pi 3+ 来说要好上太多。待机时间方面难以比较，毕竟作为耗电大户的屏幕相差太多。根据播放 720P 本地视频时电量指示下降的估计，这个充电宝能支持大约 5 小时。**未知**

### 总结 ###

在这么一番类比之后，不难看出的现实是是 PineTab 即使没有产能上的问题，由于在多媒体娱乐方面的短板，很难争得开放硬件极客团体之外的人群青睐，也不更可能对市面上行销的封闭软硬件生态圈的平板市场造成任何影响。而对于看重开源 ARM 平台的软件极客们，旗下的 [Pinebook Pro](https://www.pine64.org/pinebook-pro/) 倒是个更有吸引力且成熟度更高的产品。没错，它凭借生产力工具和做工方面的优势，是个比基于 Raspberry Pi 底板的笔记本壳更好的教育用电脑选择，但恐怕若干年后人们回想起这款设备时，更多的会是它的作为“首款转为 Linux 打造的开源硬件平板”的概念意义，而非其市场价值。。

对于笔者来说，上述 DIY 出来的便携式组合，在另配了显示器支架和 PD 插头后，变身成了家中的轻量级学习专用电脑，继续发挥着用途。
