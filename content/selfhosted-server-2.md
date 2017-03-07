Title: 跟 Toy 玩自架服务器：创建 Linode 服务器实例
Date: 2017-03-06 21:28:51
Authors: toy
Category: Tutorials
Tags: selfhosted-server
Slug: selfhosted-server-2
Via: 

作为比较流行的 VPS 提供商，Linode 的费用曾经居高不下。感谢竞争，Linode
最近推出的入门款显得开始亲民了。笔者也正好借此机会作一番实际的体验。

<!-- PELICAN_END_SUMMARY -->

**准备工作**

除开笔者在上一篇所提的[基本工具][1]之外，你还需要准备下列东东：

1. PycURL 和 linode-python，这两个 Python 库用来和 Linode 的 API
   进行交互。你可以尝试通过所用 Linux
   发行版的包管理器安装，如果仓库中没有，那么可以通过 `pip` 安装：

        pip install pycurl linode-python

2. 登录 [Linode Manager][2]，点击 My Profile &rarr; API Keys 添加一个新的 API Key
   备用。要是你还没有 Linode 帐号，需要先[注册][3]。

    ![Linode API Key]({filename}/images/linode-key.png)

3. 确保你的 SSH 公钥 `/root/.ssh/id_rsa.pub` 存在。

**创建服务器**

1. 遵照上一篇文章克隆 [Selfhosted Server][4]。

2. 打开 `group_vars/local.yml`，定位到下列行：

        linode:
          id: 0
          datacenter_id: 11
          plan_id: 1
          distro_id: 140
          server_name: toynode

    简单解释一下各选项：

    + `id`：已创建服务器的 ID，暂时置为 0，等创建完了再填上。
    + `datacenter_id`：数据中心的位置，11 代表东京，其它区域可通过以下命令得到：
        
            curl -s 'https://api.linode.com/?api_key=<你的 API Key>&api_action=avail.datacenters' | jq .

    + `plan_id`：付费计划，这里是入门款。
    + `distro_id`：操作系统，当然是 Debian 8 64 位。
    + `server_name`：服务器名称，可以随意指定。

3. 打开 `site-linode.yml`，在第二个 roles 下建议保留以下 4 个，其余可全部注释掉。

        roles:
        - common
        - unattendedupgrades
        - fail2ban
        - git-client

4. 执行 `play-site.sh` 脚本：

        ┏━┓┏━╸╻  ┏━╸╻ ╻┏━┓┏━┓╺┳╸┏━╸╺┳┓   ┏━┓┏━╸┏━┓╻ ╻┏━╸┏━┓
        ┗━┓┣╸ ┃  ┣╸ ┣━┫┃ ┃┗━┓ ┃ ┣╸  ┃┃   ┗━┓┣╸ ┣┳┛┃┏┛┣╸ ┣┳┛
        ┗━┛┗━╸┗━╸╹  ╹ ╹┗━┛┗━┛ ╹ ┗━╸╺┻┛   ┗━┛┗━╸╹┗╸┗┛ ┗━╸╹┗╸

        Which provider are you using?
        1. DigitalOcean
        2. Linode
        3. Vultr
        Your choose (number): 

    按提示输入 2，然后输入 API Key，并按回车。等候执行完毕即可登录服务器开始使用。

    ![Linode Server]({filename}/images/linode-server.png)

[1]: https://linuxtoy.org/archives/selfhosted-server-1.html
[2]: https://manager.linode.com/
[3]: https://www.linode.com/?r=28bf53dae49d2c55dd671136769c0b7526db5891
[4]: https://github.com/xuxiaodong/selfhosted-server
