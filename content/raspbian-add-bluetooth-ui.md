Title: Raspbian 新版带来更好的蓝牙支持
Date: 2016-05-13 17:33:16
Authors: toy
Category: News
Tags: raspbian, rpi
Slug: raspbian-add-bluetooth-ui
Via: Raspbian|https://www.raspberrypi.org/blog/another-update-raspbian/

树莓派系统 Raspbian 已经发布了一个新版本，该版本补上了早先缺少的蓝牙配置界面支持。此界面以 lxpanel 任务栏插件的形式提供，利用它可以方便的添加各种蓝牙设备，包括蓝牙音箱和耳机。

<!-- PELICAN_END_SUMMARY -->

![bluetooth]({filename}/images/raspbian-bluetooth.png)

新版也提供名为 **SD Card Copier** 的工具用来将整个系统备份到别的 SD 卡上，并包含从 Python 访问 GPIO 接口的 pigpio 库和 Geany 文本编辑器。

此外，其内核已更新到 4.4，将 Scratch、Sonic Pi、Node-RED、BlueJ、PyPy 升级到了新版，以及包含其它一些细小的用户界面优化。

**升级**

```
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install piclone geany usb-modeswitch
```

**下载**

+ [Raspbian Full（带桌面）](https://downloads.raspberrypi.org/raspbian_latest)
+ [Raspbian Lite（简化版）](https://downloads.raspberrypi.org/raspbian_lite_latest)
