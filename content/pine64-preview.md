Title: Pine64 初评
Date: 2016-05-11 18:17:27
Author: lovenemesis
Category: Embedded
Tags: pine64
Slug: pine64-preview

Pine64 是一个于 2015 年 12 月在 [Kickstarter 举行众筹](https://www.kickstarter.com/projects/pine64/pine-a64-first-15-64-bit-single-board-super-comput)的 SBC，当时宣传的亮点是首个 $15 的 64位 SBC。这里跟大家分享下笔者在上月初收到的 2G Plus 版本。

<!-- PELICAN_END_SUMMARY --> 

尽管 Pine64 将 $15 放入到标题中大肆宣传，实际上那个仅仅是 512M 内存的入门版本，实在是做不了太多……于是当初笔者选择其中的顶配型号，配置如下：

### Pine64+ 2G 版

* 全志 A64 四核 CortexA53 ARMv8 1.2GHz
* Mali400MP2 双核 GPU
* 2G DDR3 内存
* 千兆以太网卡
* USB 2.0 * 2
* 支持从 USB 或者 microSD 卡引导
* HDMI 1.4a ，支持 4K30p 回放
* 支持蓝牙 4.0 及 WiFi 扩展模块
* 提供与 Raspberry Pi 兼容的 40pin GPIO
* 尺寸 133mm x 80mm x 19mm

这个版本 Kickstarter 的价格是 $29，相对于基础的 $15 可谓贵了不少。加上 $12 的全球运费，到手价是 $41。

对于这 $12 的运费不得不吐槽下：至少笔者这个版本是从深圳的制造厂用圆通经济送达的，典型的*花美金的价格享受人民币的服务*……

### 做工及配件

矩形的[板子做工](http://files.pine64.org/doc/Pine%20A64%20Schematic/A64-DB-Rev%20B-TOP%20Preliminary.pdf)中规中居，尺寸上比树莓派大不少，常用的 I/O 接口分别位于板子两个短边，扩展接口在板子两个长边，接外设不会干扰，元器件之间布局宽松。2G 内存版本是 4 个 512M 的颗粒，PCB 版正反各两个。

另一个值得吐槽的：附赠了一个小的电源开关，然而它被随意的放置在快递包装袋中，没有放在板子包装盒中，差点儿便被我丢弃。需要找个焊锡固定在 USB 接口旁的 POWER 或 RESET 位置后才能使用。

本想到手后随便淘宝个外壳，怎奈这还是稀少品，唯一的[亚克力外壳售价 99 元](https://item.taobao.com/item.htm?id=530367699491&ns=1&abbucket=15#detail)，呃……然后寻求 3D 打印服务，然而某宝上对于[其社区创建的图纸](https://www.pine64.com/downloads)给出的报价是 260， 呃……最后发现[盛装 AmazonBasics 电池的纸盒](https://www.amazon.cn/dp/B0030T1NEU/) 尺寸接近且软硬适中，于是 DIY 了一个外壳先凑和着吧。

众筹时官方搭配的 5V 2A 电源价格偏高，于是再次购入 [QC 2.0 的充电器](https://detail.tmall.com/item.htm?id=524392365245)，价格实惠运行稳定。

通常的[树莓派用散热片](https://item.taobao.com/item.htm?id=529564632386)也是可以继续用在这个上面，其 SoC 和外围控制芯片大小与树莓派一模一样。

### 软件及性能

既然 SoC 是全志出品，估计你也猜到了其 Linux 的支持水平：**能用，但问题不少**。根据[更新相对及时的 Wiki 页面](http://wiki.pine64.org/index.php/Main_Page#Software.2FImage_Download)上显示，目前已经有基于它订制内核的 Debian Jessie + MATE 和 Ubuntu Xfce 两个发行版，众筹时宣传的诸如 OpenWrt 什么的还没见到。论坛上其他的人使用中也时常遇到些奇葩的小问题。

如果不介意其停留在 3.10 的内核及问题多多的 Linux OpenGL 加速的话，还算基本能用，不过是完全无法跟接近 Kernel 主线支持的 Rapsberry Pi 相比较，意料之中。
Kodi 及其各类基于它的 Linux 发行版并没有支持 PINE64 的计划。

鉴于此，Android 其实是将其投入桌面应用的唯一可行方案，也是笔者当初购买时的初衷。于是烧入其官方认为相对稳定的 Android 5.1.1 版本。

安兔兔 6.1.5 得分如下：

* 3D性能：1073
* UX性能：10457
* CPU性能：10001
* RAM性能：3340

基本就是去年中端机的水平，不出彩，不过大部分应用也能跑。最新的固件包含谷歌框架，支持 Root，支持 OTA 升级，支持 USB 键盘，但**不支持** USB 无线网卡和 HDMI CEC。

### 使用体验

如上所说，Linux 桌面应用当下是比较骨感，于是在这一个月来都是配合[空中飞鼠](https://detail.tmall.com/item.htm?id=19487710893)当做电视盒和高清播放机使用的，配合各类视频应用和 Kodi，稳定流畅，应用订制上比价位接近的电视盒要省心不少。

若作为 Linux 服务器，其造型和接口布局则是个问题。这个尺寸完全无法用于常见的 Raspberry Pi 集群支架，网线和 USB 分开的布局虽然方便了桌面应用，但是对于在空间有限的柜子里部署 USB 类设备和网线布局则会造成麻烦。

进入 2016 年来，市场上 64 位的 SBC 明显多了不少，PINE64 的价格优势在考虑了邮费之后并不明显，除非国内有分销商。其社区成熟度及 Linux 支持度远远不如 Raspberry Pi。所以若是您在寻求一个适合 Linux 的 SBC，RPi3 或许依然是您最好的选择；若是只是想要一个高度可订制的 Android 电视盒的话，PINE64 倒是一个相当吸引人的方案。

[PINE64 官方商店](https://shop.pine64.com/)

[PINE64 官方 Wiki](http://wiki.pine64.org/index.php/Main_Page)
