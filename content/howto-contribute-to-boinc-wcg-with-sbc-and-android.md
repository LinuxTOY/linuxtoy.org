Title: 在 SBC 和 Android 上使用 BOINC 参与 WCG 分布式计算
Date: 2020-09-01 22:43
Category: Howto
Tags: android, armbian, pine64, raspberrypi
Slug: howto-contribute-to-boinc-wcg-with-sbc-and-android
Authors: lovenemesis

现在谁也无法否定 COVID-19 将在短暂的人类历史上留下深刻的印象，无论以何种形式。如果截至目前为止人类社会面对这劫难及其后续各类事件的反应仍让你觉得希望尚存，且生活允许些许折腾，不妨跟着本文将了解如何让低功耗的单片机和常见的 Android 设备加入到 World Community Grid 分布式计算的全球网络中，成为为物种续命的千万个志愿者中的一员。

<!-- PELICAN_END_SUMMARY -->

### BOINC 和 World Community Grid ###

BOINC 由是美国加州大学伯克利分校的主导的高吞吐量计算平台，依据 LGPL3 分发，其上运行了多个分布式计算项目，包括早年大名鼎鼎寻找外星生命迹象的 [SETI@Home](https://setiathome.berkeley.edu/) 在内的 [30 余个项目](https://boinc.berkeley.edu/projects.php)，覆盖了物理、天文、数学、医疗、环境科学等多个方面。本文以其中专注于生命科学和环境科学的 [IBM Wordld Communit Grid 项目](https://www.worldcommunitygrid.org/) （下文简称 WCG）作为代表说明。

简单的将 WCG 与其他专注于生命科学的分布式计算项目诸如 [Folding@Home](https://foldingathome.org/)相比，有如下不同：

* WCG 上有一半的项目[支持在 ARMv7 SBC 和 Android 的设备上运行](https://www.worldcommunitygrid.org/help/viewTopic.do?shortName=minimumreq#251)，相比下 [Folding@Home 于 2017 年左右停止了其 Android 平台的支持](https://github.com/FoldingAtHome/FAHAndroid)。
* Folding@Home 最近又尝试恢复 ARM 架构的支持，但截止本文撰写时[仅有支持 ARMv8 SBC 的 Beta 版本](https://foldingathome.org/beta/)，不支持 ARMv7 的 SBC （包括当下用于 Raspberry Pi 3/4 的 Raspberry Pi OS）和 Android 设备。
* BOINC 和 WCG 原则上[支持使用 GPU（OpenCL）参与计算](https://www.worldcommunitygrid.org/help/viewTopic.do?shortName=GPU)，但目前 WCG 正在运行的项目并没有适用于 GPU 的计算单元。不过其他运行于 BOINC 上的项目比如 [Einstein@home](https://einsteinathome.org/)倒是有适用于 GPU 的项目。相比之下 Folding@Home 对于 GPU 计算的支持程度较好，有 OpenCL 和 CUDA 两种方式。
* 或许是得益于 BOINC 平台的设计，在参与 WCG 分布式计算的过程中，很容易获知当前运行的计算单元和项目的进度和意义，也可以轻松的选择想要重点贡献的项目。相对之下 Folding@Home 的界面设计很难得知在以一串数字为代表的当前计算任务究竟是干什么的，调配优先级也比较麻烦。
* 由于 WCG 所依托的 BOINC 为开源项目（注意 WCG 及其上的项目并非如此），已被收录在众多发行版仓库中，安装和配置都比较方便。Folding@Home 由于[各种原因并非开源](https://foldingathome.org/support/faq/opensource/)，安装和配置需要稍微麻烦一些。
* WCG 拥有非常直观的 Web 端配置管理系统，非常容易批量性的设置配置及部署。

### BOINC 和 WCG 在 Raspberry Pi 上的安装配置 ###

由于已被 Raspbian 仓库收录，安装非常简单：

`sudo apt update`

图形界面使用方法与桌面 Linux 发行版及其他平台无异，不再赘述。下来主要说明下 Headless 命令行的配置

`sudo apt install -y boinc-client`

在安装完成后 boinc-client 会默认以 systemd 的方式运行且设置为开机自启动。命令行的访问和配置都使用 [boinccmd](https://boinc.berkeley.edu/wiki/Boinccmd_tool) 这个工具完成。和通过 GUI 的方式不同，命令行版需要使用一个名为 "account_key" 的关联，而非直接用在 WCG 网站上注册的用户名和密码。

`boinccmd --lookup_account https://www.worldcommunitygrid.org/ <your_wcg_email> <your_wcg_password>`

之后会获得一串访问代码暨 "account_key"，记录下来以便下一步使用。

`boinccmd --project_attach https://www.worldcommunitygrid.org/ <your_wcg_account_key>`

至此初步的配置即可，接下来设备会开始向远程服务器请求并下载计算单元执行。这个命令行工具也可以做一些简单的查询：

`boinccmd --get_state`

上述这个命令可以相当全面的告诉 BOINC 的执行状态，以下为一些比较关键的字段：

* 计算应用的名称、版本和架构 `filename: wcgrid_opn1_autodock_7.17_arm-unknown-linux-gnueabihf`
* 当前运行应用的计算力评估 `estimated GFLOPS: 0.45`
* 任务汇报截止时间，晚于此将无法获得积分 `report deadline: Sat Sep  5 05:48:07 2020`
* 当前任务状态 `active_task_state: EXECUTING`
* 完成度，达到 1 代表该任务完成 `fraction done: 0.565084`

在默认配置条件下，BOINC 会利用全部可用的 CPU 进行计算，在其他非 BOINC 任务 CPU 负载超过 25% 时暂停任务。这样的负载在使用铜片被动散热 Raspberry Pi 3 Model B+ 会让 SoC 温度在 72 摄氏度居高不下，相当烫手。此外长时间运行后会观察到 SWAP 的使用，可见 1GB 的内存的确有些捉襟见肘。

### BOINC 和 WCG 在 Pine64 上的安装配置 ###

由于上述的情况，很自然的考虑迁移到性能更佳的 ARMv8 SBC 上运行。很遗憾的是，目前 WCG 的计算项目对于 ARM 架构的支持局限在 ARMv7 上，像 Pine64 等具备更大内存和 ARMv8 SoC 的 SBC 若要投入 WCG 的计算，除了按照上述 Raspberry Pi OS 的进行配置之外，还要额外声明 ARMv7 的运行时支持。这点在[专为 SBC 打造的 armbian 发行版](https://www.armbian.com/)上可以通过如下命令实现：

* 为包管理器添加额外架构 `sudo dpkg --add-architecture armhf`
* 安装 ARMv7 的 C 运行库 `sudo apt update && sudo apt install libc6:armhf libstdc++6:armhf`
* 添加动态链接库的符号连接 `cd /lib && sudo ln -vs arm-linux-gnueabihf/ld-2.23.so ld-linux.so.3`

之后使用任意顺手的文本编辑器打开 [/etc/boinc-client/cc_config.xml](https://boinc.berkeley.edu/wiki/Client_configuration#Options) 后，增加如下字段允许接受 ARMv7 架构的任务：

`<options>
       <alt_platform>arm-unknown-linux-gnueabihf</alt_platform>
 </options>`

之后重启下 boinc-client 服务即可接收到分派的计算任务了。

`sudo systemctl restart boinc-client`

相比 Raspberry Pi 3 Model B+，使用 [armbian 主线 Kernel 5.7.X 的 Pine64+](https://www.armbian.com/pine64/) 在参与 BOINC WCG 分布计算时环保不少，在提供相近的计算力的条件下功耗仅需 2.5W，满载 SoC 温度也仅有 60 摄氏度，此外 2GB 内存的充裕配置就算长时间运行也没有遇到使用 SWAP 的情况。

若是在 [Raspberri Pi 3+ 使用 Fedora ARMv8 版本](https://fedoramagazine.org/install-fedora-on-a-raspberry-pi/)的话，在参照其[桌面版的说明进行配置](https://fedoraproject.org/wiki/Installing_and_running_BOINC_client_in_Fedora_21)之后，亦需要参照这段增加 ARMv7 的支持。

另外 BOINC 还提供一个基于 ncurses 的命令行下的图形管理器 `boinctui`，使用了一段时间之后感觉功能有限且快捷键仍需单独熟悉，感兴趣的可以尝试下，不再赘述。

### BOINC 和 WCG 在 Android 手机和 Android TV 上的安装配置 ###

从某种角度来说，Android 设备在安装 [Termux](https://linuxtoy.org/archives/termux-032.html)之后亦可以参照上述 Debian 的方式从 Termux 软件仓库安装 `boinc-client` 使用，不过这里还是推荐使用 BOINC 为 Android 特别打造的版本，有更多便利性的功能。

其在 Play Store 的稳定版本相当古老的，推荐从其[官网下载](https://boinc.berkeley.edu/download_all.php)较新的版本，支持更多从 WCG Web 推送的配置项目。安装过程一如既往，稍后使用网站上注册的邮箱和密码即可关联 WCG，非常简单。
该版应用虽没有为 Android TV 做定制，不过在给 Android TV 接上无线鼠标后，还是可以很容易的完成配置过程的。

尽管 Android 的安装过程波澜不惊，但其使用的配置还是有不少与桌面版不同需要值得注意的地方：

* 默认情况下，Android 版本仅会使用检测到 CPU 核心数的一半来进行计算，比如 8 核 SoC 仅会启用其中 4 核参与。这在使用 bigLITTLE 配置多核的 ARM SoC 上其实是相当合理的，若是盲目在设置中更改为最大核心数，反而会由于温度和内存的限制降低有效计算力。
* 默认情况下，Android 版本仅会在充电且电量达到 90% 时开始计算，并不使用电池的电量消耗，避免对电池的损耗和过热。若手机系统提供了诸如电池保养的功能且散热设计良好的话，可以放心将起始百分比适当降低，提早在夜间充电时候开始计算的时间，间接提高贡献度。
* 在 Android 9+ 版本中，为了使得其在夜间充电的时候自动开始计算，需要禁用系统对其的省电策略：1) 将其添加为省电功能的例外项；2)不限制其在后台运行；3）加入系统或者第三方的内存优化应用的白名单。由于其应用受上述自身运行条件限制，哪怕在 BOINC 管理器在后台长期运行，对于白天的日常使用也完全不会造成任何影响，电量消耗 0%，内存占用 7M。[官网 Wiki ](https://boinc.berkeley.edu/wiki/Android_FAQ)上提出的另外一套在夜间采用屏保实现一直亮屏从而保证不被系统杀死的方案，对于 OLED 屏幕会带来明显损伤，且屏幕本来就是耗电产热大户，总体弊大于利，不建议采用。
* 对于 Android 机顶盒或者 Android TV 上来说，由于本来就是为长时间开机设计的，其散热和供电完全不是问题。但考虑到电视的 SoC 远不如手机且部分电视端应用资源占用惊人，建议将在设置中调整为亮屏时停止计算，这样分布式计算仅在息屏即不使用电视的时候进行，完全消除对日常使用的影响。

性能方面，经过这段时间的测试，新一代处理器的效能还是惊人的。手上采用 Snapdragon 855 SoC 的手机仅是夜间进行计算，其完成提交的任务数已经超过了同期 24 小时不间断工作的 Pine64+ 和 MediaTek 4 核 SoC Android TV 提交任务数之和。

值得提醒的时，除了 Android TV 这类既没有内置电池且本来为长时间运行的设备之外，不建议使用旧的手机或者平板长时间插电进行分布时计算。一来这些设备采用的老制成工艺的 SoC 和有限的内存会限制其性能的发挥，二来通常手机 ROM 不具备禁止电池充电的功能，而锂电池长时间处于充电状态，哪怕是涓流，也存在过热、鼓胀等安全隐患，理应避免。

### 总结 ###

至此分享了笔者在不到一个月里时间里对于参与公益性质分布式计算的一些体会和心得，并未竭尽一切设备不间断投入，也不为提交任务时积分猛涨的满足感，只是灵活利用了之前忽略了的闲置计算资源，为这个物种的存亡尽上自己微薄的一份力量而已。如果您也有类似想法，不妨一试

### 参考资料 ###

* [Pi MyLife Up](https://pimylifeup.com/raspberry-pi-boinc/)

