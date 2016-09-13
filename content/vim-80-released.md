Title: Vim 8.0 发布
Author: lovenemesis
Date: 2016-09-13 11:00:00
Category: Editor
Tags: vim
Slug: vim-80-released

老牌开源文本编辑器 Vim 发布 8.0 版本，带来了 GTK3 及 DirectWrite 支持。

<!-- PELICAN_END_SUMMARY -->

作为近十年来首个正式版本， Vim 8.0 带来的变化有：

* 新增异步 I/O 支持，得以通过频道的方式实现动态更新来自远程服务器的 JSON 内容
* 支持后台启动任务，管理并完成，比如后台启动编译器或者语法检测工具
* 支持添加定时器
* 针对 Vim 脚本的改善：支援 Lambda 和闭包
* 支持将 Vim 插件打包
* GTK3+ 支持，不过至少目前在两者共存时在编译时优先选择 GTK2+
* DirectWrite 支持，改善渲染效果

[官方发布公告](https://groups.google.com/forum/#!topic/vim_dev/CmiGxtJ7fn4)

[详细变化列表](https://raw.githubusercontent.com/vim/vim/master/runtime/doc/version8.txt)

[Win32 预编译包](ftp://ftp.vim.org/pub/vim/pc/gvim80.exe)

[*nix 源代码包](ftp://ftp.vim.org/pub/vim/unix/vim-8.0.tar.bz2)

*消息来源*：[Phoronix](https://www.phoronix.com/scan.php?page=news_item&px=Vim-8.0-Released)
