Title: 使用 apcupsd 实现 UPS 断电自动关机
Author: lovenemesis
Date: 2016-06-26 13:30:00
Category: Tips
Slug: howto-use-apcupsd-to-automatically-shutdown-system-during-outrage
Tags: raspberrypi

炎炎夏日，唯一比头顶的烈日更加恼人的便是停电了。空调没了不说，正在处理的数据或者游玩的游戏被意外中断，简直令人抓狂，这个时候一款可靠且智能的 UPS 显得尤其重要。

<!-- PELICAN_END_SUMMARY -->

由于所处的环境，在下的 PC 多年来配合 APC 的 [BK500Y UPS](https://detail.tmall.com/item.htm?id=37082783933)，该款体积小巧，价格便宜，可谓是入门 APC 的首选，几次拯救了正在处(you)理(wan)的数(zhan)据(ju)。但对于长期处于无人值守状况下运行的 NAS 来说，单纯的报警声可就远远不够了，需要一款可以在断电或者其他电力异常条件下主动向操作系统发出关机指令的智能 UPS。

经过浏览和比较，选定了 APC 家的 [BK650](https://detail.tmall.com/item.htm?id=37079450807) UPS，该款 UPS 提供 400W 的输出，在断电的时候完全足够支撑 NAS 和路由器等低功耗设备的运行。

### 硬件安装

硬件上的安装没什么特别的，注意前端**无需断路保护**，也不要再连接电力猫等设备了。而将配送的串行-USB 线分别插入 UPS 和 NAS 设备的 USB 接口即可。BK650 还可以提供对于电话线路的保护，不过在下并没有用上。

### 软件配置

若是使用诸如 MyCloud Mirror 之类的现成 NAS 的话，可以在其 Web 管理页面找到 UPS 管理的选项，不过比较简单，也就是选定下在剩余多少电量时执行安全关机。

若是使用 Raspberry Pi 等 SBC 自行组建的 NAS 的，则需要安装 [apcupsd](http://www.apcupsd.org/) 这款软件包实现控制。

`apcupsd` 是个跨平台的开源 APC UPS 管理工具，其 Linux 版本被收录于各大 Linux 发行版的仓库中。它由社区爱好者维护开发，同时也收到 APC 官方的强力支持，项目还算活跃，截至目前最新版本为 3.14.14 。

下面以基于 Debian Jessie 的 OSMC 版本为例说明下如何配置 `apcupsd`。

1. 安装： `sudo apt-get install apcupsd`，如果偏好图形化配置的话它还有 Web 和 GUI 工具可以安装
2. 用顺手的文本编辑器打开 `/etc/apcupsd/apcupsd.conf`，开始编辑
3. 在 `UPSNAME` 后面给个易懂的名字
4. 在 `UPSCABLE` 后指定为 `usb`
5. 在 `UPSTYPE` 后更改为 `usb`
6. 在 `DEVICE` 后为空，这样系统便会自动检测 USB 连接 UPS
7. 所必要的配置到此结束，可以保存退出了。如果感兴趣的话可以调整下面的关机触发条件，有剩余电量和剩余时间，默认为5%和3分钟。注意这里**只要满足其中任一条件**便会触发。
8. 用顺手的文本编辑器打开 `/etc/default/apcupsd`，将其中的 `ISCONFIGURED=` 置为 `yes`。
9. 尝试用 `sudo /sbin/apcaccess` 访问下 UPS，若能返回有效内容，代表配置正常
10. 使用 `systemctl` 开启 `apcupsd` 服务且将器设定为自动启动

若想检测下是否有效，可以断开连接 UPS 的市电，看看 NAS 是否会自动关机。

### 总结

配合 apcupsd，APC BK650 除了可以实现自动关机以外，还能实现邮件通知管理员、广播给当前登录用户等各种实用的功能，相当灵活。欢迎诸位童鞋在分享下自己的使用经验和技巧。
