Title: 跟 Toy 玩自架服务器：5 分钟搭一架梯子
Date: 2017-03-09 21:20:54
Authors: toy
Category: Tutorials
Tags: selfhosted-server
Slug: selfhosted-server-4
Via: 

笔者初次触网大概在千禧年之后不久，那时虽然在上网前耳朵要被迫接受一段“猫叫”，而且速度也不怎么样，但哪里都可以冲浪的快感依然让人感觉兴奋不已。网络因自由而兴，如今却被人为加筑了高墙，搭梯子也成了必备的技能。但是如何才能快速地架梯呢？且听笔者慢慢道来。

<!-- PELICAN_END_SUMMARY -->

本篇笔者以 [Shadowsocks-libev][1] 为例加以说明：

1. 具有一台正跑着的 VPS，如果你还没有，那么可以参考本系列文章在 [Vultr][2]、[Linode][3]、[DigitalOcean][4] 上创建一台。

2. 遵照第一篇克隆 [Selfhosted Servers][5]。

3. 打开 `group_vars/all.yml`，转到下列行：

        shadowsocks:
          server_port: "8530"
          local_port: "1080"
          timeout: "600"
          encryption_method: "chacha20-ietf"
          tcp_fast_open: "true"
          location: "/etc/shadowsocks-libev"
          password_file: "/etc/shadowsocks-libev/shadowsocks-password.txt"

    可酌情根据需要更改选项：

    + `server_port`：服务器端口号
    + `local_port`：本机端口号
    + `timeout`：超时
    + `encryption_method`：加密方法
    + `tcp_fast_open`：开启 TCP 快速打开，推荐启用
    + `location`：配置存储位置，不必更改
    + `password_file`：密码从此文件获取

4. 创建 `play-shadowsocks.yml`，其内容如下：

        ---
        - hosts: all
          become: True

          roles:
          - shadowsocks

5. 执行：

        ansible-playbook -i <你的 VPS IP 或域名>, play-shadowsocks.yml

    注意，其后的 `,` 不可少。

    以下为执行输出结果，用时也就 5 分钟：

        PLAY [all] *********************************************************************

        TASK [setup] *******************************************************************
        Thursday 09 March 2017  22:05:55 +0800 (0:00:00.017)       0:00:00.017 ********
        ok: [xxx.xx.xxx.xx]

        TASK [shadowsocks : Install shadowsocks-libev] *********************************
        Thursday 09 March 2017  22:06:57 +0800 (0:01:01.376)       0:01:01.394 ********
        changed: [xxx.xx.xxx.xx]

        TASK [shadowsocks : Generate Shadowsocks password] *****************************
        Thursday 09 March 2017  22:07:21 +0800 (0:00:24.083)       0:01:25.477 ********
        changed: [xxx.xx.xxx.xx]

        TASK [shadowsocks : Get Shadowsocks password] **********************************
        Thursday 09 March 2017  22:07:29 +0800 (0:00:08.719)       0:01:34.197 ********
        changed: [xxx.xx.xxx.xx]

        TASK [shadowsocks : Generate Shadowsocks config] *******************************
        Thursday 09 March 2017  22:07:42 +0800 (0:00:12.182)       0:01:46.380 ********
        changed: [xxx.xx.xxx.xx]

        RUNNING HANDLER [shadowsocks : Restart shadowsocks-libev] **********************
        Thursday 09 March 2017  22:11:12 +0800 (0:03:30.699)       0:05:17.079 ********
        changed: [xxx.xx.xxx.xx]

        PLAY RECAP *********************************************************************
        xxx.xx.xxx.xx              : ok=6    changed=5    unreachable=0    failed=0

        Thursday 09 March 2017  22:11:17 +0800 (0:00:04.996)       0:05:22.075 ********
        ===============================================================================
        shadowsocks : Generate Shadowsocks config ----------------------------- 210.70s
        setup ------------------------------------------------------------------ 61.38s
        shadowsocks : Install shadowsocks-libev -------------------------------- 24.08s
        shadowsocks : Get Shadowsocks password --------------------------------- 12.18s
        shadowsocks : Generate Shadowsocks password ----------------------------- 8.72s
        shadowsocks : Restart shadowsocks-libev --------------------------------- 5.00s

    至此，梯子已备好，[配置客户端][6]开始 enjoy 吧。

[1]: https://github.com/shadowsocks/shadowsocks-libev/
[2]: https://linuxtoy.org/archives/selfhosted-server-1.html
[3]: https://linuxtoy.org/archives/selfhosted-server-2.html
[4]: https://linuxtoy.org/archives/selfhosted-server-3.html
[5]: https://github.com/xuxiaodong/selfhosted-server
[6]: https://shadowsocks.org/en/config/quick-guide.html
