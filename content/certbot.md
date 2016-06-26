Title: Certbot：自动部署 Let's Encrypt 证书
Date: 2016-05-13 14:41:10
Authors: toy
Category: Apps
Tags: tls, https
Slug: certbot
Via: Certbot|https://certbot.eff.org/

日前，电子前哨基金会（EFF）为 [Let's Encrypt][l] 推出了客户端 Certbot。通过 Certbot，你可以自动部署 Let's Encrypt 证书，以便为网站加上 HTTPS 支持。

<!-- PELICAN_END_SUMMARY -->

![certbot]({filename}/images/certbot.png)

**安装**

```
sudo apt-get install letsencrypt -t jessie-backports # Debian 8
sudo apt-get install letsencrypt                     # Debian testing/unstable, Ubuntu 16.04
wget https://dl.eff.org/certbot-auto                 # CentOS/RHEL 7
chmod a+x certbot-auto                               # CentOS/RHEL 7
```

**获得证书**

```
letsencrypt certonly  # Debian/Ubuntu
certbot-auto certonly # CentOS/RHEL
```

**自动续期**

将下列命令加入 `cron` 即可：

```
letsencrypt renew --quiet  # Debian/Ubuntu
certbot-auto renew --quiet # CentOS/RHEL
```

[l]: https://linuxtoy.org/archives/lets-encrypt.html
