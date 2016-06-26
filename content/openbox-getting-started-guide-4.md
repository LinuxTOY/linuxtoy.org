Title: 窗口管理器 Openbox 入门指南 (4)
Date: 2008-08-04 09:09
Author: toy
Category: Featured
Tags: Guide, Openbox, WM
Slug: openbox-getting-started-guide-4

这是《窗口管理器 Openbox 入门指南》的第四部分。

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

### 控制应用程序 {#applications}

记得我们曾经在介绍[如何将终端窗口嵌入桌面](http://linuxtoy.org/archives/embed-the-terminal-on-the-desktop.html)时，使用过一个名叫 Devil's Pie 的窗口匹配工具。其实，Openbox 就具有类似的功能。通过 Openbox，我们可以控制每一个应用程序的初始状态。比如，URxvt 启动后就没有边框，Gvim 启动后直接放置到第二个桌面，等等。

跟键盘绑定和鼠标绑定一样，控制应用程序的设置也位于 rc.xml 文件中。应用程序的设置使用 `<applications>` 标签定义：  

    <applications> ... </applications>

具体到一个单独的应用程序，则使用 `<application>` 标签，该标签具有 name、class 及 role 属性：

-   name：窗口名称，用来指定一个确定的窗口。
-   class：窗口类名，其作用同上。
-   role：可选属性，对窗口作进一步的匹配，比如可用来区分是针对窗口还是针对对话框进行控制。

其中，name 属性和 class 属性可以仅使用其一，也可同时使用。

举例如下：

    <applications>
     <application name="" class="" role="">
     ...
     </application>
     ...
    </applications>

**获取 name 和 class**

当我们针对应用程序进行设置时，首先需要获取该程序的 name 或 class。这可以通过执行下面的命令来完成：

    xprop WM_CLASS

该命令执行后，鼠标指针将变成十字型，然后在程序窗口中单击即可。例如，单击 Gvim 获得的结果如下：

    WM_CLASS(STRING) = "gvim", "Gvim"

这说明，该窗口的 name 为 gvim，class 为 Gvim。

**实例一：让 Gvim 启动后直接放置到第二个桌面**

可定义如下：

    <application name="gvim">
     <desktop>2</desktop>
    </application>

**实例二：去掉 URxvt 的窗口边框**

作下面的定义：

    <application name="urxvt">
     <decor>no</decor>
    </application>

**实例三：让 Mirage 启动后窗口最大化**

可定义为：

    <application name="mirage">
     <maximized>true</maximized>
    </application>

**使用通配符**

Openbox 在匹配窗口的 name、class 及 role 时，可以使用通配符 \* 和 ?。其中，\* 用来匹配任意多个字符，而 ? 仅能匹配单个字符。例如：

    <application name="*">
     <decor>no</decor>
    </application>

这样就去掉了所有窗口的边框。

上面的例子仅作抛砖引玉之用。其实，通过 Openbox 这项特性，你还可以设置窗口的位置、是否最小化、全屏显示等诸多属性。在 rc.xml 文件的 applications 部分有详细的说明，大家只要照做即可。
