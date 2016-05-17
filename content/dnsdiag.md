Title: DNSDiag：诊断 DNS 故障
Date: 2016-05-17 14:26:53
Authors: toy
Category: Apps
Tags: dns, network
Slug: dnsdiag
Via: DNSDiag|https://dnsdiag.org/

DNS 流量被 ISP 劫持？DNS 响应了错误的行为亦或指向了错误的地址？如果你碰到了诸如此类的 DNS 问题，那么别慌，DNSDiag 可以助你排查问题所在。

<!-- PELICAN_END_SUMMARY -->

**安装**

DNSDiag 提供有二进制包，从 [GitHub][g] 下载后解包即可使用：

```
tar zxvf dnsdiag-1.3.4.linux-x86_64-bin.tar.gz
```

DNSDiag 包含 dnsping、dnstraceroute、dnseval 三个工具。

**dnsping**

又一个跟 `ping` 类似的工具，针对 HTTP 的可参考 [httping]({filename}/httping.md)。dnsping 发送 DNS 查询来 ping DNS 服务器：

```
./dnsping -s 8.8.8.8 -c 5 linuxtoy.org
dnsping DNS: 8.8.8.8:53, hostname: linuxtoy.org, rdatatype: A
39 bytes from 8.8.8.8: seq=0   time=111.764 ms
38 bytes from 8.8.8.8: seq=1   time=65.606 ms
39 bytes from 8.8.8.8: seq=2   time=110.593 ms
38 bytes from 8.8.8.8: seq=3   time=67.940 ms
38 bytes from 8.8.8.8: seq=4   time=66.181 ms

--- 8.8.8.8 dnsping statistics ---
5 requests transmitted, 5 responses received,   0% lost
min=65.606 ms, avg=84.417 ms, max=111.764 ms, stddev=24.449 ms
```

其中，`-s` 指定 DNS 服务器，`-c` 为请求次数，linuxtoy.org 为要查询的域名。从结果我们可以看到，查询的最小、最大及平均响应时间。

**dnstraceroute**

这个工具与 `traceroute` 相似，用来查询 DNS 请求的路由：

```
./dnstraceroute --expert -s 8.8.8.8 linuxtoy.org
dnstraceroute DNS: 8.8.8.8:53, hostname: linuxtoy.org, rdatatype: A
1       gateway (10.217.89.1) 1 ms
2       10.210.4.37 (10.210.4.37) 1 ms
3       10.210.2.67 (10.210.2.67) 1 ms
4       254.118.142.219.broad.bj.bj.dynamic.163data.com.cn (219.142.118.254) 2 ms
5       10.210.1.14 (10.210.1.14) 4 ms
6       192.168.5.30 (192.168.5.30) 7 ms
7       180.149.129.217 (180.149.129.217) 7 ms
8        *
9       180.149.128.9 (180.149.128.9) 8 ms
10      202.97.53.146 (202.97.53.146) 8 ms
11      202.97.58.94 (202.97.58.94) 9 ms
12      202.97.91.114 (202.97.91.114) 49 ms
13      202.97.62.214 (202.97.62.214) 47 ms
14      209.85.241.58 (209.85.241.58) 43 ms
15      209.85.142.185 (209.85.142.185) 45 ms
16      216.239.41.7 (216.239.41.7) 152 ms
17      209.85.243.23 (209.85.243.23) 62 ms
18       *
19      google-public-dns-a.google.com (8.8.8.8) 72 ms

=== Expert Hints ===
 [*] public DNS server is next to an invisible hop (probably a firewall)
```

`--expert` 选项可以给出一些有用的提示。

**dnseval**

批量 `ping` 工具，同样是针对 DNS：

```
./dnseval linuxtoy.org
server              avg(ms)     min(ms)     max(ms)     stddev(ms)  lost(%)
---------------------------------------------------------------------------
10.210.12.10        51.627      1.169       503.838     158.891     %0
202.106.182.153     285.889     2.336       604.162     312.265     %14
```

需要指出的是，不仅限于本文所提到的，这三个工具都自带一些有用的选项，可通过 `-h` 查看。

[g]: https://github.com/farrokhi/dnsdiag/releases
