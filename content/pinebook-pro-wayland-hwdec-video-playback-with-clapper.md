Title: PineBook Pro 暨 Wayland 下使用 Clapper 实现硬件解码视频回放
Date: 2022-07-20 22:00
Category: Howto
Tags: manjaro, pine64, wayland
Slug: pinebook-pro-wayland-hwdec-video-playback-with-clapper
Authors: lovenemesis

去年花了[不少时间折腾的 Pinebook Pro](https://linuxtoy.org/archives/pinebook-pro-review.html) 凭借着还算趁手的键盘配合无风扇的轻量化设计特别适合外出的时候做些本地化工作。相比 Apple 今年挤牙膏式的 M2 升级，Pinebook Pro 的可用性在社区各个层面的开发者努力下有了不小的提升，其中之一就是**硬件加速的本地视频回放**。

硬件加速的视频回放是一个需要从内核层到应用层、解码库到播放器都逐步发展才能实现的功能，其中：

* 名为 [Hantro 的内核模块](https://wiki.pine64.org/wiki/Mainline_Hardware_Decoding#Hantro)暴露了 Rockchip R3399 VPU 硬件解码功能
* [GStreamer 的 V4L2 支持](https://gitlab.freedesktop.org/gstreamer/gst-plugins-bad/-/merge_requests/1141) 从而可以[处理 stateless 编解码器](https://www.kernel.org/doc/html/latest/userspace-api/media/v4l/dev-stateless-decoder.html)
* 播放器对于编解码器库的正确调用从而可以适配各类媒体及复杂的桌面环境，譬如 [Clapper](https://flathub.org/apps/details/com.github.rafostar.Clapper)。

[Clapper](https://flathub.org/apps/details/com.github.rafostar.Clapper) 是一款基于 GStreamer 的 GNOME 媒体播放器， 特别之处在于其使用全新的 GTK4 实现界面渲染并仅依赖 GL/EGL 完成视频输出 。此外它还具备以下特点：

* 支持 GStreamer [前瞻性的 playbin3 媒体调用接口](https://gstreamer.freedesktop.org/documentation/playback/playbin3.html?gi-language=c#playbin3-page)，支持实时流切换和高效的 zero-copy 视频渲染；
* 对于 A 卡和 I 卡默认使用 GStreamer [新的 VA-API 接口插件 va](https://gstreamer.freedesktop.org/documentation/va/index.html?gi-language=c)，可以实现 AV1 硬件解码回放，对于 N 卡默认使用[新的 nvdec 系列硬件解码插件](https://gstreamer.freedesktop.org/documentation/nvcodec/index.html?gi-language=c#plugin-nvcodec)
* 无标题栏的精简化设计，配合[扩展](https://extensions.gnome.org/extension/4691/pip-on-top/)实现 GNOME 桌面环境的常驻画中画模式
* 内建**部分流媒体站点 URI 解析功能**，经测试 YouTube 和 Bilibili 的非付费内容均可播放； 
* 支持在**移动设备 SoC 常见的 V4L2 的硬件加速接口**。

现在划重点了，下面就是目前来说最便捷的**在 Wayland 窗口管理协议下实现硬件加速视频回放**的步骤：

1. 通过 [Flathub 安装 Clapper](https://flathub.org/apps/details/com.github.rafostar.Clapper) 后，点击左上角菜单，进入“选项”/“Perference”；
2. 进入 “调整” /“Tweak”选项卡，开启实验性的 `playbin3` 支持；
3. 关闭并重启 Clapper，播放支持硬件加速的视频文件，点击播放进度条右侧的摄像机图标，检查所调用编码器；
4. 若 A 卡和 I 卡提示 va 开头解码器（例如 `vah264dec`） ，或 N 卡提示 nv 开头的解码器（例如 `nvh264dec`），或在 Pinebook Pro 上提示 v4l2 开头的解码器（例如 `v4l2slh264dec`），则代表硬件加速已正确启用。

是不是很简单？经过和另外两大开源媒体播放器（[VLC Media Player](https://www.videolan.org/vlc/) 和 [mpv](https://mpv.io/)）的对比，使用 Clapper 可谓是目前所需额外设置最少的能工作在 Wayland 窗口协议下的硬件加速视频回放方案。

硬件加速的视频回放在 Pinebook Pro 这类设备上的影响是巨大的。在开启硬件加速后，视频播放的时候 RK3399 两个 A72 的**大核负载几乎为 0%**，而同样视频的在先前使用软件解码回放时会使得两个大核长期保持 50% ~ 60% 的中度负载，这对于热量和电量的益处是显而易见的。此外，stateless 的 memory-to-memory 特性也使得内存需求大幅降低，现在亦可**流畅播放 4K H264 和 VP9 视频**。根据最新的消息，[Hantro 模块针对 H265/HEVC 的硬件加速和 H264 的硬件编码加速支持](https://www.phoronix.com/scan.php?page=news_item&px=RkVDEC-HEVC-Patches)也已提交内核邮件列表审阅了，Pinebook Pro 未来可期。