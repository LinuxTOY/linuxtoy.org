Title: 窗口管理器 Openbox 入门指南 (5)
Date: 2008-08-06 08:30
Author: toy
Category: Featured
Tags: Guide, Openbox, WM
Slug: openbox-getting-started-guide-5

这是《窗口管理器 Openbox 入门指南》的第五部分。

<!-- PELICAN_END_SUMMARY --> 

**目录表**

-   [我喜欢 Openbox 的原因](http://linuxtoy.org/archives/openbox-getting-started-guide.html#reasons)
-   [如何安装 Openbox](http://linuxtoy.org/archives/openbox-getting-started-guide.html#installation)
-   [运行 Openbox](http://linuxtoy.org/archives/openbox-getting-started-guide.html#running)
-   [配置 Openbox](http://linuxtoy.org/archives/openbox-getting-started-guide-2.html#configuration)
-   [设定键盘和鼠标绑定](http://linuxtoy.org/archives/openbox-getting-started-guide-3.html#bindings)
-   [控制应用程序](http://linuxtoy.org/archives/openbox-getting-started-guide-4.html#applications)
-   [使用自动启动脚本](http://linuxtoy.org/archives/openbox-getting-started-guide-5.html#autostart)
-   [提示与技巧](http://linuxtoy.org/archives/openbox-getting-started-guide-5.html#tips)
-   [参考资源](http://linuxtoy.org/archives/openbox-getting-started-guide-5.html#ref)

### 使用自动启动脚本 {#autostart}

通过 Openbox 的自动启动脚本，我们可以随机启动一些程序，像输入法、面板等等。

**前提**

使用自动启动脚本的前提是，你必需使用包含会话功能支持的 Openbox，即 openbox-session。

**创建**

Openbox 默认的自动启动脚本文件位于:

    /etc/xdg/openbox/autostart.sh

你可以在建立自己的自动启动脚本时参考参考。

使用下列命令来建立一个自己的 autostart.sh 文件：

    vim ~/.config/openbox/autostart.sh

比如，我们要开机即加载面板程序 Pypanel，可以加入下面的内容：

    pypanel &

很简单，是不是？如果要加入多个程序，则分行写即可。

### 提示与技巧 {#tips}

**Openbox 常用快捷键**

-   在桌面按鼠标中键，将显示窗口列表菜单
-   Win-d：隐藏屏幕上所有的窗口
-   Alt-Tab：切换窗口
-   Win-(F1-F4)：依次转到第1-4个工作区
-   Alt-F4：关闭窗口
-   Alt-Esc：将下面的窗口提升到上面

**不用敲 startx 直接进入 Openbox**

在没有使用图形化登录管理器的情况下，要进入 Openbox，我们需要敲 startx。如果使用 bash 的话，在 `~/.bash_profile` 中加入下列内容，可以免敲 startx：

    if [[ -z "$DISPLAY" ]] && [[ $(tty) = /dev/vc/1 ]]; then
      startx
      logout
    fi

**设置壁纸**

有多种工具可以设置壁纸，我使用的是 feh：

    feh --bg-scale /path/to/wallpaper.png

示例中的壁纸路径及名称需要换成你自己的。

然后将：

    eval `cat $HOME/.fehbg` &

加入 Openbox 的 autostart.sh 文件。

**设置 GTK 主题**

不用使用任何工具，在 ~/.gtkrc-2.0 中加入：

    gtk-theme-name = "Infini-Herbe"

这将设置 GTK 程序的主题。将引号中的内容换成你自己喜欢的主题名称（下同）。

    gtk-icon-theme-name = "ALLGREY"

设置所用的图标主题。

    gtk-cursor-theme-name = "Vanilla-DMZ-AA"

设置鼠标指针主题。

    gtk-font-name = "Luxi Sans 10"

设置 GTK 程序用的字体。

    gtk-toolbar-style = GTK_TOOLBAR_ICONS

设置工具栏样式，我喜欢只显示图标。

### 参考资源 {#ref}

-   Openbox 主页：<http://icculus.org/openbox/index.php/Main_Page>
-   Openbox 文档：<http://icculus.org/openbox/index.php/Help:Contents>
-   Openbox 主题：<http://www.box-look.org/index.php?xcontentmode=7402>
-   ObConf：<http://icculus.org/openbox/index.php/Obconf>
-   Archlinux Wiki：<http://wiki.archlinux.org/index.php/Openbox>
-   Gentoo Wiki：<http://gentoo-wiki.com/HOWTO_Openbox>
-   Ubuntu Wiki：<https://help.ubuntu.com/community/Openbox>

[完]
