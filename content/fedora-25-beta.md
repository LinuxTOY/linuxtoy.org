Title: Fedora 25 Beta
Author: 1dot75cm
Date: 2016-10-12 2:00:00
Category: Distro
Tags: fedora
Slug: fedora-25-beta

经过例行的延期，Fedora Project 宣布 Fedora 25 Beta 发布，也是首个默认使用 Wayland 的主流发行版。

<!-- PELICAN_END_SUMMARY -->

从 Get Fedora 网站下载预发布版本，并 [刻录 U 盘](https://fedoraproject.org/wiki/How_to_create_and_use_Live_USB/zh-cn) 进行安装：

- [获取 Fedora 25 Beta 工作站版](https://getfedora.org/en/workstation/prerelease/)
- [获取 Fedora 25 Beta 服务器版](https://getfedora.org/en/server/prerelease/)


寻找 Cloud 版本？请查看下面的 [Fedora Atomic](https://fedoramagazine.org/announcing-release-fedora-25-beta/#Fedora_Atomic) 部分。或选择其他版本：

- [获取 Fedora 25 Beta Spins](https://spins.fedoraproject.org/prerelease)
- [获取 Fedora 25 Beta Labs](https://labs.fedoraproject.org/prerelease)
- [获取 Fedora 25 Beta ARM](https://arm.fedoraproject.org/prerelease)

Fedora 的旅程不仅仅是用最新和最好的软件包来更新操作系统。同时，Fedora Project 也为许多不同平台带来了创新：Workstation, Server, Atomic 和各种 Spins 版本。协调许多工作组并不是一项简单的任务，而是对 Fedora 社区内的杰出人才和专业精神的证明。

在 Fedora 25 发布周期的 Beta 阶段，我们为用户带来了以下更新。


# Fedora-Wide Changes

Fedora 所有产品将包含以下更新：

- Docker 更新至 1.12
- 删除对弱加密证书（即 1024bit）的支持
- Node.js 更新至 6.x
- “Secondary architectures” 现在称为 “alternate architectures”
- **Rust**: Fedora 25 带来了 [Rust 编程语言的支持](https://fedoramagazine.org/rust-meets-fedora/)。Rust 是一个系统编程语言，其运行速度惊人，并能防止几乎所有崩溃，段错误和数据竞争。
- **Python**: 除了 Fedora 25 中包含的“标准” Python 版本（3.5和2.7），Python 程序员现在可以从软件源安装 Python 3.4, 3.3 和 2.6（以及已存在的 PyPy, PyPy3, Jython），用于帮助他们用多个 Python 版本运行测试用例。


# Fedora Workstation

Fedora 25 Beta 工作站版本将包含以下更新：

- **GNOME 3.22**: Fedora 25 将在预览版和正式版中使用 GNOME 3.22。有用的新特性包括，多文件重命名，重新设计的键盘设置工具，和其他 UI 方面的修改。详情请参考 [GNOME 3.22 发行注记](https://help.gnome.org/misc/release-notes/3.22/)。
- **新的 Fedora media writer**: 新的 Fedora Media Writer 工具可以帮助您下载最新的 Fedora 稳定版。它可以帮助您将镜像写入 USB 设备，您可以方便的在您的系统中安装 Fedora。如果您喜欢 Fedora，您可以直接在 Live 环境中安装 Fedora。Fedora Media Writer 支持 Windows, Mac OS, Linux。
- **默认使用 Wayland**
    - Wayland 是传统 X11 显示系统的替代品。Wayland 已经开发了好些年。虽然多数软件仍然会有一些 bug，不过我们相信它能作为默认显示系统，并适用于大多数用户。
    - 如果有必要，用户仍然可以选择旧的 X11 系统，以避免一些问题。
- **Software 工具增强了 Flatpak 支持**: Software 工具现在可以安装，更新和卸载 Flatpak 软件包。
- GNOME Shell 扩展现在不再检查与当前 Shell 版本的兼容性。最初需要兼容性检查，是因为早期 GNOME 接口变动频繁。现在这些接口已经趋于稳定，扩展通常都可以与新版本一同工作。任何问题都应该向扩展作者报告。


# Fedora Server

Fedora 25 Server 在该周期中也有一些有趣的新变化，特别是 Cockpit 工具：

- **SELinux 调试模块**: Cockpit 现在有一个类似于 Fedora Workstation 的 SELinux Troubleshooter 模块。
    - 如果遇到 SELinux 拒绝，将显示有关该问题的信息和解决该问题的建议。
    - 没有该模块，管理员必须注意到发生拒绝，并挖掘日志中的拒绝信息，并搜索解决方法。SELinux Troubleshooter 程序提供的信息可以清楚方便的从 Cockpit 中看到。
- **在系统面板显示主机 SSH keys**: 可以清楚的看到为连接到主机，向系统添加了哪些 SSH key。
- **包括对网络组，Docker 卷，和存储管理的支持，以及创建 systemd timer 单元**
- **支持多步 (包括双因素) 认证**


FreeIPA 认证管理系统也更新至 4.4：

- 拓扑管理：FreeIPA Web UI 现在可被用于可视化管理大型部署的拓扑结构
- DNS 站点：FreeIPA 的 DNS 管理现在支持位置相关的服务配置
- 子 CA 中心：FreeIPA 证书颁发机构（Certificate Authority）现在能创建从属 CA 中心，用于颁发特定范围的证书
- Kerberos Authentication Indicators: Kerberos KDC 现在在为账户发出认证指示时，考虑服务票据。这允许，例如，在获得 VPN 服务（通过 OpenConnect服务支持）的票据前，需要先获得 Kerberos 凭据，以此实现双因素认证。
- Web UI 使用客户端证书认证：现在可以将 FreeIPA Web UI 和 API 配置为使用客户端证书和智能卡进行认证。
- 活动目录集成改进：为企业环境添加了许多功能
    - FreeIPA 现在支持来自 Active Directory 的备用用户主体名和后缀，并允许 FreeIPA 用户具有 Kerberos 别名
    - Active Directory 用户现在可以直接通过命令行管理自己的信息，包括 SSH 公钥和证书
    - 在信任多个 Active Directory 林的情况下，FreeIPA 现在能够自动解决 DNS 名称空间路由冲突
- FreeIPA 框架已支持外部插件
- FreeIPA 的性能已针对大型环境进行优化


# Fedora Atomic

Fedora Atomic 包括适合创建虚拟机的基础镜像，用于创建部署容器的主机的 Fedora Atomic Host 镜像和 Docker 镜像。Fedora 在这方面有些令人兴奋的变化，我们在 Fedora 中构建了更多的云和容器部署工具，来创建一个梦幻般的开发平台。虽然 Fedora 25 Atomic Host 不是 Beta 版本的一部分，但是 Fedora Project 计划将 Fedora Atomic Host 改为基于 Fedora 25。

Fedora Atomic 主机镜像可访问以下链接下载：

- https://getfedora.org/atomic_qcow2_latest
- https://getfedora.org/atomic_raw_latest
- https://getfedora.org/atomic_vagrant_libvirt_latest
- https://getfedora.org/atomic_vagrant_virtualbox_latest

Fedora Atomic 会在主要版本发布后的两个星期内发布新版本。它非常容易更新，以适应快速开发支持最新的应用程序。它也可以作为桌面运行，以满足需要轻量级和可重新配置环境的用户的需求。

Fedora Atomic 仍然在活跃的开发，一旦稳定，它便可以允许普通的 Fedora 用户轻松地提供云服务。对于即将到来的新版本，我们非常欢迎用户的贡献和经验。

Fedora Atomic 将代替 Fedora Cloud 作为我们的三个版本之一。[Fedora Cloud Base 镜像](https://getfedora.org/en/cloud/prerelease/)将继续为那些希望在云环境中使用基于传统 rpm 环境的用户进行构建。


# Spins and More

Fedora Beta 中的其他变更。KDE 版本为音乐，视频和个人信息管理提供了新的包。Xfce 包括对终端，通知和电源管理的改进。Mate-Compiz 更新至Mate 1.16 并完全切换到 GTK+3 toolkit。

您现在就可以[下载并体验新的 Fedora 25 Beta 版本](https://getfedora.org/)！


# What is the Beta Release?

Beta 版本拥有完整的代码，并且与正式版本非常相似。Fedora 25 的正式版本预计将在 [11 月发布](https://fedoraproject.org/wiki/Releases/25/Schedule)。如果您下载并试用测试版，您可以检查并确保所有您用到的功能都可以正常工作。您发现和报告的每个 Bug 都可以提高全球数百万 Fedora 用户的体验！我们有一个协调新功能和尽可能多地向上游提交补丁的文化，您的反馈不仅改进了 Fedora，而且还促进了 Linux 和开源社区的发展。


# Issues and Details

由于这是一个 Beta 版本，您可能会遇到错误或缺少的功能。要报告测试期间遇到的问题，请通过邮件列表或 Freenode 上的 ＃fedora-qa 与 Fedora QA 团队联系。随着测试的进行，您可以在 [Common F25 Bugs 页面](https://fedoraproject.org/wiki/Common_F25_bugs) 上查看常见问题。

关于报告错误的提示，请阅读[如何提交错误报告](https://fedoraproject.org/wiki/How_to_file_a_bug_report)。

稿源：https://fedoramagazine.org/announcing-release-fedora-25-beta/

-EOF-
