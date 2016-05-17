Title: httping：测量网站延迟
Date: 2016-05-17 09:56:34
Authors: toy
Category: Apps
Tags: ping, http, network
Slug: httping
Via: httping|https://www.vanheusden.com/httping/

遇到网络问题的时候，我们一般会先通过 `ping` 这个工具来了解基本的情况。httping 与 `ping` 类似，不过它不是发送 ICMP 请求，而是发送 HTTP 请求。利用
httping，我们可以测量出 Web 服务器跟网络的延迟。

<!-- PELICAN_END_SUMMARY -->

**安装**

```
apt-get install httping # Debian/Ubuntu
yum install httping     # Fedora/CentOS/RHEL
yaourt -S httping       # Arch Linux
emerge -av httping      # Funtoo/Gentoo
```

**使用**

假如我们想测测 linuxtoy.org，那么可以执行：

```bash
httping -g https://linuxtoy.org -l -c 5 -Y

PING linuxtoy.org:443 (/):
connected to 173.252.207.108:443 (402 bytes), seq=0 time=4190.59 ms 
connected to 173.252.207.108:443 (401 bytes), seq=1 time=1195.44 ms 
connected to 173.252.207.108:443 (402 bytes), seq=2 time=940.84 ms 
connected to 173.252.207.108:443 (401 bytes), seq=3 time=888.14 ms 
connected to 173.252.207.108:443 (401 bytes), seq=4 time=1122.04 ms 
--- https://linuxtoy.org/ ping statistics ---
5 connects, 5 ok, 0.00% failed, time 13338ms
round-trip min/avg/max = 888.1/1667.4/4190.6 ms
```

简单介绍一下这里用到的选项：

+ `g`：要测量的网址
+ `-l`：使用 SSL 连接
+ `-c`：这个和 `ping` 一样，为请求数量
+ `-Y`：启用颜色输出

httping 还支持 IPv6、代理、超时、请求头等其他特性，详情可以通过 `man httping` 查询。值得一提的是，httping 也有 Android 版本，有需要有朋友可通过 Google Play 获取。
