#!/usr/bin/env python
# coding: utf-8

import codecs
import datetime
import feedparser

rss_url = 'http://linuxtoy.disqus.com/latest.rss'
disqus = feedparser.parse(rss_url)

html_header = """
<!DOCTYPE html>
<html lang="zh">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Comments</title>
        <link rel="stylesheet" href="https://linuxtoy.org/theme/css/main.css">
        <link rel="stylesheet" href="https://linuxtoy.org/theme/css/calluna.css">
        <!--[if lte IE 8]>
        <link rel="stylesheet" href="https://linuxtoy.org/theme/css/grids-responsive-old-ie-min.css">
        <link rel="stylesheet" href="https://linuxtoy.org/theme/css/side-menu-old-ie.css">
        <![endif]-->
        <!--[if gt IE 8]><!-->
        <link rel="stylesheet" href="https://linuxtoy.org/theme/css/grids-responsive-min.css">
        <link rel="stylesheet" href="https://linuxtoy.org/theme/css/side-menu.css">
        <!--<![endif]-->
        <link rel="stylesheet" href="https://linuxtoy.org/theme/css/pygments.css">
        <link rel="shortcut icon" type="image/x-icon" href="https://linuxtoy.org/favicon.ico">
        <link rel="alternate" type="application/atom+xml" href="https://linuxtoy.org/feeds/all.atom.xml" title="LinuxTOY Atom Feed">
        <!--[if IE]>
        <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
        <![endif]-->
    </head>
    <body>
        <div id="layout" class="pure-g">
            <div class="sidebar pure-u-1 pure-u-md-1-5">
                <div class="header">
                    <a id="menuLink" class="menu-link" href="#menu">
                        <span></span>
                    </a>

                    <div id="menu">
                        <div class="pure-menu">
                            <a class="pure-menu-heading" href="https://linuxtoy.org/" title="LinuxTOY">
                                LinuxTOY
                            </a>

                            <ul class="pure-menu-list">
                                <li class="pure-menu-item">
                                    <a class="pure-menu-link" href="https://linuxtoy.org/pages/all-archives.html" title="Archives">
                                        Archives
                                    </a>
                                </li>
                                <li class="pure-menu-item">
                                    <a class="pure-menu-link" href="https://linuxtoy.org/pages/all-archives.html" title="Books">
                                        Books
                                    </a>
                                </li>
                                <li class="pure-menu-item">
                                    <a class="pure-menu-link" href="https://linuxtoy.org/pages/all-archives.html" title="Talks">
                                        Talks
                                    </a>
                                </li>
                                <li class="pure-menu-item">
                                    <a class="pure-menu-link" href="https://linuxtoy.org/pages/download.html" title="Download">
                                        Download
                                    </a>
                                </li>
                                <li class="pure-menu-item">
                                    <a class="pure-menu-link" href="https://linuxtoy.org/pages/faq.html" title="FAQs">
                                        FAQs
                                    </a>
                                </li>
                                <li class="pure-menu-item">
                                    <a class="pure-menu-link" href="https://linuxtoy.org/pages/contact.html" title="Contact">
                                        Contact
                                    </a>
                                </li>
                                <li class="pure-menu-item">
                                    <a class="pure-menu-link" href="https://linuxtoy.org/pages/donate.html" title="Donate">
                                        Donate
                                    </a>
                                </li>
                                <li class="pure-menu-item">
                                    <a class="pure-menu-link" href="https://linuxtoy.org/pages/license.html" title="License">
                                        License
                                    </a>
                                </li>
                                <li class="pure-menu-item">
                                    <a class="pure-menu-link" href="https://linuxtoy.org/pages/links.html" title="Links">
                                        Links
                                    </a>
                                </li>

                                <li class="pure-menu-item pure-menu-selected">
                                    <a class="pure-menu-link" href="https://linuxtoy.org/pages/comments.html" title="Comments">
                                        Comments
                                    </a>
                                </li>
                                <li class="pure-menu-item">
                                    <a class="pure-menu-link" href="https://linuxtoy.org/random.html" title="Comments">
                                        Random
                                    </a>
                                </li>
                                <li class="pure-menu-item">
                                    <a class="pure-menu-link" href="https://linuxtoy.org/feeds/all.atom.xml" title="RSS">
                                        RSS
                                    </a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

<div class="content pure-u-1 pure-u-md-4-5">
    <div class="posts">
        <section class="post">
            <header class="post-header">
                <h2 class="post-title">Comments</h2>
            </header>
            <div class="post-description">
"""

html_footer = """
            </div>
        </section>
    </div>
</div>
        </div>

        <script src="https://linuxtoy.org/theme/js/zepto.min.js"></script>
        <script src="https://linuxtoy.org/theme/js/ui.js"></script>
        <script>
            Zepto(function($){
                $('table').addClass('pure-table pure-table-bordered');
            });
        </script>
<script type="text/javascript">
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-349050-2']);
    _gaq.push(['_trackPageview']);
    (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
</script>
<script type="text/javascript">
    (function(w,d,t,u,n,s,e){w['SwiftypeObject']=n;w[n]=w[n]||function(){
    (w[n].q=w[n].q||[]).push(arguments);};s=d.createElement(t);
    e=d.getElementsByTagName(t)[0];s.async=1;s.src=u;e.parentNode.insertBefore(s,e);
    })(window,document,'script','//s.swiftypecdn.com/install/v2/st.js','_st');

    _st('install','zWjtxRdA6ciZ7LBm4R4K','2.0.0');
</script>
    </body>
</html>
"""

with codecs.open('/var/www/linuxtoy.org/pages/comments.html', mode='w', encoding='utf-8') as f:
    f.write(html_header)
    for item in disqus.entries:
        dt = datetime.datetime(*item.published_parsed[:7]) + datetime.timedelta(hours=12)
        date_srt = dt.strftime("%Y/%m/%d %H:%M:%S")
        title = item.title.replace(u' \xb7 LinuxTOY', '')
        f.write('<p><a href="%s">@%s</a> %s &raquo; %s</p>\n' % (item.link,
            item.author, title, date_srt))
        f.write('%s\n' % item.summary)
    f.write(html_footer)
