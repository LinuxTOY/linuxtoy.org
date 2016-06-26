Title: 窗口管理器 Openbox 入门指南 (3)
Date: 2008-08-01 09:15
Author: toy
Category: Featured
Tags: Guide, Openbox, WM
Slug: openbox-getting-started-guide-3

这是《窗口管理器 Openbox 入门指南》的第三部分。

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

### 设定键盘和鼠标绑定 {#bindings}

**配置文件**

Openbox 默认的键盘和鼠标绑定文件位于：

    /etc/xdg/openbox/rc.xml

同样复制一份到 .config/openbox/：

    cp /etc/xdg/openbox/rc.xml ~/.config/openbox/

**键盘绑定**

Openbox 的键盘绑定使用 `<keyboard>` 标签，形如下面的内容：  

    <keyboard> ... </keyboard>

要定义一个具体的键盘绑定，我们需要使用 `<keybind>` 标签。该标签具有 key 属性，其作用是指定快捷键。常用的修饰键如下：

-   S - Shift
-   C - Ctrl
-   A - Alt
-   W - Win (即 Windows 徽标键)

例如，假设我要为最大化窗口指定快捷键为 Alt-F6，那么，可以定义如下：

    <keyboard>
     <keybind key="A-F6">
      <action name="MaximizeFull" />
     </keybind>
     ...
    </keyboard>

又如，我想为 URxvt 指定启动快捷键 Win-u，可作下面的定义：

    <keybind key="W-u">
     <action name="Execute">
      <command>urxvt</command>
     </action>
    </keybind>

其实，Openbox 已经默认定义了很多键盘绑定，如切换活动桌面、提升窗口等等，具体内容都可以在上面的 rc.xml 文件中找到。

至于在我们前面的菜单创建过程中、键盘绑定中、以及后面的鼠标绑定中所用的 Action，可以通过下面的地址参考：

<http://icculus.org/openbox/index.php/Help:Actions>

**鼠标绑定**

鼠标绑定使用 <mouse> 标签定义。具体如下：  

    <mouse> ... </mouse>

与键盘绑定不同的是，鼠标绑定会要求你首先设置情景，也就是触发鼠标绑定的对象，即 `<context>` 标签。常用的 Context 如下表所示：

名称                                   | 说明
-------------------------------------- | -----------------------------------
Frame                                  | 除桌面外的任何窗口
Client                                 | 应用程序窗口，不含窗口边框
Desktop                                | 桌面
Root                                   | 与 Desktop 相似，通常用于 Root 菜单
Titlebar                               | 窗口标题栏
Top, Bottom, Left, Right               | 窗口的上、下、左、右四边
TLCorner, TRCorner, BLCorner, BRCorner | 窗口的四角
Icon                                   | 窗口图标
Iconify                                | 最小化按钮
Maximize                               | 最大化按钮
Close                                  | 关闭按钮
AllDesktops                            | 所有桌面按钮
Shade                                  | 折叠按钮
MoveResize                             | 移动并调整窗口大小

扩展上面的例子：

    <mouse>
     <context name="Titlebar">
     ...
     </context>
    </mouse>

Titlebar 说明这是针对标题栏的鼠标操作。

然后，即可使用 `<mousebind>` 标签进行具体的鼠标绑定。该标签具有 button 和 action 属性：

-   button：该属性指定使用哪一个鼠标按钮来触发鼠标绑定，如左键、右键、滚轮等。  

名称     | 说明
-------- | --------
Left     | 鼠标左键
Right    | 鼠标右键
Middle   | 鼠标中键
UP       | 向上滚
Down     | 向下滚

-   action：用来指定一个鼠标触发的事件，如按下、单击、双击等。一些常见的 Action 事件如下表所示：  

名称          | 说明
------------- | ----
Press         | 按下
Click         | 单击
DoubleClick   | 双击
Release       | 释放
Drag          | 拖曳

例如，当我们双击一个窗口时让其最大化，可以作如下定义：

    <mouse>
     <context name="Titlebar">
      <mousebind button="Left" action="DoubleClick">
       <action name="ToggleMaximizeFull"/>
      </mousebind>
     </context>
    </mouse>
