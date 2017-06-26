Title: 处理 Intel Skylake/Kaby Lake 处理器超线程 bug
Date: 2017-06-26 12:58:25
Authors: toy
Category: Tips
Tags: Intel
Slug: intel-processor-ht
Via: https://lists.debian.org/debian-devel/2017/06/msg00308.html

近日，Debian 开发者在其邮件列表中披露了 Intel Skylake 及 Kaby Lake
处理器存在超线程 bug 的问题。该 bug
将导致难以预料的系统行为，包括应用程序崩溃、数据损坏或丢失等等。

<!-- PELICAN_END_SUMMARY -->_

### 检查处理器型号

    grep name /proc/cpuinfo | sort -u

根据结果对照 [Skylake][s] 及 [Kaby Lake][k] 列表查询。

### 检查是否支持超线程

    grep -q '^flags.*[[:space:]]ht[[:space:]]' /proc/cpuinfo && \
        echo "Hyper-threading is supported"

如果你的 CPU 不支持超线程，则可以忽略。否则，请继续后续步骤。

### Skylake 处理器修复法

    grep -E 'model|stepping' /proc/cpuinfo | sort -u

若得到的处理器型号为 78 或 94，且 stepping 是 3，那么可以安装最新版本的
intel-microcode 包（20170511）来解决。

否则，只能通过 BIOS/UEFI 禁用超线程支持。

### Kaby Lake 处理器修复法

目前只能通过 BIOS/UEFI 禁用超线程支持来避免此 bug。

[s]: http://ark.intel.com/products/codename/37572/Skylake
[k]: http://ark.intel.com/products/codename/82879/Kaby-Lake
