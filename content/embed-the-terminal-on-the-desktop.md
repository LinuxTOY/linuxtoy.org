Title: 在你的 Linux 桌面嵌入终端窗口
Date: 2007-08-24 16:37
Author: toy
Category: Tips
Slug: embed-the-terminal-on-the-desktop

除了我们曾经介绍过的 [Tilda 和 Yakuake 终端](http://linuxtoy.org/archives/tilda-and-yakuake.html)具有嵌入桌面的效果之外，使用 [Devil's Pie](http://www.burtonini.com/blog/computers/devilspie) 这个小程序你同样可以将终端窗口嵌入到你的 Linux 桌面。

<!-- PELICAN_END_SUMMARY -->

![Devil's Pie](http://i.linuxtoy.org/i/2007/08/devilspie.png)

下面就以 GNOME Terminal 为例来说明嵌入到桌面的过程：

1.  **安装 Devil's Pie：**

    在 Debian/Ubuntu 中可以通过执行下列指令安装 Devil's Pie：

        sudo apt-get install devilspie

    如果你使用其他 Linux 发行版，那么可以[获取 Devil's Pie 的源代码](http://www.burtonini.com/computing/devilspie-0.20.2.tar.gz)编译安装：

        ./configure && make && make install

2.  **创建 Devil's Pie 的配置文件：**

    在终端中执行：  

        mkdir ~/.devilspie 
        nano ~/.devilspie/DesktopConsole.ds

    然后添加下列内容：

        (if
                (matches (window_name) "DesktopConsole")
                (begin
                        (set_workspace 4)
                        (below)
                        (undecorate)
                        (skip_pager)
                        (skip_tasklist)
                        (wintype "utility")
                        (geometry "+50+50")
                        (geometry "924x668")
                )
        )

    此时，你可以根据自己的需要作出适当调整，如使用哪一个工作区、终端窗口的位置及大小等。

3.  **创建名为“DesktopConsole”的 GNOME Terminal 配置文件：**

    取消选择“常规”标签中的默认显示菜单栏，在“滚动”标签中将滚动栏禁用，切换到“效果”标签可以设置为透明背景。

4.  **将 Devil's Pie 和 GNOME Terminal 添加到会话中：**

    这样可以让 Devil's Pie 和 GNOME Terminal 随机自动运行。你需要在“启动程序”中添加：  

        devilspie
        gnome-terminal --window-with-profile=DesktopConsole

    注销并重新登录系统即可让上述设置生效。

其实，Devil's Pie 是一个蛮有意思的程序，它还有很多其它玩法，你不妨参阅它的[详细说明](http://foosel.org/linux/devilspie)。

[[via](http://ubuntuforums.org/showthread.php?t=202249)]
