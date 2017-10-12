Title: 增强 Bash 的功能
Date: 2006-11-16 22:13
Author: toy
Category: Tips
Tags: Bash
Slug: bash_tricks

下面两个诀窍可以增强 Bash 的功能，一个是针对 Bash 的命令历史管理进行了改善，另一个是使 Bash 能够具有更加智能的自动完成特性。实现的过程并不复杂，只需修改 Bash 的默认配置即可。

1.  改善 Bash 的命令历史管理功能：

    Bash 的默认配置会存在一个问题，如果同时打开两个（或两个以上的）控制台，那么在这两个控制台中执行的命令并不会互相分享到 history 中。有的命令历史甚至最终会被覆盖掉。要解决这个问题，可把下列内容添加到
    `~/.bashrc` 或 `~/.bash_profile` 文件中：  

        shopt -s histappend 
        PROMPT_COMMAND='history -a'

    第一句的作用是将命令追加到 history 中。第二句是在显示命令提示符时，保存 history。

2.  设置智能的自动完成功能：

    在 Bash 中我们已经可以通过按 Tab 键来享用自动完成的特性。通过下面的设置，则可以使用 Up 和 Down 键来选择命令后所跟的参数。在 `.inputrc`（如果该文件不存在，则创建一个）中加入下列内容：  

        "\e[A": history-search-backward
        "\e[B": history-search-forward
        set show-all-if-ambiguous on

    前两句使用 Up 和 Down 在 history 中进行搜索。后一句是按 Tab 显示自动完成。如果结合 Ctrl - R，则更加好用。

[via [amix](http://amix.dk/blog/viewEntry/19030)]
