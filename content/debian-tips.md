Title: Debian GNU/Linux 包管理妙计串烧
Date: 2016-08-15 20:41:26
Authors: toy
Category: Tips
Tags: debian
Slug: debian-tips

作为一个资深的 Debian GNU/Linux（后文简称“Debian”）粉，笔者可是私藏了不少既实用又鲜为人知的锦囊妙计哦。独乐乐不如众乐乐，现从中撷取几条分享给大家，希望对各位有所帮助。

<!-- PELICAN_END_SUMMARY -->

**当包管理工具被玩坏……**

设想有一天你不小心误删了 `dpkg`，因为它是 Debian 中最底层的包管理工具，所以然后你将杯具地发现从此再也不能成功安装 Debian 包。别慌，如果你了解一点儿有关 `.deb` 二进制包的知识，那么可以使用如下方法解决：

1. 从 Debian 官方网站下载 dpkg 的 `.deb` 包，形如 `dpkg_1.17.26_amd64.deb`。其中，`amd64` 说明该包支持 64 位架构。若你的 Debian 系统为其它架构，请自行选择合适的包文件。

2. 先用 `ar` 工具对 `.deb` 解包：

        ar x dpkg_1.17.26_amd64.deb

    可能大家对于 `tar` 比较熟悉，这个 `ar` 又是什么东东？`ar` 是一个比 `tar` 还要古老的归档工具，这里的 `x` 指令是提取的意思，跟 `tar` 类似。

3. 再用 `tar` 将所需文件展开到 /（根目录）：

        tar -C / -p -xzf data.tar.gz

至此，笔者已经将 `dpkg` 安装到 Debian 系统。莫名消失的 `dpkg` 重新回到身边，你是否觉得应倍加珍惜呢？也许你会多留一个心眼，为什么这样做有效？让我们回到基础来谈一谈吧。

当我们用 `ar` 解包 `.deb` 后，一般将会得到下列三个文件：

    -rw-r--r-- 1 root root    9543 Aug 16 08:26 control.tar.gz
    -rw-r--r-- 1 root root 2980910 Aug 16 08:26 data.tar.gz
    -rw-r--r-- 1 root root       4 Aug 16 08:26 debian-binary

+ `debian-binary`：用来指明 `.deb` 文件所用版本的文本文件，本例为 2.0。
+ `control.tar.gz`：该存档文件包含与包相关的各种元信息，像是包名称及版本。其它一些信息则是包管理工具所需要的，据此能够决定是否可安装或卸载。如果你对此充满好奇，那么不妨用 `tar` 将其解包细看。

        -rw-r--r-- 1 root root    87 Nov 26  2015 conffiles
        -rw-r--r-- 1 root root  2621 Nov 26  2015 control
        -rw-r--r-- 1 root root 10133 Nov 26  2015 md5sums
        -rwxr-xr-x 1 root root  1965 Nov 26  2015 postinst
        -rwxr-xr-x 1 root root  1500 Nov 26  2015 postrm
        -rwxr-xr-x 1 root root  2126 Nov 26  2015 preinst
        -rwxr-xr-x 1 root root  4838 Nov 26  2015 prerm

+ `data.tar.gz`：这个存档文件包含要从包中提取的所有文件，比如可执行文件、文档等等。值得一提的是，除了末尾的 `.gz` 之外，Debian 有时也会使用其它压缩格式：`data.tar.bz2` 是 bzip2、`data.tar.xz` 为 XZ。

        ./var
        ./var/lib
        ./var/lib/dpkg
        ./var/lib/dpkg/updates
        ./var/lib/dpkg/alternatives
        ./var/lib/dpkg/info
        ./var/lib/dpkg/parts
        ./usr
        ./usr/share
        ./usr/share/locale
        ./usr/share/dpkg
        ./usr/share/dpkg/cputable
        ./usr/share/dpkg/ostable
        ./usr/share/dpkg/triplettable
        ./usr/share/dpkg/abitable
        ./usr/share/doc
        ./usr/share/doc/dpkg
        ./usr/share/doc/dpkg/changelog.gz
        ./usr/share/doc/dpkg/AUTHORS
        ./usr/share/doc/dpkg/changelog.Debian.gz
        ./usr/share/doc/dpkg/THANKS.gz
        ./usr/share/doc/dpkg/usertags.gz
        ./usr/share/doc/dpkg/README.feature-removal-schedule.gz
        ./usr/share/doc/dpkg/copyright
        ./usr/share/lintian
        ./usr/share/lintian/overrides
        ./usr/share/lintian/overrides/dpkg
        ./usr/share/man
        ./usr/bin
        ./usr/bin/dpkg-trigger
        ./usr/bin/dpkg-deb
        ./usr/bin/dpkg
        ./usr/bin/dpkg-query
        ./usr/bin/dpkg-split
        ./usr/bin/dpkg-maintscript-helper
        ./usr/bin/dpkg-divert
        ./usr/bin/update-alternatives
        ./usr/bin/dpkg-statoverride
        ./usr/sbin
        ./usr/sbin/dpkg-statoverride
        ./usr/sbin/update-alternatives
        ./usr/sbin/dpkg-divert
        ./sbin
        ./sbin/start-stop-daemon
        ./etc
        ./etc/dpkg
        ./etc/dpkg/dpkg.cfg.d
        ./etc/dpkg/dpkg.cfg
        ./etc/alternatives
        ./etc/alternatives/README
        ./etc/cron.daily
        ./etc/cron.daily/dpkg
        ./etc/logrotate.d
        ./etc/logrotate.d/dpkg

