Title: 跟 Toy 玩自架服务器：创建 DigitalOcean Droplet
Date: 2017-03-08 19:50:19
Authors: toy
Category: Tutorials
Tags: selfhosted-server
Slug: selfhosted-server-3
Via: 

在笔者的印象中，DigitalOcean 貌似是最先以 SSD 作为存储介质的 VPS
提供商。如今，它已然成为全球第二大面向 Web
的主机公司。本篇笔者就来谈一谈如何创建 DigitalOcean 的 Droplet 吧。

<!-- PELICAN_END_SUMMARY -->

**准备工作**

1. 笔者在第一篇所提到的[主要工具][1]，你依然需要。

2. 因为我们通过 Python 与 DigitalOcean 的 API
   进行交互，所以在你的系统中还需要有 dopy 这个库：

        pip install dopy

3. 登录 [DigitalOcean 管理界面][2]，点击 API &rarr; Generate New Token
   来生成一个 API 访问 Token，并记录备用。如果你还没有 DigitalOcean
   帐号，那么要先[注册][3]一个。

    ![DigitalOcean API]({filename}/images/do-api.png)

4. 确认 SSH 公钥 `/root/.ssh/id_rsa.pub` 存在。

**创建 Droplet**

在 DigitalOcean 的语境中，服务器实例被称为 Droplet，下面就让我们来创建它：

1. 使用 Git 克隆 [Selfhosted Server][4]。

2. 打开 `group_vars/local.yml`，转到以下行：

        droplet:
          id: 0
          server_name: toyland
          ssh_key_name: toyland
          size_id: 512mb
          region_id: sgp1
          image_id: debian-8-x64

    各选项说明：

    + `id`：已创建 Droplet 的 ID，暂时设为 0，待创建完毕再补上。
    + `server_name`：Droplet 的名称，可任意指定。
    + `ssh_key_name`：SSH 公钥的名称。
    + `size_id`：内存大小，跟付费计划相关，此处为入门型。
    + `region_id`：数据中心位置，此处为新加坡。为了获得更佳的访问速度，你可能想要更改此位置，可通过如下命令获得其它区域：

            curl -X GET -H "Content-Type: application/json" -H "Authorization: Bearer <你的 API Token>" "https://api.digitalocean.com/v2/regions" | jq .

    + `image_id`：操作系统类型，此处为 Debian 8 64 位。

3. 打开 `site-do.yml`，定位到第二个 roles，暂时保留其下的 4
   个任务即可，其它可全部注释掉：

        roles:
        - common
        - unattendedupgrades
        - fail2ban
        - git-client

4. 执行：

        ./play-site.sh

    根据提示输入 1，然后再输入 API Token。待脚本执行完毕即可投入使用了。

    ![DigitalOcean Server]({filename}/images/do-server.png)

**一点比较**

经过对 Vultr、Linode、以及 DigitalOcean 的使用，笔者感觉在付费计划上，Vultr
显得更加灵活（他们甚至推出了 $2.5/月的沙箱计划）；以 $5/月为例，DigitalOcean
的配置明显要低一些（内存仍然为 512Mb）。网站的管理界面，Vultr 和 DigitalOcean
的设计看起来更加现代，而 Linode
就比较老土了。在数据中心位置方面，笔者目前主要使用东京和新加坡，感觉前者的访问速度要好于后者。

[1]: https://linuxtoy.org/archives/selfhosted-server-1.html
[2]: https://cloud.digitalocean.com/
[3]: https://m.do.co/c/7758457f61ad
[4]: https://github.com/xuxiaodong/selfhosted-server
