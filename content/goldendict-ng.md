Title: GoldenDict-ng 多格式字典查询软件
Date: 2023-06-03 15:19
Category: App
Tags: 
Slug: goldendict-ng
Authors: slbtty

GoldenDict-ng 是一款开源、功能全面、多格式的字典软件，可以在查询一个单词的时候从多本词典中显示结果。

支持包括 MDict、StarDict、DSL、Zim/Kiwix 等常见的离线字典格式 和 Wiktionary、DictD、LinguaLibre 等在线的资源。并且可以添加任意的网站和程序来当作字典的来源。

<!-- PELICAN_END_SUMMARY -->

GoldenDict-ng 是由国人从原版 GoldenDict 分支出来的，相比原版：

* 支持最新版的 Qt6，用 QtWebEngine 取代不再维护的 QtWebKit
* 处理了大量原版中多年没有解决的 bug 和功能需求，比如暗黑模式、大字典的支持、high DPI 显示、修改字典名称、和 Anki 整合等等
* 内部代码经过重构和优化后可维护性高
* 使用 Xapian 来支持全文搜索
* 通过 libzim 支持最新的 zim 标准
* ...

[仓库地址](https://github.com/xiaoyifang/goldendict-ng) 和 [文档和安装说明](https://xiaoyifang.github.io/goldendict-ng/)

![goldendict-ng]({filename}/images/gdimg1.png)
![goldendict-ng]({filename}/images/gdimg2.png)
