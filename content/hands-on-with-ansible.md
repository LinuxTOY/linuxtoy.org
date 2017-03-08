Title: Ansible 快速上手
Date: 2013-11-01 14:12
Author: toy
Category: Tutorials
Tags: Ansible
Slug: hands-on-with-ansible

最近纠结于在 [Puppet][p]、[Chef][c]、[SaltStack][s]、[Ansible][a] 等一干配置管理工具中如何选择。考虑到一旦开始没有选好，以后更改又是一堆麻烦事，所以就稍微有些慎重。

<!-- PELICAN_END_SUMMARY -->

Puppet 和 SaltStack 我曾用过，但不是十分符合预期，所以先行排除。至于 Chef，虽然老早就听说过，但却一直没有找到机会尝试。翻了翻文档，Chef 跟 Puppet 及 SaltStack 也是一样采用服务端/客户端模式，对于在现有一定数量的机器上部署仍然有  些麻烦。最后落单到 Ansible 上。经过对 Ansible 的把玩，我感觉 Ansible 于我比较相投。我喜欢 Ansible 的方面包括：

* 充分利用现有设施。使用 Ansible 无需安装服务端和客户端，只要 SSH 即可。这意味着，任何一台装有 Ansible 的机器都可以成为强大的管理端。我觉得，这种去中心化的思路显得更为灵活。可能有人会担心 SSH 的效率，Ansible 的并行执行及加速模式或许可以打消你的顾虑。  
* 使用简单，快速上手相当容易。我在用 Puppet 之前，就没少花时间钻研它。想想吧，我们使用这类自动化管理工具不就是想把自己从重复的、复杂的事情中解放出来么？为了简化一件事，而沉入另一件复杂的事，是不是有些不划算？从我的体验来看，Ansible 上手十分快，用 Ad-Hoc 可以应付简单的管理任务，麻烦点的也可以定义 Playbook 文件来搞定。  
* 采用人类易读的格式。Ansible 的主机定义文件使用 INI 格式，支持分组，能够指定模式；此外也能动态生成，这对管理云主机应当很有用。而 Playbook 则是 YAML 格式，我觉得它比 Puppet 的 DSL 要易读易写多了。  
* 能够使用你熟悉的语言来编写模块。虽然 Ansible 是使用 Python 开发的，但它不会将你限制到某种具体的编程语言，Bash、Python、Perl、Ruby 等等都可以，你擅长什么就用什么。

一言以蔽之，Ansible 背后的简单化哲学深得我心。这也比较符合我选择软件的一贯原则。可能还有人会比较关心目前 Ansible 都有谁在用。毕竟，榜样的力量是无穷。Puppet 不正是因为 Google 在用而吸引了不少眼球么？据我所知，当前使用 Ansible 较为知名的用户包括 Fedora、Rackspace、Evernote 等等。

**安装 Ansible**

Ansible 能够安装到 Linux、BSD、Mac OS X 等平台，Python 版本最低要求为 2.6。常用 Linux 发行一般可以通过其自带的包管理器[安装 Ansible][i]：

    yum install ansible     # RHEL/CentOS/Fedora，需要配置 EPEL
    apt-get install ansible # Debian/Ubuntu
    emerge -avt ansible     # Gentoo/Funtoo

如果你在所用 Linux 发行版的包仓库中找不到 Ansible，那么也可以通过 `pip` 来安装 Ansible，同时也会安装 paramiko、PyYAML、jinja2 等 Python 依赖库。

    pip install ansible

**准备 Inventory**

Inventory 文件用来定义你要管理的主机。其默认位置在 `/etc/ansible/hosts` ，如果不保存在默认位置，也可通过 `-i` 选项指定。被管理的机器可以通过其 IP 或域名指定。未分组的机器需保留在 hosts 的顶部，分组可以使用 `[]` 指定，如：

    [web]  
    linuxtoy.org

同时，分组也能嵌套：

    [vps:children]  
    web  
    db

