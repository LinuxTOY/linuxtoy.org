Title: Linux Kernel 4.7 发布
Author: lovenemesis
Date: 2016-07-25 23:20:00
Category: Kernel
Tags: kernel
Slug: linux-kernel-4-7

Linux 4.7 正式版本发布，带来了包括 AMD RX480 显卡在内的一系列新硬件支持。

<!-- PELICAN_END_SUMMARY -->

![tux]({filename}/images/tux.png)

本次更新的亮点有：

* 包含 AMD RX480 GPU 的开源驱动支持，配合正在开发的 Mesa 12.1 即可使用
* 并行化的文件夹内容缓存查询
* 新的 `schedutil` 频率管理器，使用来自调度器的信息调整 CPU 频率，奠定根据负载调整主频的基石
* 为内核追溯增加分布频数图支持
* `perf` 支持追溯访问栈
* 允许创建包含整合性追踪点的特殊 BPD 应用
* 支持向 EFI 固件发送二进制文件，可以[实现在 Linux 下更新 UEFI 固件](https://blogs.intel.com/evangelists/2015/06/23/better-firmware-updates-in-linux-using-uefi-capsules/)
* 允许创建虚拟的 USB 控制器而无需任何物理 USB 设备，方便与 USB/IP 设备使用
* 来自 Android 的 “sync_file" 机制被认为足够稳定
* 新增 LoadPin 模块，可以用来校验所载入的内核模块、固件、kexec 镜像和安全策略是否源自同一文件系统
 
[详细更新日志](http://kernelnewbies.org/Linux_4.7)

[官方源代码下载](https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.7.tar.xz)

消息来源：[Phoronix](https://www.phoronix.com/scan.php?page=news_item&px=Linux-4.7-Released)



