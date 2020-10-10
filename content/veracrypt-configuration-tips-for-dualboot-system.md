Title: 双引导系统下的 VeraCrypt 配置
Date: 2020-10-10 21:22
Category: Howto
Tags: grub, veracrypt
Slug: veracrypt-configuration-tips-for-dualboot-system
Authors: lovenemesis

对于笔记本电脑这种时常会携带外出的电子设备，基本的安全考量是必不可少的，而应用全盘加密（Full Disk Encryption）便是其中一个避免个人资料泄漏的重要措施。本文将简述如何在 Win Linux 双引导系统下使用 VeraCrypt 的配置技巧。

<!-- PELICAN_END_SUMMARY -->

## 注意事项 ##

[开源的 VeraCrypt](https://www.veracrypt.fr/en/Home.html) 继承自 TrueCrypt ，支持 Win、OSX、Linux 和 FreeBSD 系统，且包含适用于 Raspberry Pi 的 ARMv7 版本。本文以常见的 Win 和 Linux 双引导系统配置为例说明，但其思路同然适用于其他多系统共存时的组合。
由于当前所有主流 Linux 发行版配置的 GRUB2 引导器并不支持从 VeraCrypt 加密的根分区上引导系统，且主流 Linux 发行版都推荐使用 Linux 系统分区将使用 LUKS dm-crypt 的加密框架实现全盘加密方案，所以 VeraCrypt 将仅用于 Win 系统分区以及共享数据分区的加密。

另本文着眼于场景和目的为“普通民众在设备遗失的情况下避免未授权的第三方对于私人数据的访问”，不涉及 VeraCrypt 包含的为其他场景设计的高级功能。

## VeraCrypt 与 BitLocker 比较 ##

Win 系统本身提供了 BitLocker 的加密方案，和第三方提供的 VeraCrypt 有和不同呢？

* BitLocker 源码封闭，且没有经过独立的第三方审计；而 VeraCrypt 源码开放，且经过独立的第三方审计，个人认为这点安全软件来说加分不少。
* 在使用 BitLocker 加密的 Win 系统分区后，分区表结构会发生改变多出来一个分区；而使用 VeraCrypt 加密 Win 系统分区则不会有此问题。
* BitLocker 在双引导系统使用过程会时不时会由于 UEFI 配置变更甚至 Linux 内核更新的缘故进入救援模式，十分不便；而 VeraCrypt 使用的链式引导策略则不会有此问题。
* 在 Linux 下虽有用于[访问 BitLocker 分区的 Dislocker 工具](https://github.com/Aorimn/dislocker/releases)，但该工具目前开发已经近乎停滞，上个正式版本已为 2017 年，缺少对于 NTFS 和 exFAT 的 BitLocker To Go 的支持。
* BitLocker 仅支持 Win 常用的 NTFS 和 FAT 系文件系统；而 VeraCrypt 不仅支持 Win 系统上的 NTFS 和 exFAT 格式，且支持 Linux 上的 Ext 系列甚至较新的 Btrfs 文件系统。
* BitLocker 支持使用 TPM 实现启动前系统完整性校验；VeraCrypt 则认为这[与其设计预期不符，不会实现](https://www.veracrypt.fr/en/FAQ.html) （笔者此方面学识尚浅，不足以过多评价）。
* BitLocker 默认在启用 TPM 后不使用启动前密码验证，且仅允许专业版本启用该功能，这[在理论上开启了利用 DMA 漏洞访问数据的可能性](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-countermeasures)（实际中操作前提较难满足，但并非不可能）；相比下 VeraCrypt 则允许在为包括家庭版本内的任意的 Win 上为系统分区开启启动前密码验证；
* 除了整个设备的加密，VeraCrypt 还支持创建加密容器文件，在灵活性和通用性上更胜一筹。

## 使用 VeraCrypt 加密 Win 系统分区 ##

值得提醒的是搜索引擎中相关主题结果排名靠前的教程、提问和视频中的情况多为三四年前的状况，其中结论已经不再能反映当下情况了。VeraCrypt 近些年来增加了对于 Secure Boot 和 UEFI 的支持，对于近期的设备来说进行多系统引导的支持已经不是问题了。经过笔者几日来使用虚拟机和物理机多次实践，下面为加密 Win 系统分区时所需要注意的配置要求。

### 在 UEFI 系统上的推荐步骤 ###

* 如果使用 UEFI 配合 GPT 分区表的磁盘，**推荐优先安装 Win 系统，然后再安装 Linux 系统**，这般 GRUB2 可以通过 os-probe 自动查找到早先已经安装好的 Win 系统并添加对应的选项到 GRUB 启动菜单中；
* 在安装完 Linux 系统重启后，通过 GRUB2 启动菜单再次进入 Win 系统，完成驱动和安全更新等安装后，再下载并安装 VeraCrypt；
* 运行 VeraCrypt，从工具中即可选择为系统分区加密，进入向导界面；
* 在系统分区加密的向导过程中，非常重要的一步是**在询问”操作系统数目“时选择“多重启动”**，如下图所示：

 ![VeraCrypt Dualboot configure]({filename}/images/veracrypt-dualboot-configure.png)

* 在向导最后 VeraCrypt 会重启计算机，此时继续在 GRUB2 菜单中选择 Win 系统，输入在过程中创建的密码，进入 Win 系统开始真正的系统文件加密过程。取决于选择的加密、哈希和擦除方式以及分区大小，所用时间从半小时到几个小时都有可能，耐心等待完成即可。并不复杂，对吧？接下来如果有需要共享数据的分区的话，也可以采取类似的步骤使用向导将其加密，不再赘述。

### 在 UEFI 系统上修复引导错误 ###

如果在上述系统分区加密向导过程中，在"操作系统数目"步骤参考了网上视频教程选择了“单系统”的话，在重启之后将无法使用 GRUB2 启动菜单的 Win 项目正确进入系统。究其原因，是 VeraCrypt 安装的 EFI 启动器以单系统下“先 VeraCrypt 后 Win 启动器”的方式配置。于是这里需要为 GRUB2 创建指向 VeraCrypt 启动器的条目。由于 os-probe 并不能正确识别加密的 Win 分区和 VeraCrypt 启动器，这个步骤需要手动完成：

* 打开 `/boot/efi` 分区中的 `grub.cfg` 文件，找到关于 Win 引导字段的写法，如在 Fedora 系统这个是 `/boot/efi/EFI/fedora/grub.cfg` 文件中的以 `### BEGIN /etc/grub.d/30_os-prober ###` 开头的部分；
* 编辑 `/etc/grub.d/40_custom` 文件，参考以上 Win 引导字段的内容，但将其中 chainloader 部分修改为指向 VeraCrypt 启动器： `chainloader /EFI/VeraCrypt/DcsBoot.efi` ；
* 为了便于区分，可以将标题部分也稍微修改下，和原始的 Win 的区分，通过编辑 `menuentry` 实现，随自己喜好；
* 之后使用 `grub2-mkconfig -o /boot/efi/EFI/fedora/grub.cfg` 重新生成 UEFI 分区下的 GRUB 配置文件。

之后重新启动后，便可在 GRUB 菜单中看到新近添加的条目，选择其将先启动 VeraCrypt 启动器，输入密码后再引导 Win 系统开机。

## 在 Linux 系统下自动挂载 VeraCrypt 加密分区 ##

无论是使用 VeraCrypt 加密的 Win 系统分区还是共享数据分区，都可以通过 Linux 下的 VeraCrypt 客户端进行在登录系统后进行手动挂载。如果有需要的话，也可以配置自动挂载以方便使用。经过多次实践，有两种方式可以实现。

### 使用 cryptsetup 和 fstab 进行自动挂载 ###

在 cryptsetup 1.6.7 之后的版本增添了对于 VeraCrypt 格式的加密分区的有限支持，对于常用的单次 AES 加密和 SHA 哈希算法支持良好。这意味着可以复用 Linux 原生的 LUKS 跨架实现自动挂载，这里带来的便利是若 VeraCrypt 加密分区与 Linux LUKS 加密分区使用同样的密码，无需在启动时二次输入。

* 首先使用 `blkid` 找到 VeraCrypt 加密分区的 UUID，记录下来；
* 根据 crypttab man 列举的格式，编辑 `/etc/crypttab` 文件添加上述记录的 UUID 分区，注意在 `option` 字段附上这些参数以识别 VeraCrypt 格式的加密分区：`tcrypt-veracrypt`；
* 密码字段既可以指向一个仅包括的纯文本文件，或者写入 `none` 以便启动时输入；
* 如果要挂载的 VeraCrypt 加密分区同样也是系统分区的话，在 `option` 字段需要再加上这个参数：`tcrypt-system`；
* 接下来便可以根据 fstab man 列举的格式，编辑 `/etc/fstab` 挂载即可，唯一差别仅仅是使用在 `/etc/crypttab` 中定义的 `/dev/mapper` 作为挂载设备，而非原始的 UUID。

由于 systemd 已经包含了针对 fstab 的自动生成器，无需像部分网上教程再额外为此声明。

### 使用 VeraCrypt 客户端文本模式和 systemd 进行自动挂载 ###

如果使用非 cryptsetup 支持的加密或者哈希算法，或者使用了层叠式加密的话，启动时自动挂载便只能使用 VeraCrypt 客户端的文本非交互模式实现了。为了达到该目的，需要利用的 VeraCrypt 命令行参数有：

* `-t` 开启文本模式
* `--non-interactive` 开启非交互式模式
* `-k ""` 密钥文件位置，若是没有的话也需要传入空字符串
* `--pim=0`PIM数值，创建时如未特殊指定的话用 `0` 代表默认值
* `-p [PASSWORD]` 明文密码
* `-m [OPTION]` 加密分区挂载参数，如加密分区为系统分区的话需要指定 `system`
* `--fs-options=[FS_OPTIONS]` 挂载文件系统参数，fstab 里的参数列的内容都可以填写到这里
* `--mount [BLOCK_DEVICE]` 挂载设备
* `[MOUNT_POINT]` 挂载点，任意目录都行

组织好 `veracrypt` 的参数后只需要将其以任意方式在开机时执行即可，最简单的方式是利用 systemd 的 SystemV 的兼容模式，创建 `/etc/rc.d/rc.local` 文件并放入其中，这样借助 systemd 自动生成器的帮助它会在所有启动项目的最后执行。然而相信大多数采取此种方式的都是使用非常见算法或者层叠式加密的，这些算法在大多数硬件上由于没有硬件指令集的协助，处理速度都比较慢，所以若能在启动过程中更早的阶段开始当然是更好的了，于是这里推荐为其创建 system unit 文件并安装至 multi-user.target 的方式实现自动时自动挂载，参考其 systemd.unit man 手册实现即可，不再赘述。

## 总结 ##

其实如果追求安全的话，不使用 Win 系统是最省心的，或者在全盘加密的 Linux 系统下使用虚拟机是最可靠的了。不过如果您无论由于什么原因仍需要保持一个双引导的环境的话，那么通过本文的介绍使得您能放心的采取 VeraCrypt 保护个人数据安全。

