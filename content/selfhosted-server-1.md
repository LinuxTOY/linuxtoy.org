Title: 跟 Toy 玩自架服务器：创建 Vultr 服务器实例
Date: 2017-03-05 18:09:25
Authors: toy
Category: Tutorials
Tags: selfhosted-server
Slug: selfhosted-server-1
Via: 

回想笔者初次建站还是 2004 年那会儿，花 120 元 1
年在网易购买了空间。不过使用起来实在受限得很，只能通过 FTP 上传一些 HTML
静态页面。眼下，云主机层出不穷，拥有一台个人 VPS 也并非什么难事。如果你对想要拿
VPS 来干什么毫无头绪的话，那么不妨跟随笔者的脚步一起来玩一玩自架服务器。

<!-- PELICAN_END_SUMMARY -->

玩过 VPS
的同学想必都有和笔者类似的切身感受，那就是虽然架好的服务看起来很美好，但却是反复折腾的结果。这个过程不仅费时费力，而且更是对自己功力和耐心的考验。感谢
Puppet、Ansible、SaltStack、Docker
等新一代工具的兴起，使像架设服务这类对普通人而言比较困难的事情也变得更加容易了。

笔者在此不会论及如何选一台趁手好用的
VPS，这个主题已经有很多同学探讨过了。你若对此感兴趣，不妨查一查相关的资料。在这个文章系列中，笔者将以
Vultr、Linode、DigitalOcean 这三家 VPS 提供商作为例子加以说明。

**准备工作**

在开始之前，我们需要事先准备好下列事项：

1. Git：用来从 GitHub 克隆源代码仓库。
2. Ansible：笔者用来自动化服务器架设的首选工具，如果在你的系统中还没有它，那么可以参考笔者曾经撰写的《[Ansible 快速上手][1]》一文。
3. 登录 Vultr，点击 Account &rarr; API，生成一个新的 Personal Access
   Token，并记录备用。若你还没有 Vultr 帐号，那[注册][2]先。

    ![Vultr API]({filename}/images/vultr-api.png)

4. 点击 Servers &rarr; SSH Keys，添加你的 SSH 公钥，并记录 SSH Key ID（URL 中
   SSHKEYID= 后面的部分）。如果你还没有 SSH
   公钥，那么可以参考相关文档[生成][3]一个。

    ![Vultr SSH Key]({filename}/images/vultr-ssh.png)

**创建服务器实例**

现在万事已经俱备，只等我们撸起袖子开干了。

1. 克隆笔者编写的 Selfhosted Server：

        git clone --recursive https://github.com/xuxiaodong/selfhosted-server.git

2. 配置服务器，打开 `group_vars/local.yml` 文件，转到以下行：

        vultr:
            dc_id: 25
            plan_id: 201
            distro_id: 193
            ssh_key_id: 58b917dc1b55b
            server_name: toydroid

    其中，各选项作用如下：

    + `dc_id`：数据中心所处的位置，此处为东京。
    + `plan_id`：付费计划，此处为 $5/月。
    + `distro_id`：要用的操作系统，此处为 Debian 8 64 位版本。
    + `ssh_key_id`：SSH 公钥，替换成你自己的。
    + `server_name`：服务器名称，替换成你自己的。

    你可能会想要更改数据中心位置或付费计划，那么如何查询它的 ID
    呢？使用以下命令即可：

        # 获取数据中心位置
        curl -H 'API-Key: <你的 API 访问 Token>' https://api.vultr.com/v1/regions/list
        # 获取付费计划
        curl -H 'API-Key: <你的 API 访问 Token>' https://api.vultr.com/v1/plans/list

3. 选择执行的任务，打开 `site-vultr.yml` 文件，转到下列行：

        roles:
        - common
        - unattendedupgrades
        - fail2ban
        - git-client

    在服务器实例被创建以后，你可以酌情选择要执行的任务。推荐保留上述四个，这将安装常用的
    htop、git、fail2ban 等工具，并对系统进行一些调优。

4. 执行以下脚本，并按提示输入 3，接着再输入 API Token：

        ./play-site.sh

    等候脚本执行完毕（[参考输出][4]），登录 Vultr，你应当可以看到服务器实例已经创建好了。

    ![Vultr Server]({filename}/images/vultr-server.png)

[1]: https://linuxtoy.org/archives/hands-on-with-ansible.html
[2]: http://www.vultr.com/?ref=7123175
[3]: https://www.vultr.com/docs/how-do-i-generate-ssh-keys/
[4]: https://paste.unixkoans.com/view/c6b6ec48
