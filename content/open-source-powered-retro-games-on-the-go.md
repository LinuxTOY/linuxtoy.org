Title: 经典游戏的开源引擎重制移动版
Date: 2024-04-30 20:30
Category: Games
Tags: classic, psv, android, gog
Slug: open-source-powered-retro-games-on-the-go
Authors: lovenemesis

伪小长假即将到来，无论你是打算宅在家中躲避拥堵，还是打算成为一位出行的“大聪明”，本文精选的这几款经典游戏的开源引擎重制版，配合从业界良心 [GOG.com](https://www.gog.com/)合法获得的素材包，都能使你在或安静或拥堵的假期中再次领略没有氪金的美好。

这次的介绍的游戏符合均以下几个标准：

* 引擎是**开源重制**的，完成度较高，可以应用于包括 Linux 在内的主流桌面操作系统；
* 原始游戏**素材可以合法的渠道**取得；
* **社区相对活跃**，最近版本不早于 2022 年；
* 具备**对应的移动端**版本，可以是手机或掌机；

由于笔者并非 FPS 达人，所以对于无处不在的 Doom 和 Quake 移植就不赘述了。

## 英雄无敌之魔法门2 fheroes2 ##

[fheroes2](https://ihhub.github.io/fheroes2/) 是奇幻风格的战棋类策略游戏[英雄无敌之魔法门2](https://www.gog.com/en/game/heroes_of_might_and_magic_2_gold_edition) 的开源引擎重制。粉丝团体们近乎完美的复刻了当年的体验的基础上，增加了高分辨率界面和移动平台端的触摸操作，修订了原版一系列的 Bug。

引擎项目主线支持 Android、PS Vita、Switch 移动平台，从项目 Release 页面即可获得。经过笔者在 PS Vita 上的测试体验良好。

* [项目主页](https://ihhub.github.io/fheroes2/)
* [GOG.com 商店](https://www.gog.com/en/game/heroes_of_might_and_magic_2_gold_edition)
* [Flathub](https://flathub.org/apps/io.github.ihhub.Fheroes2)

值得一提的是：
* 该应用的 Flathub 版本在安装时会默认从 Web Archive 尝试下载 Demo 版本，可能由于网络原因而失败；
* 从已经安装好的 GOG.com 版本安装目录提取 `anime` 有些麻烦，使用随附的脚本从安装文件获取更便捷；
* [PS Vita 安装教程](https://github.com/ihhub/fheroes2/blob/master/docs/README_PSV.md)对于 `anime`存放的路径描述有误。

## 英雄无敌之魔法门3  VCMI ##

[VCMI](https://vcmi.eu/)是奇幻风格的战棋类策略游戏[英雄无敌之魔法门3](https://www.gog.com/en/game/heroes_of_might_and_magic_3_complete_edition) 的开源引擎重制，支持地图编辑器和多人联机的功能。

引擎项目主线仅支持 Android 移动平台，可从 [F-Droid 获取](https://f-droid.org/packages/is.xyz.vcmi/)。经过笔者测试，工作良好但是触屏操作需要熟悉。

安装简单，将原版桌面版安装目录下对应的目录按照说明复制到 `vcmi` 的目录下即可。

* [项目主页](https://vcmi.eu/)
* [GOG.com 商店](https://www.gog.com/en/game/heroes_of_might_and_magic_3_complete_edition)
* [Flathub](https://flathub.org/apps/eu.vcmi.VCMI)

## 凯撒3 augustus ##

[augustus](https://github.com/Keriew/augustus)是历史题材模拟建设游戏[凯撒3](https://www.gog.com/game/caesar_3)的开源引擎重制。这个版本引入了游戏机制上的优化，相应的更新更为活跃一些。

引擎项目主线支持 Android、PS Vita、Switch 移动平台，从项目 Release 页面即可获得。经过笔者在 PS Vita 上的测试体验良好。

安装简单，将原版桌面版安装目录下对应的目录按照说明复制到 `augustus` 的目录下即可。

* [项目主页](https://github.com/Keriew/augustus)
* [GOG.com 商店](https://www.gog.com/game/caesar_3)
* [Flathub](https://flathub.org/apps/com.github.keriew.augustus)

## 暗黑破坏神 DevilutionX ##

[DevilutionX](https://github.com/diasurgical/devilutionX)是斜视角动作 RPG 的早期标志性游戏[暗黑破坏神](https://www.gog.com/game/diablo)的开源引擎重制，提供广泛的平台支持。

引擎项目主线支持 Android、PS Vita、Switch 移动平台，从项目 Release 页面即可获得。笔者尚未测试，不过从活跃的社区和视频平台他人的分享来看，完成度很高。

* [项目主页](https://github.com/diasurgical/devilutionX)
* [GOG.com 商店](https://www.gog.com/game/diablo)
* [Flathub](https://flathub.org/apps/org.diasurgical.DevilutionX)

## 命令与征服 Vanilla-Conquer ##

[Vanilla-Conquer ](https://github.com/TheAssemblyArmada/Vanilla-Conquer/)是即时战略风格游戏早期的标志性游戏[命令与征服](https://www.pcgamingwiki.com/wiki/Command_&_Conquer)的开源引擎重制，和另一个同样活跃的 [OpenRA](https://www.openra.net/) 引擎重制项目相比，这款专注于还原初心体验。

注意的是：
* 该项目并没有固定的发布版本，但是[其 CI 版本相对频繁](https://github.com/TheAssemblyArmada/Vanilla-Conquer/releases)，简单方便，将二进制文件解压到从光盘中获取的游戏素材目录即可。
* 获取素材过程中需要用到 [Unshieldv3](https://github.com/wfr/unshieldv3) 处理一个特别的压缩文件。
* 引擎项目主线没有包含移动版，但其一个紧密跟进的[分支提供了 PS Vita 平台](https://github.com/Northfear/Vanilla-Conquer-vita)的支持。从其 [Release 页面](https://github.com/Northfear/Vanilla-Conquer-vita/releases/)获得安装包，拷贝入素材即可。经过笔者的测试，体验良好。

这款游戏本身已经被 EA 在多年前以免费软件的方式分发，但由于时间原因原下载链接已经失效。现在**可从 mod 社区合法获取**：

* [GDI](https://www.moddb.com/games/cc-gold/downloads/command-conquer-gold-free-game-gdi-iso)
* [NOD](https://www.moddb.com/games/cc-gold/downloads/command-conquer-gold-free-game-nod-iso)
* [ALLIED](https://www.moddb.com/games/cc-red-alert/downloads/cc-red-alert-full-game-allied-iso)
* [SOVIET](https://www.moddb.com/games/cc-red-alert/downloads/cc-red-alert-full-game-soviet-iso)
