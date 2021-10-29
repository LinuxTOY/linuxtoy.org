Title: 跨平台开源待办事项和笔记 OpenTodoList
Date: 2021-10-29 15:00
Category: App
Tags: qt, todo, android, nextcloud, webdav
Slug: opentodolist
Authors: lovenemesis

待办事项和笔记管理软件各式各样，但能真正做到开源且全平台制霸的还真没几个，如果您也是位注重安全和隐私的多平台用户的话，不妨尝试一下 OpenTodoList。

<!-- PELICAN_END_SUMMARY -->

相比同类产品，基于 [Qt 技术](https://www.qt.io/) 的 OpenTodoList 有如下几点与众不同之处：

* 一套代码实现的跨平台支持，无论是桌面版还是智能手机端，操作体验都是类似的
* 融合了待办事项和 Markdown 笔记管理，且内容可以互相转换
* 除了支持跨平台网络同步以外，也支持**完全离线的本地存储模式**
* 内建 NextCloud 和 ownCloud 同步支持，并**不依赖对应客户端或者第三方辅助同步工具**
* 支持基于**通用的 WebDAV 存储**，意味着可复用现有邮箱或者网盘提供的存储空间
* 开放式的资料库管理结构允许使用第三方工具进行同步管理

经过一段时间的使用，虽然 Qt 在 Android 平台上有一些小问题，比如没有接入 SAF 和默认字体大小，但总体上来说还是一款可圈可点的好应用，值得推荐。

### PS ###

笔者已为其补完其简体中文本地化的工作，不出意外将在包含在下个版本中。

[Linux Flathub 下载（支持 X86 及 ARM）](https://flathub.org/apps/details/net.rpdev.OpenTodoList)

[Win 及 OSX 桌面版 GitHub 下载](https://github.com/mhoeher/opentodolist/releases)

[Android Play Store 下载](https://play.google.com/store/apps/details?id=net.rpdev.opentodolist)

[Android IzzyOnDroid on F-Droid 下载](https://apt.izzysoft.de/fdroid/index/apk/net.rpdev.opentodolist)

[iOS App Store 下载](https://apps.apple.com/cn/app/opentodolist/id1490013766?l=en)

[项目主页及源代码](https://opentodolist.rpdev.net/)