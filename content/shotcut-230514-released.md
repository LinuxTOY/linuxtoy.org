Title: 开源跨平台非线性视频编辑器 Shotcut 23.05.14 发布
Date: 2023-05-16 18:00
Category: App
Tags: shotcut, nle
Slug: shotcut-230514-released
Authors: lovenemesis

基于[开源非线性编辑媒体框架 MLT](https://www.mltframework.org/) 的 [Shotcut](https://www.shotcut.org/) 最近发布了 23.05.14 版本，包含了众多改进和新功能。
实际上该版本为问题修订版，修复了在 23.05.07 版本发布后不少社区反馈的包括[本地化语言缺失](https://forum.shotcut.org/t/missing-translated-message-in-23-05-07-ui/38755/4)在内的重大问题，更适合非英语母语用户团体使用。

整个 23.05 版本包含了众多改进，可谓是功能满满：

* 迁移至 Qt6 界面框架，意味着在 Win10+ 和 OS X 平台将分别使用性能更好的 DX11 和 Metal API 进行界面渲染任务；
* 现在 OS X 的安装包平台将统一支持 X86 和 ARM 指令集；
* 恢复长期停更的 **Linux ARM64 版本**，经笔者测试可在 [PineBook Pro](https://linuxtoy.org/archives/pinebook-pro-review.html) 上运行；
* 得益于界面不再依赖 OpenGL 渲染，重新引入了 **GPU 特效**，这些特效不仅性能更佳且**原生支持 10bit 色彩**。**注意**虽说可以在一个项目内混用 CPU 和 GPU 效果，但后期无法单独移除 GPU 特效且会回退到 8bit 色彩支持；
* 带来了备受期待的**动作追踪滤镜**，可以追踪视频中的一个元素，将其的运动变化和关键帧关联起来，配合其他诸如位置剪裁、文字等滤镜实现和动作相关联的剪辑效果；
* 带来了使用更佳便捷的“仅快进”和“快进和回退”滤镜，方便调整剪辑片段中部分段路的播放速度；
* 支持**设定“滤镜分组”**，方便保存和加载各种自己频繁使用的滤镜组合；
* 更新 MLT、ffmpeg、Glaxnimate 等依赖库至最新版本，带来诸如**大幅度改善的 AV1 视频编解码**支持，在 Win 平台甚至支持 Intel 的 10-bit AV1 及 VP9 硬件编码加速。

Linux X86/64/ARM64 Flatpak 下载：`flatpak install flathub org.shotcut.Shotcut`

[其他平台官方预编译安装包下载](https://shotcut.org/download/)

[官方发布公告](https://shotcut.org/blog/new-release-230507/)

**PS**: 如果尝试在 Pinebook Pro 或者 Raspberry Pi 4 上进行视频剪辑工作的话，不妨参考之前分享的[使用代理素材的技巧](https://linuxtoy.org/archives/proxy-editing-using-shotcut.html)改善流畅度。