Title: rm-protection：一个尽可能从根源防止误删的 rm 替代品
Date: 2017-02-04 15:22:04
Authors: Alan Chen
Category: Apps
Tags: 
Slug: rm-protection
Via: 

前几天在 YouTube 上目睹了 GitLab 的删库意外事件，突然想到一个主意：若是管理员当时能被问一句「你在删哪个数据库？」，恐怕这种事情也不会发生了吧。

<!-- PELICAN_END_SUMMARY --> 

![rm-p]({filename}/images/rm-p-logo.png)

rm-protection 就是这样一个轮子。它与原生 rm 完全兼容（事实上它会将参数原封不动地传递给 rm），唯一不同的是，它在执行 rm 前将检查你要删的每一个文件或者目录是否被「保护」。rm-protection 提供了一个命令 protect 来保护文件或者目录，通过这个命令你可以为一个文件或者目录设置一个安全问题与回答。

若是 GitLab 管理员提前将数据库目录保护起来，设置问题和回答为分别「你在删哪个数据库？」「生产」。当管理员回答「测试」时，就会自动中止并提示，防止酿成惨剧。

![rm-p]({filename}/images/rm-p.gif)

[源代码](https://github.com/alanzchen/rm-protection)已经在 GitHub 上了。程序也已经被打包到 PyPi。

与其他类似的轮子相比（比如各种 trash 类的，mv 类的），这个工具更能够保护特定的文件，而且将会从源头上解决问题。GitHub Readme 尾部提供了一个表格，对比其他轮子的特性。
