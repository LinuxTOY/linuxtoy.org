Title: grimd：阻止广告的 DNS 代理
Date: 2016-05-12 16:58:14
Authors: toy
Category: Apps
Tags: dns, proxy, go
Slug: grimd
Via: grimd|https://github.com/looterz/grimd

grimd 是使用 Go 语言编写的 DNS 代理，它能自动获取多个锁定网址列表。利用 grimd，你可以阻止本机访问广告及恶意网站。

<!-- PELICAN_END_SUMMARY -->

[![grimd]({filename}/images/grimd.thumb.png)]({filename}/images/grimd.png)

**安装**

利用 `go` 直接获取即可：

    go get github.com/looterz/grimd

或[下载预编译的二进制][d]，如 64 位为：

    chmod a+x grimd_linux_x64
    ./grimd_linux_x64 # 需要 root 权限

首次启动 grimd，它将生成 `grimd.toml` 配置文件。稍后，可根据需要修改。

**添加 Systemd 启动文件**

将下列内容保存为 `/etc/systemd/services/grimd.service`，根据实际情况调整路径：

```
[Unit]
Description=grimd dns proxy
Documentation=https://github.com/looterz/grimd
After=network.target

[Service]
User=root
WorkingDirectory=/root/grim
LimitNOFILE=4096
PIDFile=/var/run/grimd/grimd.pid
ExecStart=/root/grim/grimd_linux_x64 -update
Restart=always
StartLimitInterval=30

[Install]
WantedBy=multi-user.target
```

**Web 界面**

grimd 提供有 REST API，也可通过 [reaper][r] 查看其数据。

[d]: https://github.com/looterz/grimd/releases
[r]: https://github.com/looterz/reaper
