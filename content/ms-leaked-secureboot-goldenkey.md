Title: MS Secure Boot 金钥匙泄漏？
Author: lovenemesis
Date: 2016-08-15 14:05:00
Category: News
Tags: secureboot, uefi
Slug: ms-leaked-secureboot-goldenkey

近日 MS Secure Boot 金钥匙泄漏的事情热火朝天，然而究竟有多大影响呢？

<!-- PELICAN_END_SUMMARY -->

[爆料页面](https://rol.im/securegoldenkeyboot/)可读性相当差；[主流科技媒体](http://arstechnica.com/security/2016/08/microsoft-secure-boot-firmware-snafu-leaks-golden-key/)的报道也是一团混杂；在下毫无 WinRT 设备经验，对于它 UEFI 的诸多坑并不太明白。一直 [Matthew Garrett 的博文](http://mjg59.dreamwidth.org/44223.html)才算是清楚了是什么原因，再次稍微总结下，便于快速掌握要领：

* 这次泄漏的并不算后门，所以也不能算“金钥匙”
* 泄漏的文件是用于 MS Surface ARM 系列产品的 **UEFI 安全策略附加文件**，主要用途是为了方便开发者深度定制
* 由于 MS UEFI 早期版本的设计缺陷，它们会错误当把该 UEFI 安全策略附加文件当作完整安全策略。所以若应用在早期版本的 MS Surface ARM 产品上时会导致包括 Secure Boot 在内的安全机制关闭
* 该特定于 MS Surface ARM 系列产品的问题已经在 Win10 AE 更新中修复了
* 在 MS Surface ARM 设备上刷入 UEFI 安全策略是需要人工干预的，无法悄无声息的植入 UEFI
* 非 Surface ARM 系列产品的 UEFI 不受此问题影响，甚至 Surface Pro 等 X86 处理器的产品也不受此影响
* 运行在 UEFI 环境下的非 Windows 操作系统也是**不受此影响**的


[消息来源](https://twitter.com/tuxradar/status/763661409917997057)
