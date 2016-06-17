Title: 窗口管理器 Openbox 入门指南 (2)
Date: 2008-07-31 08:00
Author: toy
Category: Featured
Tags: Guide, Openbox, WM
Slug: openbox-getting-started-guide-2

这是《窗口管理器 Openbox 入门指南》的第二部分。

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

### 配置 Openbox {#configuration}

当 Openbox 安装完成后，其默认的选项设置可能并不合你意。因此，你可以根据自己的使用习惯来对 Openbox 进行配置。要配置 Openbox，既可以采用图形化的工具，也可以直接编辑文件手动配置。

**使用 ObConf**

ObConf 是一个图形化的 Openbox 配置工具，可以完成一些基本的配置，包括：

-   安装、选用或打包 Openbox 主题
-   配置外观 (像窗口按钮布局、字体等) 及窗口行为
-   配置虚拟桌面及桌面边距
-   配置 Dock

可以使用以下指令来安装 ObConf。

在 Archlinux 中，可以执行：

    pacman -S obconf

Debian/Ubuntu 用户可以执行：

    sudo apt-get install obconf

Fedora 用户可执行：

    yum install obconf

启动后的 ObConf 如下图所示：

![obconf.png](http://i.linuxtoy.org/i/2008/07/obconf.png)

鉴于 ObConf 的操作非常直观，在此就不赘述了。大家花点时间琢磨一下，很快就可以上手。

**创建菜单**

最直接配置 Openbox 的方式是手工编辑其配置文件。不过，在编辑之前，一些语法规则是需要我们掌握的。Openbox 默认的菜单文件 (系统级) 位于：

    /etc/xdg/openbox/menu.xml

当你在桌面右击鼠标时，将显示 Openbox 的 Root 菜单。通过此菜单，用户可以执行启动应用程序、注销、退出等操作。

为了避免更新 Openbox 程序时该文件被覆盖，复制一份到：  

    mkdir ~/.config/openbox 
    cp /etc/xdg/openbox/menu.xml ~/.config/openbox/

从 menu.xml 文件的扩展名我们可以看出这是一个 XML 文件。使用任何文本编辑器皆可打开该文件。除了文件首行的 XML 声明外，所有的 Openbox 菜单项目都是由 `<openbox_menu>` 标签所包围的。

1. **一级菜单**

    首先，让我们来创建一个一级菜单。要定义一个菜单，我们需要使用 `<menu>` 标签。该标签具有 id、label、以及 execute 属性：

    -   id：每一个菜单项目都必须指定一个唯一的 id，以用来区分其他菜单项目。
    -   label：用来描述一个菜单的名称。
    -   execute：执行一个命令，常用于创建动态菜单。

    例如，我们可以将 Openbox 的 Root 菜单定义如下：  `<menu id="root-menu" label="Openbox Root Menu"> ... </menu>`

    如果一个菜单中没有任何项目，我想是不能称其为真正的菜单吧。所以，我们还需要为菜单创建具体的菜单项目。要定义菜单项目，我们可以使用 `<item>` 标签。与 `<menu>` 标签一样，`<item>` 标签也具有描述菜单项目名称的 label 属性。我们试着扩展上面的例子：

            <menu id="root-menu" label="Openbox Root Menu">
            <item label="URxvt">
            ...
            </item>
            ...
            </menu>

    现在，我们已经有了一个名为 URxvt 的菜单项目。根据该名称的命名初衷，我们当然希望通过该菜单项目能够启动 URxvt 终端程序。要完成这个任务，我们需要使用 `<action>` 标签。该标签主要用来执行一个操作，比如启动程序。`<action>` 标签具有 name 属性。我们继续扩展先前的例子：

            <menu id="root-menu" label="Openbox Root Menu">
            <item label="URxvt">
            <action name="Execute">
            ...
            </action>
            </item>
            ...
            </menu>

    该例中 name 属性已经包含了“Execute”值，其作用是启动一个程序。

    我想，你已经猜到接下来我们需要做什么了。要启动程序，没有具体的命令是不行的。这可以通过 `<command>` 标签来完成。我们仍以前面的例子来说明：

            <menu id="root-menu" label="Openbox Root Menu">
            <item label="URxvt">
            <action name="Execute">
            <command>urxvt</command>
            </action>
            </item>
            ...
            </menu>

    值得一提的是，命令可以附带路径或选项参数。

2. **几个特殊的菜单项目**

    在此，我们介绍几个较为特殊的菜单项目：

    -   分隔线：可以使用 `<separator>` 标签在菜单项目间绘制一条分隔线。`<separator>` 标签同样具有 label 属性。需要注意的是，因为 `<separator>` 标签没有具体的内容，所以在关闭该标签时，应照下面的方式进行：

            <separator />

        这是另一个例子，包含 label 属性：

            <separator label="tools" />

    -   重新配置 Openbox：使用该菜单项目的好处是，当你对 Openbox 的配置文件进行修改后，不必注销系统便可即时生效。该菜单项目定义如下：

            <item label="Reconfigure">
            <action name="Reconfigure" />
            </item>

        注意，这里 `<action>` 标签的关闭方式与 `<separator>` 一样。

    -   重新启动 Openbox：

            <item label="Restart">
            <action name="Restart" />
            </item>

    -   退出 Openbox：

            <item label="Exit">
            <action name="Exit" />
            </item>

    -   注销会话：

            <item label="Session Logout">
            <action name="SessionLogout" />
            </item>

        注意，需要启动带会话支持的 Openbox 才有效。

3. **二级菜单**

    掌握了创建一级菜单的方法，二级菜单则如法炮制即可。当二级菜单创建完毕之后，可按以下方法加入一级菜单：

        <menu id="tool-menu" />

附：我的 [menu.xml](http://i.linuxtoy.org/files/openbox/menu.xml) 文件，仅供参考。
