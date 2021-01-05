Title: PineBook Pro 评测
Date: 2021-01-05 12:00
Category: Gadget
Tags: manjaro, armbian, pine64
Slug: pinebook-pro-review
Authors: lovenemesis

2020 年的电子产品为消费者钱包考虑甚多：光发布，买不到。自从去年底得知 [Pinebook Pro](https://www.pine64.org/pinebook-pro/) 的存在和年初的小范围发售后，上半年笔者遍尝各种渠道尝试购入一台，毕竟全尺寸 ARM 笔记本并不是那么常见。究其无果后下半年最终在[某宝](https://item.taobao.com/item.htm?id=626530998190)额外支付了相对海外税前定价 50% 的费用（官方定价 $199，国内“官方代理”标价 ￥1999，笔者订单价 ￥2198 约合 $300）后， 又开启了的一轮似乎更有盼头的等待。终于在 Apple 都憋出了同样是基于 ARM 的 MacBook Air 之后，笔者在本月初收到了 PineBook Pro，经过一周的使用和折腾后，跟大家分享下体验。遵循本站一贯的风格，本文绝对跟您在其他地方读到过关于 PineBook Pro 的评测不同。

<!-- PELICAN_END_SUMMARY -->

### 配置及对比平台 ###

尽管同属 Pine64 出品，PineBook Pro 的硬件配置相比之前的 [Pine64](https://linuxtoy.org/archives/pine64-review.html) 以及 [PineTab](https://linuxtoy.org/archives/lightweight-portable-desktop-with-pine64.html) 有着显著的不同。PineBook Pro 主要配置升级为：

* big.LITTLE 两大四小结构的 Rockchip RK3399 SOC，以及强大很多的 Mali T860 GPU
* 4GB LPDDR4 内存
* 支持 [802.11ac WiFi 5 和蓝牙 5.0 的无线模块](https://wiki.pine64.org/wiki/Pinebook_Pro#Bluetooth_and_WiFi)，单天线设计
* 具备 USB 3.0 Type-A 和 [PCIE 4x NVME 扩展](https://wiki.pine64.org/wiki/Pinebook_Pro#Using_the_optional_NVMe_adapter)
* 具备一个**全功能的 USB Type-C 接口**，支持 15W PD 充电、3.0 数据传输和视频输出
* 可升级的 64G eMMC 内部存储和 microSD SD3.0 读卡器
* 操作系统无关，固件级别的 WiFi、麦克风和摄像头隐私开关
* [14寸 1080P IPS 屏幕，250 nit 亮度](https://wiki.pine64.org/wiki/Pinebook_Pro#LCD_Panel)
* 10000mAH 电池
* 铝镁合金外壳，无风扇全被动散热设计

相比之前的产品，PineBook Pro 至少在外围接口领域至少跟上了现在的主流标准。然而在某宝上仅需比笔者订单价在多支付三四百元，便能购入的一台性能看起来更有优势的全新 X86 笔记本，譬如以 HP 星14 青春版为代表的搭载 Ryzen Mobile R3 3250U 的笔记本，若是二手市场则选择更为广泛。在本文接下来的体验中，笔者将时不时结合手头稍早型号的 Ryzen Mobile 2500U 轻薄笔记本作为参考进行比较。

### 外观做工 ###

由于购买渠道的特殊性，笔者的 PineBook Pro 的开箱即是拆开套娃快递盒的过程，五层包装后终于到最后一层那个平淡无奇，仅仅在左下角便利贴表示为 ANSI 的原浆色本体包装盒，小巧的 15W 圆孔电源适配器单独在另一个白色的盒子里。1.2KG 的 PineBook Pro 本体纯黑色的外壳，铝镁合金的 A 面和 D 面表面没有使用任何拉丝或者磨砂工艺，轻度指纹收集器。值得一提的是，它的屏幕的下边缘尽管没有部分游戏本那样垫起 D 面改善散热的作用（因为 D 面本来就有四个巨大的圆形橡胶垫），但依然不能展开至 180 度。当然不是大问题，但这对于习惯了 2-in-1 的笔者来讲差点导致开箱即杯具……此外笔者收到的估计是九月份生产的最后一批预装预置 Debian 的版本，虽然并非预装开箱体验更好的 Manjaro KDE，但也没有年初早期版本诸如 WiFi 隐私启用、屏幕排线异常或者扬声器排线错误的问题。类似 MacBook Air 的整体设计的全黑机身低调沉稳、毫不张扬，若不是底部强制性的 FCC 标签可谓毫无特征。它做工方面可以说尚可，硬质塑料的 B、 C 面与 A、D 铝镁合金面的接缝基本规整，但估计模具设计优先考虑易拆卸，面板接缝处于单手抓持时候的掌心部分，虽说不至于割手，但还是能感受到接缝的存在。做工之外，硬件本身素质如何呢？

* 这块屏幕的 250 nit的亮度、1000:1 的对比度、63% sRGB 的色域覆盖、不可调整的 1080P 分辨率和 60Hz 刷新率的参数非常高调的彰显着“为软硬件开发人员省钱”的设计思想，并不适合影音娱乐和图像处理。不过若在写代码之余仅仅用来玩玩怀旧的模拟游戏或者看看动漫，那还是毫无问题的。基本上**明显落后**相近价位的 X86 笔记本。
* 扬声器是另一个高调彰显上述设计思想的地方，本身高频走音低频不在中频声音还有点儿小，位置又在 D 面朝下，导致最终外放效果还不如手机。不过它依然贴心的保有 3.5mm 耳机麦克接口，不影响戴耳机写代码的极客们，但总体上还是**落后**相近价位的 X86 笔记本。
* 无线模块虽说是 802.11ac 了，但受制于单天线设计，WiFi 5 理论速率上限只有 433Mbps，且若是同时开蓝牙的话会影响同频段 2.4G 的 WLAN 连接。笔者实测了在 802.11ac 网络配合蓝牙 5.0 耳机观看流媒体视频，并未觉察到影响，所以现阶段可以认为与相近价位的 X86 笔记本**持平**。当然最好的检测方法是联网游戏，不过目前软件生态不允许……
* 电池从容量上来说确实够大，且结合 ARM 低负载时低功耗的特性，根本不用在诸如午餐时段走开的时候进入睡眠模式。仅仅是轻度网页配合文字工作的话，满充后显示可以工作 14 的小时，完整覆盖工作和加班时间，**领先**于这个价位的 X86 笔记本。
* 放置于室温 24 度的咖啡厅桌子上时，空闲时 `sensors` 报告 Pinebook Pro 温度 30.3 度，而以高负载状态播放 1080P 在线视频时则飙升至 52.8 度，显得烫手（或膝盖）。相比之下笔者的轻薄本在默认散热配置下负载稍微高些便会启动风扇主动散热，哪怕如此高负载情况 68度的运行温度也很常见。需要注意的是估计是电源回路的设计因素，若边充边用的话，温度会变得更高。从笔记本的主要使用场景上来看，笔者认为 PineBook Pro 这方面是要**优于**相近价位的 X86 笔记本的。
* 由于编辑区以 Fn 的方式实现，实际上这款 14 寸本本的键盘可用按键数还不如用作对比的 13 寸轻薄本多，特别是原先是 DEL 的位置变成 POWER 键还是需要稍微适应下的。但键盘的手感却令人眼前一亮，敲击感和键程调教的拿捏适中，远超大多数轻薄本的软棉塑料感；而声音则些许清脆却不会太吵以至影响周围。不足之处恐怕的就是背光的缺失和在无从考证的耐久性了。无按钮设计的触控板足够宽大，支持多点触控，可以配置边缘手势操作。另外一个很小但也可称为优点的地方是键盘鼠标的固件都可以通过开源工具刷写。整体体验上 Pinebook Pro **优于**相近价位的 X86 笔记本。

SoC 和内存等组件和软件紧密相关，不同发行版上的体验还真有那么一些差别，所以且容笔者慢慢道来。

### 软件体验 ###

Pinebook Pro 特别为系统折腾者考量，默认启动顺序为 SD 卡、USB 接口最后是内置 eMMC，PCIE 的 NVME 是不能用作系统引导的。这种引导顺序代表着完全可以将 SD 卡中的系统当作主力系统使用，尝试多个不同系统也仅需替换下 SD 卡即可。若之后是对 SD 卡中系统满意，则可以便捷的使用 `dd` 将镜像写入至 eMMC 即可。速度方面，本来其内置 eMMC 也仅仅是处于中阶水平，读写性能跟 SanDisk Extreme 接近。所以若是手头 SD 卡足够快的话，完全不必纠结写入 eMMC。

笔者这台 Pinebook Pro 预装的还是 Debian Jessie 9 版本，完全没有想用的欲望，于是自然而然的想到了之前在 Pine64 上使用的 [Armbian 的 PineBook Pro 版本](https://www.armbian.com/pinebook-pro/)，这次它推荐的是基于 Ubuntu 20.04 LTS 主线 5.9 内核的版本，默认使用 Xfce 桌面环境。它继承了 Ubuntu 的便于配置和广泛第三方软件支持的优点，比如原生支持 ARMv8 的 [WPS Office for Linux 版本](https://linux.wps.cn/)和 [VS Code](https://code.visualstudio.com/Download)。但从另一方面，由于是 LTS 版本，核心软件的版本趋于保守一些，譬如 Mesa 还是 20.0 版本，对于 Pinebook Pro 所依赖的 T860 逆向工程驱动 Panforst 并没有与时俱进。所以在简单试用了 Armbian 之后，转而选择近几年很火且对于 Pinebook Pro 支持很上心的 [Manjaro ARM Xfce 版本](https://www.manjaro.org/download/#pinebook-pro-xfce) 体验一下。

#### Manjaro Pinebook Pro Xfce ####

这个体验的开始过于顺畅，而结束却又过于突然……

Manjaro 20.10 提供的开箱体验虽不比 Fedora Workstation 和 GNOME 高度集成的初始化设置，但其友好性还是略胜 Armbian。在终端界面设置了常用用户名和密码后很快便启动图形化界面，进入 Xfce 环境，内存占有与保持了与 Armbian 相近的 630M 左右，然后……然后很快的发现触控板不支持 Tap-to-Click 轻触即点击！Pinebook Pro 和近些年的大多数的笔记本一样，触控板部分并没有独立的实体键，在没有“轻触即点击”的情况下只能通过按压左下方和右下方的方式模拟鼠标操作，相当不便。同时多点触控滚动手势也随之丢失……这个对于笔记本的使用场景来说体验降分非常严重的问题竟然在 Manjaro Xfce 版被忽视了实在让笔者感到惊讶。经过搜索发现这个是 Manjaro Xfce 版本的普遍问题，但在根据说明折腾了一圈 libinput 配置后并没有什么改观……但在 Pinebook Pro 上情况似乎更令人迷惑的是一些，因为同样的 libinput 的配置在 Armbian Focal Xfce 则完全没有这个问题……

好吧，既然 Pinebook Pro 提供了拔插 SD 卡即可更换系统的便利，看来现在就是利用此技能的时候了，于是……

#### Manjaro Pinebook Pro KDE ####

作为第二批 Pinebook Pro 的默认预装系统，Manjaro KDE 版本在开箱体验上明显得到了足够的打磨，进入图形化界面后这方面的优势展现无疑：首先，触控板如预期那般支持“轻触即点击”和多点触控滚动手势；其次 KDE 充分利用了 Panforst 的 OpenGL 加速效果，整体桌面体验上流畅度和视觉效果兼顾。但深入体验下来，还是能发现一些值得更进一步改善的地方。

* 触控板右键：尽管触控板手势默认支持了，但响应程度并不如预期，特别是双指右键常常没相应。好在 [Wiki 上给出了微调的方式](https://wiki.pine64.org/wiki/Pinebook_Pro#X-Windows_.26_trackpad_settings)，在 KDE 环境下可以通过“系统设置” - “触摸板” 调整其 “最大时间” 参数实现。
* 网页浏览：预装的 Firefox 虽然版本紧跟发布，但由于 Panforst 的缘故并无法启用 WebRender，而强行启用会导致部分页面花屏的情况，所以虽然流畅，但是渲染速度**逊色**于相近价位上 X86 的 Linux 笔记本。另外角度，由于 Widevine DRM 模块没有预编译的 ARMv8 版本，部分需要此模块的在线视频站点会无法正常使用，但社区提供了一个 [Docker 当作临时措施](https://wiki.pine64.org/wiki/Pinebook_Pro#Watching_DRM_content_.28Netflix.2C_etc..29)部分解决。
* 中文支持：得益于 KDE 国际化的良好支持，系统已经预装了 noto 字体，不会有豆腐块的情况。但中文输入法的配置却不像 GNOME 环境下那么便捷。首先 Manjaro 没有像 Ubuntu 那样提供类似“Language Support”的图形化工具，一站式的搞定应用软件语言包、输入法框架和环境变量设置等配置，需要用户根据需求手动安装各个组建并配置。其次 KDE 环境下首推的 FCITX5 输入法框架在 Pinebook Pro 上候选字选择栏渲染花屏，这恐怕还是 Panfrost 的问题……最终，参照 [Arch IBus Wiki](https://wiki.archlinux.org/index.php/IBus) 上配置完成中文输入法。
* 硬件解码：尽管 SoC 不同，但这方面和 [Pine64 的状态类似](https://linuxtoy.org/archives/lightweight-portable-desktop-with-pine64.html)，内核部分的支持在最新的 5.9 中已经包含，但是对应用户态的库和应用软件的支持都还尚在进行中。于是现阶段视频解码工作只能依赖 CPU 部分软解码实现。这方面经过测试，1080P 24FPS/30FPS 的视频回放（例如 B 站的 1080P）没有问题，此时 CPU 占有率约 70%，更高码率的 1080P 60FPS （例如 B 站大会员的 1080P+ ）则会导致 CPU 占有率飙升至 80% 以上，出现高达 30% 丢帧的情况。这样的性能意味着大多数互联网视频和本地视频观看是不受影响的。同时得益于 ARM 本身较低的功耗和温控，续航时间颇有保证，笔者尝试了在 WiFi 5 网络下全屏播放 [B 站的 2020 Game Awards](https://www.bilibili.com/video/BV15z4y1C7nD)结束后仍有 68% 的余电，只可惜屏幕是在差强人意，否则外出刷剧还是不错的。
* Type-C 视频输出：很不幸，笔者手上仅有的两个 Type-C 至 HDMI 视频转换头（一个多功能复合型，一个单纯视频输出）连接 Pinebook Pro 后目前都无法获得视频输出。 这方面社区维护了一个这个[接口视频转换器的兼容列表](https://wiki.pine64.org/wiki/Pinebook_Pro_Hardware_Accessory_Compatibility#USB_C_alternate_mode_DP)纪录现在兼容的 Type-C 视频输出。相信随着后续 Kernel 版本的更新和 [Pine64 自己 Docking Station 的推出](https://www.youtube.com/channel/UCxQKHvKbmSzGMvUrVtJYnUA)，这个方面的状况近期应该就会得到改善。
* 无线模块相关：由于未知原因，[PineBook Pro 无法连接启用了 802.11r Fast Roaming 的无线热点](https://forum.pine64.org/showthread.php?tid=11960)，这个功能是 WiFi 5 协议中的标准扩展，在不少高端 Mesh 路由中或者 OpenWrt 固件都会启用，用来改善无线设备在共用相同 SSID 的多个路由间漫游时的丢包情况。考虑到这个问题也[出现在使用 Manjaro 的 Pinephone](https://forum.manjaro.org/t/pinephone-cannot-connect-to-wifi-networks-where-fast-roaming-ieee-802-11r-is-active/37968) 上，两者 SoC 并不相同，故笔者推测问题在软件或者内核问题，而非硬件本身。

#### Armbian Focal Xfce ####

出于偶然的机会，又将 [Armbian Focal Xfce](https://www.armbian.com/pinebook-pro/) 的 SD 卡插入 Pinebook Pro 引导了，这次重点尝试了在 Manjaro KDE 上不尽人意的地方，没想到有惊喜：

* Type-C 视频输出：和 Manjaro 问题倍出的状态不同，Armbian 的 Rockchip64 主线 5.9.14 内核对于 Type-C 视频输出良好，4K 和超宽屏都可以使用，且可同时利用 Type-C 坞站的 PD 充电功能，只可惜无法通过 HDMI 实现音频输出。
* 无线模块相关：Manjaro 上无法连接 802.11r 无线热点的奇葩问题在 Armbian 上并不存在，证实了之前为软件异常而非硬件缺陷的猜想。

#### 其他发行版 ####

随着 RK3399 在内核态的主线支持的完善，越来越多的发行版开始支持 Pinebook Pro。目前 [Debian](https://lists.debian.org/debian-devel-announce/2020/12/msg00001.html) 预期将在下个版本正式支持，而 [Fedora](https://ask.fedoraproject.org/t/fedora-33-for-pinebook-pro/9892) 也已经在路上了。

### 总结 ###

由于 Type-C 接口问题，这篇文章是在 X86 笔记本和 Pinebook Pro 上交替着完成的，但笔者外出时更乐于携带 Pinebook Pro 的倾向性足矣证明这款产品的市场定位还是有其价值的。如果您是一名 Linux 爱好者，目前在考虑以低于 ￥2500 的价位购入适用于出行使用的码字利器，那么 Pinebook Pro 绝对是一个比入门级 X86 笔记本甚至 Chrombook 更好的选择。回想一下，目前 Pinebook Pro 在软件体验上的不足，几乎是近 10 年前 Linux 桌面版在笔记本上使用时面临的类似问题，无一不都在接下来的几年里都被逐个解决了。而在当下这个可能是芯片产业指令集方面近半个世纪以来的转折期，Pinebook Pro 能以如此低廉的价格将 Linux 桌面的过去和可能的未来连接到一起，何尝不值得把玩呢？
