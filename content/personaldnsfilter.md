Title: 跨平台加密 DNS 和广告过滤 personalDNSfilter
Date: 2022-01-13 22:00
Category: network
Tags: dns, android, privacy
Slug: personaldnsfilter
Authors: lovenemesis

作为从互联网诞生之初便存在的域名解析服务 DNS，在现在日益险峻的网络环境下面临各种挑战。于是激发了多个平台上的各种实现，尝试在各自的领域解决相关的问题，但这也无形中对于普通用户和网络管理员增加了学习成本和维护难度。personalDNSfilter 是一款轻量级的跨平台 DNS 过滤代理，可以使用一套配置满足横跨 Android 移动端、桌面 Win 和 Linux 平台的安全 DNS 需求，且支持远程控制。

<!-- PELICAN_END_SUMMARY -->

personalDNSfilter 的特点有：

* 通过 Java(OpenJDK) 实现的完整加密 DNS 支持，包括 [DoH](https://en.wikipedia.org/wiki/DNS_over_HTTPS) 和 [DoT](https://en.wikipedia.org/wiki/DNS_over_TLS)，IPv4 和 IPv6；
* 支持大多数现有的广告、恶意软件和行为追踪过滤列表，支持定期更新和规则自动去重，**过滤操作完全本地完成**；
* Android 版本支持以 VPN 方式，无需 root 权限；
* 支持应用和域名白名单操作；
* 桌面版本不仅可用作本地域名解析，亦可配置接受局域网其他设备的请求；
* 支持**通过 Android 远程配置和检索桌面版本**；
* 一套**配置文件通用于移动端和桌面端**；
* 默认开启 CNAME 隐藏保护，破解使用 CNAME 伪装的跨站点追踪行为；
* 基于 GPLv2 发布的[开源软件](https://github.com/IngoZenz/personaldnsfilter)，其 [Android 版本亦发布在 F-Droid](https://f-droid.org/en/packages/dnsfilter.android/) 上。
* 轻量级设计，哪怕上百万条过滤规则内存占用也仅有数 MB。

经过笔者一段时间的使用，相比其他针对 DNS 相关问题的应对方案，personalDNSfilter 不仅弥补了 `systemd-resolved` 不支持 DoH 的缺陷，同时规避了使用私人 DNS 执行过滤的隐私泄漏风险；且一套方案无论是居家办公还是出门在外都适用，维护起来方便不少。遂在此分享一些配置和使用方面的经验，以期有所帮助。

### 手机 Android 版本配置 ###

这款软件的界面设计实属清奇，虽然已有完整的中文本地化，但还是强烈建议仔细阅读下[官方帮助文档](https://www.zenz-solutions.de/help/)。

其 Android 版本适配性还算凑合，笔者尝试了只有 1GB RAM 的初代 Fire 7 平板，亦能流畅使用。Android TV 也能用，但是需要外接鼠标键盘操作，不支持遥控器。

如果深度定制的 Android 系统有类似后台节电功能的话，请不要忘了将其加入白名单，并**在 VPN 设置中将其设定为“始终开启的 VPN”**市保护常在。

### 桌面 Linux 版本配置 ###

在[官方的完整安装包](https://www.zenz-solutions.de/?smd_process_download=1&download_id=67)中提供了适用于 Win 系统的配置脚本，但缺乏针对 Linux 平台的。笔者据此撰写了一套适用于基于 bash 和 systemd 的 Linux 系统配置脚本，已经提交上游，将会在后续版本随完整安装包发布。现阶段可以[从 Issue 下载附件使用](https://github.com/IngoZenz/personaldnsfilter/issues/190)。

如果已经配置好了 Android 版本的话，可以将其 `dnsfilter.conf` 文件复制到完整安装包解压后的文件夹中直接使用，非常的方便。

### 手机远程配置和管理 ###

personalDNSfilter 的手机端还支持远程控制桌面端版本，只需要在桌面版本的 `dnsfilter.conf` 中配置好 `server_remote_ctrl_keyphrase` 密码，之后在手机 Android 版本就能随时切换至远程桌面版进程，进行配置和使用情况监控了。

这一点比诸如 [Pi-Hole](https://pi-hole.net/) 和 [Adblock](https://openwrt.org/docs/guide-user/services/ad-blocking) 的方案在实际中着实好用不少。

### 局域网旁路 DNS 配置 ###

如果希望安装和配置了 personalDNSfilter 的设备也为局域网的其他设备提供加密 DNS 和隐私保护功能，那么可以在`dnsfilter.conf` 中将 `dnsProxyOnlyLocalRequests` 选项设置为 `false`，之后再在对应设备网络设置中的 DNS 指向到运行 personalDNSfilter 的设备即可。

或者更直接一些，将路由器的首选 DNS 指向运行 personalDNSfilter 的设备，这样局域网内所有设备的 DNS 都会转交由它处理，这种方式特别适合 IoT 等不支持配置网络详情的设备。

[官方网站](https://www.zenz-solutions.de/personaldnsfilter-wp/)

[包含桌面版本的完整安装包下载](https://www.zenz-solutions.de/?smd_process_download=1&download_id=67)