**同时安装和移除包**

这是笔者最为喜欢的一条妙计。对于 `apt/apt-get/aptitude install` 或 `apt/apt-get/aptitude remove` 来安装/移除包，想必大家都比较熟悉，可是你知道它们还能同时安装并移除包么？

因为笔者同时也是一位不折不扣的 Vim 粉，所以会执行如下命令来安装 Vim，但这条指令的作用绝不仅仅于此：

    apt install vim emacs-

该指令在将 Vim 安装到 Debian 中的同时也会移除 Emacs。emacs 后面的 `-` 起移除作用。

与此等效的命令是：

    apt remove emacs vim+

vim 之后的 `+` 为安装之意。

**阻止升级某些包**

在执行系统更新时，有时候笔者想阻止某些个别的包升级， Debian 下可以使用 `apt-mark` 命令。

+ 阻止包

        apt-mark hold <pkg>

    比如，阻止升级 Perl，执行 `apt-mark hold perl` 即可。

+ 取消阻止

    如果不想阻止了，那么可以通过 `apt-mark unhold` 取消：

        apt-mark unhold <pkg>

+ 显示已阻止的包

    要查看已经被阻止的包，则可以执行：

        apt-mark showhold

**缓存代理包**

虽然 Debian 官方针对世界各地提供了包仓库的镜像，但有时候还是会感觉下载的速度不够理想。另外，如果你有多个 Debian 系统，那么架设一个本地的包缓存代理服务显然是一种既经济又高效的方式。

APT 包管理工具除了支持标准的 HTTP/FTP 代理方法外，Debian 也具有专门的软件来搭建代理缓存服务器。在此，笔者向各位推荐 Approx。你可以将 Approx 看作是远端仓库的镜像，只不过这个镜像在本地而已。

Approx 的使用方法很简单，按如下步骤执行即可：

+ 安装 Approx

        apt install approx

+ 配置 Approx

    Approx 的配置文件存于 `/etc/approx/approx.conf`，将下列地址行前的注释去掉：

        # <name> <repository-base-url>
        debian   http://ftp.debian.org/debian
        security http://security.debian.org

+ 配置 `sources.list`

    Approx 默认监听 9999 端口，调整需要使用代理缓存的 Debian 系统的 `sources.list` 文件，将其指向 Approx 所在机器的域名或 IP：

        deb http://192.168.0.2:9999/debian jessie main contrib non-free
        deb http://192.168.0.2:9999/security jessie/updates main contrib non-free

**在多台系统安装相同的包**

笔者有两台 VPS 都跑着 Debian 系统，它们的基本环境几乎一致。为了方便省事，在一台系统上装好所需要的包之后，将其导出为包列表：

    dpkg --get-selections > installed_pkgs.txt

接着，把导出的列表文件 `installed_pkgs.txt` 传输到另一台系统。并执行以下操作：

    # 更新 dpkg 的包数据库
    apt-cache dumpavail > avail.txt
    dpkg --merge-avail avail.txt
    # 更新 dpkg 的包列表
    dpkg --set-selections < installed_pkgs.txt
    # 安装选择的包
    apt-get dselect-upgrade

若有其它 Debian 系统，则依法炮制即可。
