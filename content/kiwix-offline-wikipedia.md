Title: Kiwix 离线维基百科阅读器
Date: 2022-04-06 18:00
Category: App
Tags: wikipedia
Slug: kiwix-offline-wikipedia
Authors: lovenemesis

Kiwix 是一款针对在没有网络的情况下查阅维基百科内容设计的阅读器，同时也可以阅读任何使用 Zim 存档的网站内容。经过简单的配置，也可以方便将其内容分享给局域网中的其他人。

<!-- PELICAN_END_SUMMARY -->

Zim 是构建于 [Web Recorder 项目愿景之上](https://webrecorder.net/faq)的网页存档格式，可将网站的全部内容整合并压缩为便于离线分享和存储的单一文件中。
Kiwix 项目使用该格式，将部分教育类资源站点保存下来，供没有网络或者网络不畅的社区或个人使用，实现知识的共享。其特点有：

* Zim 文件的阅读、检索和共享的时候无需生成临时文件，对于系统的负载也比较很小；
* 项目收集了多种语言的知名教育资源类内容，包括[维基百科](https://www.wikipedia.org/)、[古登堡计划](https://www.gutenberg.org/) 、[TED](https://www.ted.com/) 等；
* 维基百科类内容除了完整的内容包以外，还有依据学科题材分类单独下载，以及仅简介、详情但不包含图片的更小尺寸压缩包，适合于不同的需求；
* Kiwix 的开源免费阅读器覆盖了[常见的桌面操作系统和智能手机平台](https://www.kiwix.org/en/download/)；
* 亦可使用[浏览器插件或者 PWA 网站应用](https://www.kiwix.org/en/downloads/browser-extensions/) 阅读 Zim 文件；
* 提供了[生成 Raspberry Pi 专属镜像的工具](https://www.kiwix.org/en/documentation/how-to-set-up-kiwix-hotspot/)，方便创建预先灌装有内容且完成服务器、WiFi 热点等设置的 SD 卡；

### 搭建并配置 Kiwix-Serve ###

Kiwix 的桌面版阅读器都内建了服务器功能，可将当前正在加载的 Zim 生成一个本地站点，使得同一局域网内的用户可以直接使用浏览器访问而无需任何额外工具。Kiwix-Serve 则是将这一部分功能独立分发的服务器端工具，非常适合在学校或者家庭网络内供多人分享。这里简述其配置过程：

1. 首先从 Kiwix 网站上[下载 Kiwix-Serve 工具包](https://www.kiwix.org/en/downloads/kiwix-serve/)，这里以适用于 ARMv7 Linux 的版本为例。
2. 将其压缩包内的四个文件安装至系统目录，譬如 `sudo install -Z kiwix-* /usr/local/bin/`；
3. 使用 `kiwix-manage` 创建对应的资料库管理文件，譬如 `kiwix-manage library.xml add wikipedia_zh_all_maxi_2022-03.zim`；
4. 之后便可以使用 `kiwix-serve` 启动服务，譬如 `kiwix-serve --library library.xml --port 9000`，端口号这里使用了 9000，也可以换成其它的；
5. 然后在客户端的浏览器里就可以使用运行 `kiwix-serve` 的 IP 或者域名加端口号的方式浏览内容了，无需任何扩展或者阅读器。

如果需要设置成系统服务的话，这里提供一个 systemd unit 的模板作为参考：

```
[Unit]
Description=kiwix-serve Service
Wants=network-online.target
After=network.target

[Service]
Type=simple
Restart=on-failure
RestartSec=3
WorkingDirectory=/var/lib/kiwix/
ExecStart=/usr/local/bin/kiwix-serve --library /var/lib/kiwix/library.xml --port 9000
StandardOutput=journal
StandardError=null

# Hardening
DynamicUser=true
MemoryDenyWriteExecute=true
NoNewPrivileges=true

[Install]
WantedBy=multi-user.target
```

这里使用的一些 systemd 提供的安全强化措施，减少由于 `kiwix-serve` 本身潜在安全漏洞对于系统整体的影响。

[适用于各种 Linux 发行版的 Flatpak 安装包](https://flathub.org/apps/details/org.kiwix.desktop)
[适用于 Android 平台 APK 直接下载](https://download.kiwix.org/release/kiwix-android/kiwix.apk)（F-Droid 版本较老，无法用于新版 Android 系统）