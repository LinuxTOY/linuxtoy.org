Title: 跨平台 XMPP 即时聊天软件 Gajim 发布 1.4.1 版本
Date: 2022-05-25 11:40
Category: Apps
Tags: im, xmpp
Slug: gajim-141
Authors: lovenemesis

使用 PyGTK 开发的 XMPP 即时聊天软件 Gajim 迎来了全新设计的 1.4.X 系列，并过去的周末发布了第一个修订版本  1.4.1。

<!-- PELICAN_END_SUMMARY -->

Gajim 上一个稳定版本发布已经为 20201 年 10 月份的 1.3.3，而阔别已久的 1.4 系列引入大量的变化，其中非常明显的便是拥抱[工作区设计](https://gajim.org/post/2021-08-27-workspaces/)的主窗口：

 ![gajim 1.4 main window]({filename}/images/gajim-window-1-4.png)

除了用户交互体验方面的大量全新设计外，新版本还有下列变化：

* 完整支持 [XEP-0393](https://xmpp.org/extensions/xep-0393.html) 消息样式（包括输入框的实时样式设定）和 [XEP-0425](https://xmpp.org/extensions/xep-0425.html) 群聊消息审核；
* 移除不常用的 [XEP-0174](https://xmpp.org/extensions/xep-0174.html) Zeroconf 通讯、 [XEP-0107](https://xmpp.org/extensions/xep-0107.html)用户心情和[XEP-0108](https://xmpp.org/extensions/xep-0108.html) 用户活动 支持；
* 整合了图片预览、插件安装器、语法高亮和 AppIndicator 通知插件，无需另行安装；
* 调整了“给自己的笔记”的功能，方便给另一台设备上登录的自己发送消息；
* 切换至 Python 3.9，在使用更新的依赖库的同时结束对于 Win7 和 32 位系统的支持；
* 大量的 Bug 修复。

**PS** 由于新版本的大量变化，本地化工作也不出意外地近乎重头再来，笔者在过去一个月中对其 2K+ 的条目逐一进行了翻译或润色。但孤军奋战难免会有疏忽，如果在使用中遇到简中本地化的问题，欢迎联系我。

* [适用于 Win 和各个 Linux 发行版的官方下载](https://gajim.org/download/)
* [适用于 Linux 的 Flathub 下载](https://flathub.org/apps/details/org.gajim.Gajim)