此外，也可以通过数字和字母模式来指定一系列连续主机，如：

    [1:3].linuxtoy.org # 等价于
    1.linuxtoy.org、2.linuxtoy.org、3.linuxtoy.org  
    [a:c].linuxtoy.org # 等价于
    a.linuxtoy.org、b.linuxtoy.org、c.linuxtoy.org

**小试牛刀**

现在，我们执行以下命令来看看 Ansible 是否能正常工作：

    ansible -i hosts all -m ping -u www

该命令选项的作用分别为：

* `-i`：指定 inventory 文件，使用当前目录下的 hosts  
* `all`：针对 hosts 定义的所有主机执行，这里也可以指定组名或模式  
* `-m`：指定所用的模块，我们使用 Ansible 内置的 ping 模块来检查能否正常管理远端机器  
* `-u`：指定远端机器的用户

如果返回如下结果：

    linuxtoy.org | success >> {  
    "changed": false,  
    "ping": "pong"  
    }

则说明一切正常。

下面我们再看看远端机器的 uptime：

    ansible vps -a 'uptime'

这将输出：

    linuxtoy.org | success | rc=0 >>  
    11:23:16 up 177 days, 21:19, 0 users, load average: 0.55, 0.45, 0.39

此处我们省略了 `-m`，Ansible 默认使用 command 模块；`-a` 指定模块的参数，即执行 `uptime` 命令。

**使用 Ad-Hoc 管理简单任务**

执行 Ad-Hoc 就跟我们在 Linux 下执行单行命令差不多，用来快速完成简单的任务十分方便。比如：如果被管理端的 Python 为 2.4，那么需要 python-simplejson 这个包。我们可以通过以下命令在所有 CentOS 主机上安装它：

    ansible all -m raw -a 'yum -y install python-simplejson'

花时间看看 [Ansible 的模块][m]非常值得，你将明白它能干什么。创建用户及组、安装软件包、分发配置文件、管理服务等等不一而足。在命令行下，可通过 `ansible-doc` 查询模块文档，如：

    ansible-doc raw

**使用 Playbook 管理复杂任务**

对于需反复执行的、较为复杂的任务，我们可以通过定义 Playbook 来搞定。Playbook 是 Ansible 真正强大的地方，它允许使用变量、条件、循环、以及模板，也能通过角色及包含指令来重用既有内容。我们来看一个简单的例子，该例子在远端机器上创建一个新的用户：

    ---  
    - name: create user  
    hosts: vps  
    user: root  
    gather_facts: false

    vars:  
    - user: "toy"

    tasks:  
    - name: create {{ user }} on vps  
    user: name="{{ user }}"

首先，我们给 Playbook 指定了一个名称；接着，通过 `hosts` 让该 Playbook 仅作用于 vps 组；`user` 指定以 root 帐号执行，Ansible 也支持普通用户以 `sudo` 方式执行；`gather\_facts` 的作用是搜集远端机器的相关信息，稍后可通过变量形式在 Playbook 中使用；`vars` 定义变量，也可单独放在文件中；`tasks` 指定要执行的任务。

要执行 Playbook，可以敲入：

    ansible-playbook user.yml

执行结果为：

    PLAY [create user] ************************************************************

    TASK: [create toy on vps] *****************************************************  
    changed: [linuxtoy.org]

    PLAY RECAP ********************************************************************  
    linuxtoy.org : ok=1 changed=1 unreachable=0 failed=0

关于 Playbook 的详细用法，推荐阅读 Ansible 的[官方文档][d]，并参考[官方示例][e]。

**总结**

Ansible 由 Puppet 的前雇员所创建，使用起来真的很简单。不仅仅是配置管理，远程执行、应用部署等任务皆能完成，而且便于利用自身所熟悉的语言扩展，确为不可多得的好工具。

[p]: http://linuxtoy.org/archives/puppet.html  
[c]: http://www.opscode.com/chef/  
[s]: http://linuxtoy.org/archives/saltstack.html  
[a]: http://www.ansible.com/  
[i]: http://www.ansible.com/docs/intro_installation.html  
[m]: http://www.ansible.com/docs/modules.html  
[d]: http://www.ansible.com/docs/#playbooks  
[e]: https://github.com/ansible/ansible-examples
