Title: Duplicacy 3.0.1 发布
Date: 2022-10-09 22:00
Category: Howto
Tags: go, backup
Slug: duplicacy_cli_3.0.1
Authors: lovenemesis

[Duplicacy](https://duplicacy.com/home.html) 是一款跨平台的开源文件备份工具，在提供健壮的增量式备份机制的同时又不依赖所以索引数据库，独具一格。最近发布了其[命令行 3.0.1 版本](https://github.com/gilbertchen/duplicacy/releases/tag/v3.0.1)。

相对于其他开源文件备份工具诸如 [duplicity](https://duplicity.gitlab.io/) / [Deja Dup](https://wiki.gnome.org/Apps/DejaDup) 和 [BorgBackup](https://www.borgbackup.org/) / [Pika Backup](https://apps.gnome.org/app/org.gnome.World.PikaBackup/)，Duplicacy 有如下特点：

* 使用 Go 语言实现的**完整的跨平台支持**，支持 Win 32/64，Linux X86/64/ARMv7/ARMv8 和 OSX Intel/Apple；
* **不依赖索引数据库**的[无锁式去重机制](https://github.com/gilbertchen/duplicacy/wiki/Lock-Free-Deduplication);
* 支持多个设备备份至同一存储目标，实现[跨设备去重且允许并行操作](https://forum.duplicacy.com/t/about-duplicacy-nomenclature/2514)；
* 支持文件加密以及非对称密钥，除了基本的本地磁盘备份以外还支持超多的[云端备份供应商](https://forum.duplicacy.com/t/supported-storage-backends/1107)；
* 实现核心功能的**命令行版本开源且可供个人免费使用**，商业使用或其 GUI 版本则需少量[授权费用](https://duplicacy.com/buy.html)。

新版本的 duplicacy 命令行引入了新的快照格式，在运用此格式时[大幅度降低了备份时的内存占用](https://forum.duplicacy.com/t/memory-usage-optimization/5671)。新版本兼容既往老版本创建的快照，所以可以平滑过渡，但老的版本将无法读取新版本创建的快照格式。

笔者在 [Vero 4K](https://linuxtoy.org/archives/osmc-vero-4k-review.html) 上使用 duplicacy 进行文档和媒体文件的定期备份一年有余，感受如下：

* 命令行版本功能完备，很适合脚本化执行；
* 得益于无索引数据库的去重机制，进行**增量备份时的内存占用很小**，且不影响同时运行的其他同步应用；
* 因其配置文件完全存放于备份原目录的设计，在异地恢复备份的方式和其他软件思路稍有不同，务必建议[参考官方指南](https://forum.duplicacy.com/t/restore-to-a-different-folder-or-computer/1103)熟悉清楚；
* 由于需要维持跨平台兼容，目前仍不具备其他类 Unix 专属备份工具那样**将备份快照的当作镜像挂载的功能**，如要从备份仓库中恢复单一文件或目录，则需要熟悉[过滤表达式](https://forum.duplicacy.com/t/filters-include-exclude-patterns/1089);
* 文件扩展属性支持有限，所以更**适合备份数据文件**，而不是系统备份。


[duplicacy 命令行版本下载](https://github.com/gilbertchen/duplicacy-cli/releases)

[快速上手指南](https://forum.duplicacy.com/t/duplicacy-quick-start-cli/1101)


