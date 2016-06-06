Title: gdict.sh: 最简单的中文字典
Date: 2010-04-24 09:13
Author: toy
Category: Apps
Tags: dict
Slug: gdict

感谢 big penguin 读者与我们分享他的 gdict.sh 脚本。该脚本允许你在 Linux 命令行下通过 Google 的 dictionary 服务来查英文单词。值得注意的是，你可能需要安装 curl 和 html2text。

<!-- PELICAN_END_SUMMARY -->

```
cat gdict.sh

code : --------------------------------------------------

#!/bin/bash  
# Command line Google's dictionary  
echo "----------------------------"  
echo ' '$1 | /usr/bin/curl -s -A 'Mozilla/4.0' 'http://www.google.com.hk/dictionary?aq=f&langpair=en|zh-CN&q='$1'&hl=en' \  
| html2text -ascii -nobs -style compact -width 1000 | sed -n -e '/^ /p'| sed '1,4d' | head -n -1  
#EOF

usage: --------------------------------------------------

gdict.sh apple
```
