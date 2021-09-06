Title: Linux 手机评测：Sony Xperia X UBports 版
Date: 2021-09-06 22:00
Category: Gadget
Tags: ubports, xperia
Slug: linux-phone-review-ubports-sony-xperia-x
Authors: lovenemesis

尽管使用 Linux 内核的 Android 手机已经遍地都是，但严格意义上以嵌入式 Linux 作为系统的手机却并不那么常见。这个领域从业界传统的大牌合作 [MeeGo](https://zh.wikipedia.org/zh-hans/MeeGo) 到后来的 [Sailfish OS](https://sailfishos.org/)，从昙花一现的 [Firefox OS](https://support.mozilla.org/zh-CN/products/firefox-os) 到野心勃勃的 [Ubuntu Convergence](https://ubuntu-touch.io/zh_CN/convergence) ，经过各路高手一番厮杀之后，怎奈定夺天下的却是那个套了层 Java 马甲的 Android。时隔数年，在这个由 Android 和 iOS 二分天下的现世，已经边缘化的 Linux 手机发展的怎么样了呢？不妨随着笔者“搜刮”来的这台 Sony Xpeira X UBports 版一探究竟吧！

<!-- PELICAN_END_SUMMARY -->

### 配置及对比平台 ###

Ubuntu Touch 是 Canonical 在 2014 年间野心勃勃的 Convergence 方案的产物，然而在和当年的机圈新秀 OnePlus 合作推出过一个开发机之后，就在 Android 阵营的机海围剿下放弃了。虽说如此，其前瞻性的融合概念，依然俘获了不少极客的心，于是他们围绕其组建了 UBports 社区，独立于 Canonical 继续开发。Sony Xpeira X 便是在 UBports 社区接盘后由志愿者后续开发支持的设备。在社区维护的[产品支持完备程度列表](https://devices.ubuntu-touch.io/)中包含了 58 款设备，[Sony Xpeira X 完备度为 83%](https://devices.ubuntu-touch.io/device/suzu/)，与其近期主推的 [Volla Phone 的 83.7%](https://devices.ubuntu-touch.io/device/yggdrasil/) 十分接近，可以充分代表当下 UBports 现阶段在近期设备上的状态。作为对比，更有历史的 [Oneplus One](https://devices.ubuntu-touch.io/device/bacon/) 和 [Nexus 5](https://devices.ubuntu-touch.io/device/hammerhead/) 分别为 93.5% 和 89.6%，而现在开发火热到断货的 [PinePhone 完备度才 42.1%](https://devices.ubuntu-touch.io/device/pinephone/) ……

回到笔者手头这台从亲戚那边“搜刮”来的港区双卡高配版 Sony Xpeira X ，其配置如下：

* big.LITTLE 两大四小结构的 ARMv8 Snapdragon 650 SoC，以及 Ardeno 510 GPU
* 3GB RAM 及 64GB ROM
* 802.11ac WiFi 5 和蓝牙 4.2
* 双卡双待，支持 4G FDD LTE
* microUSB 2.0 接口，支持 OTG，无视频输出
* 前置 13MP 和后置 23MP 摄像头
* 5 寸 1080P 屏幕
* 2620mAH 电池

毕竟是 2016 年的设备，若将其与近两年 Android 阵营的手机比明显是不讲武德，但其在 SoC 和网络部分依然比同样是 Linux 手机新秀的 PinePhone 强出不少，只是受限于时代，缺少 PinePhone 的全功能 Type-C 接口。为了便于理解，接下来笔者将使用一台刷入 [LineageOS](https://lineageos.org/) 的 [Sony Xperia XA2 Ultra](https://wiki.lineageos.org/devices/discovery) 做对比，看看在同样是开源社区主导的前提下 Linux 手机与常见 Android 手机在体验上孰优孰劣。

### 系统安装 ###

UBports 方面使用[最新的 OTA 18 版本](https://ubports.com/blog/ubports-news-1/post/ubuntu-touch-ota-18-release-3764)，虽然仍基于非常古老的 16.04 LTS 版，但在应用程序框架方面已经换用现代的 Qt 5.12 版本。LineageOS 方面则使用最新基于 [Android 11 的 18.1 版本](https://lineageos.org/Changelog-25/)。

由于都是第三方系统，安装配置部分两个手机步骤相同，都是需要首先通过厂商提供的途径解锁 `bootloader` ，后刷入特定的 `recovery`，再用该 `recovery` 引导并刷入新系统镜像。只是 UBports 需要在 Ubuntu Touch 系统镜像之上再刷入由厂商提供的 BSP 和底层包。不过这一切幸好都有来自 [UBports Installer](https://ubuntu-touch.io/get-ubuntu-touch) 提供向导指引，过程直观易懂。在笔者的操作中，一次成功，故不再赘述了。

两个系统的共同之处还在于[同源的硬件抽象层](https://docs.ubports.com/en/latest/porting/index.html#what-is-ubuntu-touch)，UBports 使用的名为 [Halium 的 HAL 层](https://halium.org/)既是基于 LineageOS 的。

### 设置及驱动 ###

UBports 使用一套衍生自 Unity8 称为[Lomiri](https://lomiri.com/)的融合式桌面环境，采取了一套非常直观易上手的全屏手势进行交互操作：

* 屏幕左侧向内轻滑出应用程序启动器及快速启动栏，进一步滑动或者点击 Ubuntu 图标展开全部应用程序；
* 屏幕右侧向内轻滑进入多任务管理界面，可以通过卡片式界面在多个应用中切换，或者拖动上滑关闭;
* 从屏幕上方向下滑则展开多面板设计的通知栏区域，可以快速访问并配置系统。

但稍作把玩，在颇具实用性的交互界面之下，可以看到其在硬件驱动支持方面的不足：

* 无法使用指纹识别
* 无线热点共享不可用
* 无法识别 NFC 感应器（因为该款设备为 Android 7 兼容硬件）
* 不支持 FM 广播
* [VoLTE 支持](https://ubports.com/blog/ubports-news-1/post/first-steps-in-volte-support-for-ubuntu-touch-3768)还比较遥远

此外，由于笔者手头这台由于未知的原因，USB OTG 和 USB ADB 都不可用……

LineageOS 在 AOSP Android 11 的基础上，大量融合了来自社区的开发成果：

* 交互方面全屏手势、双按钮、三按钮都支持，通知栏快捷图标既可长按亦有下拉式菜单。
* 系统内建情景模式，可以根据连接设备或者其他传感器在诸如汽车、静音或者自定义场合下全局性的切换系统操作行为。
* 几乎所有可视化的地方都可以自定义，从最基础的图标字体颜色，到进阶的屏幕色彩配置及全局音效，到极具可玩性的自定义按键及手势组合
* 无线热点支持单独分享 5G 频段
* USB OTG 支持 exFAT 存储设备

硬件支持也比较全面，FM 广播、NFC和指纹识别等均可用。

### 安全及隐私 ###

LineageOS 和 UBports 在其首页介绍上都特别强调了相对于一般 Android 手机在安全和隐私保护方面的优势。实际中如何呢？

* 安全：使用 UBports 的 Xperia X 尽管硬件配置差一截，但无论是首次开机、后续开机还是重启速度都要稍快一些。究其原因，实际上是因为运行 LineageOS 18.1 的 Xpeira XA2 Ultra 默认启用了全盘加密，每次开机需要使用多一些的时间执行解密操作。另一方面，LineageOS 比 UBports 不仅可以使用更便捷的生物指纹解锁方式，在传统的 PIN 码解锁上也提供了乱序排列以及更长的数位支持，安全性考量更周全。
* 隐私：UBports 内嵌的 VPN 类型倒是 OpenVPN，但没有诸如私人 DNS 之类的加密 DNS 支持，或者第三方 Socket 类通道的支持。LineageOS 尽管内嵌 VPN 支持仍然是传统的 PPTP 和 IPSec 系列，但内建完善的私人 DNS 支持，且可以通过第三方应用大幅度扩展支持的 VPN 类型，成熟度更好。两者受限于较老的内核版本，都没有 WireGuard 的内核级别支持。
* 匿名：从最基本的层面来看，两者都允许在不登陆任何第三方账户的情况下直接使用。但 LineageOS 支持接入 WiFi 时使用随机 MAC 地址，而 UBports 还没有这个功能。深入的来说，两个系统都是基于厂商提供的 BSP 和底层包实现的，落后于在固件级别都是开源的 [PinePhone](https://www.pine64.org/pinephone/) 或者 [Libram 5](https://puri.sm/products/librem-5/) 。

于是仅从上面三个角度来看，UBports 所谓的安全和隐私优势其实也就只是倚仗着系统比较小众而已，功能上其实不如 LineageOS。

### 软件生态 ###

UBports 的预装应用覆盖了通常的手机用途，从必备中文输入法到终端模拟器一应俱全，如果只是备用机的话完全不需要再多装什么了。同时它也内嵌了名为 OpenStore 的软件市场供下载安装第三方应用。[UBports 上的的应用大致分为两类](https://docs.ubports.com/en/latest/appdev/index.html)：

* 使用专属的 SDK 框架的开发，以 Qt 框架为基础的原生应用
* 基于 HTML5 容器化封装到 QtWebEninge 中实现的网页应用

如果要使用桌面版 Linux 上那些熟悉的应用，需要在系统中启用名为 [Libertine 的容器化方案](https://docs.ubports.com/en/latest/userguide/dailyuse/libertine.html)才能实现，之后该方案还还面临如下问题：

* 基于的 Ubuntu 16.04 版本上的桌面 Linux 应用程序并没有为了考虑适配小尺寸触摸屏幕而采取自适应布局的，几乎都需要连接鼠标键盘和外置显示器才能实现基本的交互；
* 由于是容器化方案，输入法框架和用户主目录自然是完全独立的两套，实际使用中数据的互通存在障碍；
* GUI 性能不佳。幸好终端还能通过 apt 安装一些应用，弥补系统自带终端模拟器的不足（原因后续会介绍）。

类似的，也可以配合使用 QEMU 的[另一套容器化方案 Anbox ](https://docs.ubports.com/en/latest/userguide/dailyuse/anbox.html)来使用 Android 应用，不过这个方案也面临一些问题：

* 需要借助 adb 在系统层面激活安装；
* 从第三方的视频和其他用户的使用体验来看，目前的兼容程度距离通常意义上的 Beta 还很远；
* 运行 QEMU 带来的额外负载会导致系统发热严重

等下，那么之前所谓的 Convergence 融合在哪里呢？
根据 [UBports 的沿用自 Ubuntu Touch 的文档](https://docs.ubports.com/en/latest/humanguide/index.html)描述，"融合"其实仅限定于使用其专属 SDK 框架开发的原生新应用，通过在开发阶段制定的一些人机交互基准，确保最终的应用可以覆盖从触摸屏手机到键盘全尺寸电脑在内的各种交互场景。

基于上述原因，接下来将以 [UBports OpenStore](https://open-store.io/) 上下载的原生应用对比 LineageOS 上[开源商店 F-Droid](https://f-droid.org/zh_Hans/) 中的 Android 应用程序，看看 UBports 在各种场景下的体验如何。

#### 即时通讯 ####

* [TELEports (BETA)](https://open-store.io/app/teleports.ubports) vs. [Telegram FOSS](https://f-droid.org/zh_Hans/packages/org.telegram.messenger/) 及 [Nekogram X](https://f-droid.org/zh_Hans/packages/nekox.messenger/)：UBports 上的这款电报协议客户端为其社区团队重点开发，亦是 OpenStore 通讯类下载量第一的应用。尽管如此，目前在功能可用性及稳定程度上还的确处于 Beta 状态。相比之下，F-Droid 中的则有 Telegram 的开源版本，剔除了上游源代码中的闭源二进制组件且移除了 GCM 推送的依赖，保留了主要功能和更可靠的稳定性。此外还有第三方的 Nekogram X 备选。

* [FluffyChat](https://open-store.io/app/fluffychat.christianpauly) vs. [Element（曾为 Riot.im）](https://f-droid.org/zh_Hans/packages/im.vector.app/)：OpenStore 通讯类下载量第二的应用为基于 Matrix 协议的，界面设计和稳定性都还不错，但欠缺关键的消息加密支持…… 而 F-Droid 提供的 Riot.im 继任者 Element 在完备度保持了当年的水准，跟服务器的协议兼容性也很好。

* [ConverseJS XMPP client](https://open-store.io/app/conversejs.povoq) vs. [Conversations](https://f-droid.org/zh_Hans/packages/eu.siacs.conversations/)：说实话真没想到手机 Linux 平台代表的 UBports 上的 XMPP 客户端仅有一个如此简单的 JavaScript 库外壳，跟桌面版 Linux 上众多的可选项完全不在一个级别。相比之下 F-Droid 中不仅有 Conversations 这种 XMPP 业界标杆性的应用，还有一些零星的第三方实现备选。

另外 Ubports 上还有一款基于 Signal 协议的客户端[Axolotl Beta (Signal)](https://open-store.io/app/textsecure.nanuc)，但目前其完成程度较低。F-Droid 中并没有相似应用。

#### 视频音乐 ####

* [Video Player](https://open-store.io/app/uvideo.pavelprosto) vs. [VLC](https://f-droid.org/zh_Hans/packages/org.videolan.vlc/)：UBports 自带的视频播放器似乎仅是为了播放相机录制的 mp4 视频而存在，播放其他来源的视频居然需要原地复制一个才行，实在诡异。此外，无法回放开源无专利限制的 WebM 视频格式，需要借助名为 Video Player 的应用实现，然而这个应用也仅仅提供了基本的播放功能而已。相比之下 F-droid 中则能找到大名鼎鼎的 VLC，继承了桌面版丰富的配置和完善的格式支持，完全碾压 UBports。
* [UBports 自带相机](https://open-store.io/app/com.ubuntu.camera) vs. LineageOS 自带相机 + [Open Camera](https://f-droid.org/zh_Hans/packages/net.sourceforge.opencamera/)：UBports 的自带相机功能非常单纯，在基本的拍照和视频背之外，藏在磨砂玻璃质感的设置按钮后面的功能也就只有网格线和 HDR 模式了。相比之下 LineageOS 提供了包括白平衡、ISO、手动曝光时间控制等选项，且预制了一系列场景模式和滤镜效果。此外，在 LineageOS 上还可以选择[Open Camera](https://f-droid.org/zh_Hans/packages/net.sourceforge.opencamera/)以实现存储 SD 卡、蓝牙遥控、包围式曝光等更多高级功能。

两个平台上都有不少播客订阅应用，因为不是此类目标用户，不便比较。

#### 生活工具 ####

* UBports 自带中文输入法 vs. [OpenWnn Legacy](https://f-droid.org/zh_Hans/packages/com.googlecode.openwnn.legacy/) 及 [Trime](https://f-droid.org/zh_Hans/packages/com.osfans.trime/)：从开箱即用的角度来说，UBports 自带的输入法要友好很多，词库也不算太久。相比之下 6 年未更新的 OpenWnn 依然保留了 Android 2.X 时期的风格，在新系统下使用颇为别扭。而更新的 Trime 需要花些功夫配置才能使用，除非在 PC 上已经是该输入法的用户，那么只需要将导入配置即可。
* [Pure Maps](https://open-store.io/app/pure-maps.jonnius) + [OSM Scout Server](https://open-store.io/app/osmscout-server.jonnius) vs. [OSMAnd~](https://f-droid.org/zh_Hans/packages/net.osmand.plus/)：同样是基于 OpenStreetMap 的实现，UBports 上的软件组合在稳定性和地图显示效果相比 LineageOS 上的方案还是差了不少，而且离线地图只能按国家缓存，不支持省份级别的分块下载实在是不方便。而 OSMAnd~ 尽管由于缺少实时路况信息导致给出的路线不一定合理，至少还是能在中英混杂的 TTS 艰难前行的。
* [Document Viewer](https://open-store.io/app/com.ubuntu.docviewer) vs. [OpenDocument Reader](https://f-droid.org/zh_Hans/packages/at.tomtasche.reader/)：两者都是基于 LibreOffice 相关技术开发的用来阅读 ODF 及 PDF 文档的阅读器，在简单的文档使用体验上比较接近，细节上各有千秋。Document Viewer 支持单独的夜间模式切换，而 OpenDocument Reader 只是简单的跟随系统设置；Document Viewer 在 ODS 表格的显示上精准还原桌面端效果，但稳定性和打开速度稍慢。而 OpenDocument Reader 支持简单的编辑功能。
* UBports 自带浏览器 Morph vs. LineageOS 自带浏览器 Jelly：在 [HTML5Test](https://html5test.com/) 中，UBports 自带浏览器被识别为运行在 Chrome 77，得分高达 478，比本文撰写时 Firefox 92 Beta for Android 的 474 还要高，但使用之中却有些许小问题，比如不支持 DRM、WebGL 初始化错误等等。作为比较，被标识为 WebView 91 的 LineageOS 自带浏览器 Jelly 继承了 Chromium 的界面风格和清爽的使用体验，用起来没什么可以抱怨的。此外，F-Droid 还提供了基于 Firefox 的 [Fennec](https://f-droid.org/zh_Hans/packages/org.mozilla.fennec_fdroid/) 和老牌轻量级浏览器 [Midori for Android](https://f-droid.org/zh_Hans/packages/org.midorinext.android/) 以备更关注隐私保护的 LineageOS 用户选择。
* UBports 自带终端模拟器 vs. [Termux](https://f-droid.org/zh_Hans/packages/com.termux/)：由于 UBports 为了保证系统大版本 OTA 的平滑升级，整个系统分区是只读状态。于是尽管预装了，但相对于桌面版 Linux 的终端模拟器的多样玩法，其功能性只能说半残，也就跑个 SSH 客户端吧。而 Termux 则为 LineageOS 提供了一套精简的 Linux 工具集，并可以用其内置软件包管理工作扩展用途，可玩性很高。

#### 游戏娱乐 ####

无论是 UBports 的 OpenStore 还是 LineageOS 的 F-Droid，在其中都能找到大量诸如数独、2048、各种棋类的益智类的游戏，以及一些简单的冒险类和街机类游戏，打发时间足矣。若要追求沉浸感的体验，需要另辟蹊径：

* [GearBoy Color](https://open-store.io/app/gearboy.bhdouglass)：UBports 上的活跃开发的 GBC 模拟器，从评论来看还原度、操作和性能都不错，可以尝试。非 GBC 玩家，无法比较与实体掌机的差异。
* [Dolphin Emulator](https://f-droid.org/zh_Hans/packages/org.dolphinemu.dolphinemu/)：F-Droid 上活跃更新的 Wii 和 GameCube 模拟器，其 PC 版本历史悠久且口碑不错，其 Android 版本目前仍处于 Alpha 状态。非 Wii 或 GameCube 玩家，无法比较与实体主机的差异。
* [Moonlight Game Streaming](https://f-droid.org/zh_Hans/packages/com.limelight/)：F-Droid 上活跃更新的游戏串流客户端，可以将 PC 端的游戏串流至手机游玩，支持各类手柄和移动网络传输，由于仅限 N 卡用户，无缘体会。
* [Chiaki](https://f-droid.org/zh_Hans/packages/com.metallic.chiaki/)：F-Droid 上的 PlayStation 游戏串流客户端，可以将 PlayStation 4 和 5 上的游戏串流至手机游玩，相比官方的 RemotePlay 应用，支持各类手柄且可仅局域网通讯。已尝试，效果喜人。

#### 区域相关 ####

和现今很多的事物一样，在朝内使用手机还有一些绕不开的地区性问题需要面对：

* 系统更新站点的访问速度：感谢各大高校 Linux 用户组的支持，UBports 和 LineageOS 的系统镜像在朝内都有镜像，下载系统更新的速度还是有保证的。
* 软件应用站点的访问速度：OpenStore 使用了 CDN 加速访问，在多个 ISP 下测试了访问速度尚可。F-Droid 可以在其中[配置 TUNA 提供的镜像](https://mirrors.tuna.tsinghua.edu.cn/help/fdroid/)，速度也不错。
* 安装第三方应用：UBports 和 LineageOS 都是允许安装商店之外的第三方应用(实际上 F-Droid 商店本身即是第三方应用)的，可以通过 PC 端的网页下载后再导入手机。但 UBports 上的应用几乎都在 OpenStore 上架了，这个功能用途不大。而在 LineageOS 则可以下载一些其他站点上的为 Android 平台设计的开源应用，譬如 [Tux Paint](http://www.tuxpaint.org/) 和 [RetroArch](https://www.retroarch.com/index.php?page=platforms)。
* 各地区健康码：鉴于 COVID-19 导致的疫情，现在朝内出门都免不了被要求出示健康码。有些地区的健康码可能允许基于 HTML5 的访问，但有些地区的健康码仅能使用绑定了用户信息的微信或者支付宝扫码才可。在后者的情况下，UBports 无解。而 LineageOS 尚可诉诸上一条中方案下载第三方应用妥协。

### 总结 ###

经过这么一圈对比下来，不难看出尽管现在有了诸如 PinePhone 这样火热的硬件平台，Linux 手机要追上有商业公司财力背书的 Android 和 iOS 平台要走的路还很长：

* 前瞻性的融合概念仍未落地，符合其框架的桌面应用几乎没有，而依据其框架开发的移动端应用相比同类型的现有桌面端应用还很不完善；
* 硬件方面明显仅靠一个想买也买不到的 PinePhone 是远远不够的，需要在后装机型覆盖上接近 LineageOS 的程度才有竞争力；
* 软件方面开发平台的版本过于陈旧（目前还是基于 16.04 的），虽说独门全屏手势交互很好，怎奈从功能角度在全部领域都落后于 Android 平台上的同类开源软件。

文末，笔者看着订单列表里付款一年了都没发货的 PinePhone，心情颇为复杂……