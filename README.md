linuxtoy.org
------------

这是 [LinuxTOY][l] 网站的源代码，原来采用 WordPress，现迁移到 Pelican，其中包括：

- content：所有文章，为 Markdown 格式
- themes：Pelican 主题
- plugins：Pelican 插件
- pelicanconf.py：Pelican 配置文件
- develop_server.sh：开发脚本
- Makefile：Make 构建脚本

## 如何使用

请参照 [Pelican 快速入门][p] 安装 Pelican。

## 新建文章

为了保持一致性，推荐使用 Markdown 格式，主要包括文章元数据和正文两个部分，例如：

    Title: (标题)
    Date: 2010-12-03 10:20 (创建日期)
    Modified: 2010-12-05 19:30 (修改日期)
    Category: Python (分类，只能使用单一分类)
    Tags: pelican, publishing (标签，多个以 , 分隔)
    Slug: my-super-post (slug，将用于 url，请与文件名保持一致)
    Authors: (作者，多个以 , 分隔)

    这是正文。

## 关于摘要

我们一般把文章第一段作为摘要，但 Pelican 的摘要功能只会将其显示在首页，而文章本身所在页面却并不显示。因此推荐使用以下方式来产生摘要，只需将其添加到第一段之后即可：

    <!-- PELICAN_END_SUMMARY -->

## 引用图像

将图像文件放入 `content/images` 目录之后，然后只需按如下方式引用即可：

    ![Title]({filename}/images/<image.png>)

由缩略图链接到大图：

    [![Title]({filename}/images/<image.thumb.png>)]({filename}/images/<image.png>)

将 `<image.png>` 和 `<image.thumb.png>` 替换成实际的图像文件名。

BTW：也可按此方式链接先前文章：

    [Article]({filename}/tmux.md)

## 添加代码

在撰文时，可对引用代码添加语法高亮显示，记法如下：

    A block of text. (正常文本)

        :::identifier (标识符，如 python)
        <code goes here> (具体的代码)

另外，也支持通过如下形式添加代码：

    ```identifier
    <code goes here>
    ```

## Vim 支持

若你使用 Vim 文本编辑器，那么可以在 .vimrc 中定义如下函数并绑定快捷键 `_ + m`，这样能够快速生成文章元数据：

```viml
"-- Markdown header --"
function! MarkdownHeader()
let date = strftime("%Y-%m-%d %T")
exe "normal iTitle: "
exe "normal oDate: " . date
exe "normal oAuthors: "
exe "normal oCategory: "
exe "normal oTags: "
exe "normal oSlug: "
exe "normal o"
endfunction

nmap _m :call MarkdownHeader()<cr>
```

## 欢迎贡献

我们是开放性网站，主要聚焦于 GNU/Linux 和开源，内容包括但不限于新闻、应用、以及提示诸方面，无论是来稿，抑或改善意见，我们都欢迎。

1. Fork 后，再发 Pull Request 即可。
2. 发邮件给我们作为会员加入。

## 版权许可

本网站文字及图片内容遵循“[署名-非商业性使用-相同方式共享 2.5 中国大陆][c]”的创作共用协议。

[l]: http://linuxtoy.org
[p]: http://docs.getpelican.com/en/3.5.0/quickstart.html
[c]: http://creativecommons.org/licenses/by-nc-sa/2.5/cn/
