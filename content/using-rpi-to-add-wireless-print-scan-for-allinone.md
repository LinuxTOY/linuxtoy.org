Title: 入门级打印扫描一体机的飞升：借助树梅派实现无线打印扫描
Date: 2023-04-27 20:00
Category: Howto
Tags: cups, sane, raspberrypi
Slug: using-rpi-to-add-wireless-print-scan-for-allinone
Authors: lovenemesis

入门级别或者早年购买的扫描打印一体机通常只具备 USB 连接功能，很难满足当下无线办公环境下的多人共享需求。而市面上销售的无线打印盒子几乎都依赖第三方的云端服务实现基本的功能，安全及长期可靠性难以保障。
实际上，只需要借助空闲的树梅派甚至 [Vero 4K 机顶盒](https://linuxtoy.org/archives/osmc-vero-4k-review.html)，就可以为这些老旧的设备插上飞升的翅膀，拥抱无线办公/教学的浪潮。

接下来要描述的实现方案设计出发点为：

* 服务器端基于 Debian Linux / Raspberry Pi OS 的系统，长期可靠性有保证；
* 桌面操作系统客户端无需额外驱动安装，降低客户端接入复杂度；
* Android 客户端使用厂商中立的 [Mopria 系列应用](https://mopria.org/)；
* 远程功能限制到局域网内，避免不必要的信息外溢；

下面将以在 Raspberry Pi 3+ 上完成基本配置的 Debian 11 / Raspberry Pi OS 配合通过 USB 接口连接的 HP Deskjet 的入门打印一体机作为范例来介绍下配置过程。

## 打印服务器端配置 ##

[Internet Printing Protocol(IPP)](https://www.pwg.org/ipp/) 是拥有广泛终端和应用支持的网络打印协议，下来将配置 CUPS 打印服务程序把连接的打印机用该协议共享出来。

1. 安装打印机驱动及 [CUPS 打印服务进程](https://openprinting.github.io/cups/)：`sudo apt install hplip cups` ；
2. 允许默认的 `pi` 用户管理打印服务: `sudo usermod -aG lpadmin pi` ；
3. 开启并允许打印服务: `sudo systemctl enable --now cups` ；
4. 因为是局域网配置，所以可以允许远程管理: `sudo cupsctl --remote-any && sudo systemctl restart cups` ；
5. 最后，可以通过在浏览器以端口号 631 访问树梅派设备的 IP 来访问并配置打印机了，仅需要记得**勾选"共享这台打印机"**即可。过程简单直观，不再赘述。

经过这番配置之后，打印机会通过 IPP 协议在局域网内分享。

## 打印客户端配置 ##

### Linux 工作站 ###

常见的桌面 Linux 发行版都可以直接通过预装的 mDNS 找到网络中的 IPP 共享打印机，无需额外配置可以立即使用。

### Android 手机 ###

Android 手机自带的打印服务对于 IPP 的支持有限，建议前往 [Mopria 联盟官网下载 Mopria Print 应用](https://mopria.org/print-from-android)（提供 Play Store 和直接下载），稍后便可搜索并连接到共享打印机了。

### Windows PC ###

最新版本的 Win10 和 Win11 都可以直接连接并使用网络中的 IPP 共享打印机，亦无需安装驱动。

## 扫描服务器端配置 ##

虽说 Linux 环境下的 SANE 本身提供网络共享服务进程 `saned` ，但与其对应在 [Android 系统上的前端](https://play.google.com/store/apps/details?id=com.sane.droid)早已年久失修，无法在最新的 Android 13 权限下保存扫描结果。
于是这里转而使用 AirSane 通过跨平台兼容性更好的 AirScan 协议将扫描功能在局域网共享出来。

1. 由于软件相对较新，尚未被 Debian 11 收录，所以需要从 [AirSane Github 仓库](https://github.com/SimulPiscator/AirSane/releases)下载最新 Release 版本源代码进行编译，本文截稿时为 0.3.5 版本；
2. 之后安装必要的编译依赖环境：`sudo apt install libsane-dev sane-utils libjpeg-dev libpng-dev libavahi-client-dev avahi-daemon libusb-1.*-dev git cmake g++` ；
3. AirSane 使用 cmake 构建，遵循其常规解压并创建构建目录：`tar xf AirSane-0.3.5.tar.gz && mkdir AirSane-build && cd AirSane-build` ；
4. 构建编译依赖并开始编译，该软件体积小巧，哪怕在树梅派也仅需不到三分钟：`cmake ../AirSane-0.3.5 && make` ；
5. 在正式安装 AirSane 之前，需要确保扫描仪已经可以被 SANE 识别：`sudo scanimage -L` ；
6. 如上述结果无误，可以继续 AirSane 的安装并启用：`sudo make install && sudo systemctl enable --now airsaned` ；
7. 最后，可以通过在浏览器以端口号 8090 访问树梅派设备的 IP 来访问并检查扫描仪是否正常工作了。AirSane 默认的配置已经适用绝大多数场景，如需更多微调可以编辑 `/etc/airsane/options.conf` 文件实现。

## 扫描客户端配置 ##

### Linux 工作站 ###

常见的桌面 Linux 的 SANE 套间中已经包含了 `sane-airscan` 组件，但是默认使用的是 eSCL 协议后端，需要切换后端为 AirScan。

1. 使用顺手的文本编辑器打开 SANE 配置文件：`sudo vim /etc/sane.d/dll.conf`
2. 注释掉 `escl` 所在行的一行
3. 添加新行 `airscan`

之后在 Linux 工作站用 `sudo scanimage -L` 或者 [Simple Scan](https://gitlab.gnome.org/GNOME/simple-scan)程序便能发现局域网共享的扫描仪了。

### Android 手机 ###

前往 [Mopria 联盟官网下载 Mopria Scan 应用](https://mopria.org/scan-to-android)（提供 Play Store 和直接下载），稍后便可搜索并连接到共享扫描仪了。

### Windows PC ###

最新版本的 Win10 和 Win11 都可以直接连接并使用网络中的 AirScan 共享扫描仪，亦无需安装驱动。

## 绿色办公 ##

如果现有打印一体机工作正常的话，参照上述的方法利用已有硬件，配合开源软件即可扩展新的功能。
此举不仅避免了购买第三方打印盒子的开销，同时也避免了产生电子垃圾。
绿色办公，何乐而不为？
