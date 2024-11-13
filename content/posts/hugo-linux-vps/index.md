---
title: How to install Hugo in a Linux VPS
date: 2023-08-12T10:43:30+08:00
tags:
  - hugo
  - linux
  - vps-hosting
  - debian
  - ubuntu
summary: Let me help you run Hugo on a Debian or Ubuntu Linux server.
slug: hugo-linux-vps
draft: false
description: This post explains how to install Hugo on Debian or Ubuntu. It covers installing an older version via APT, as well as installing the latest version from GitHub by downloading the .deb file, installing it, and ensuring the binary is properly copied to the /usr/bin/ directory. It also includes instructions for updating Hugo to the latest release.
---

## Via APT

If you're running Debian or Ubuntu on your VPS, you can actually easily install Hugo via: 

```bin
sudo apt install hugo
```

However, the version you can get from the repository is so old. Mine's around version 0.80 I think.

## Via Deb file from Github

### Download and Run

If you want the latest version of Hugo installed, you need to get it from [github](https://github.com/gohugoio/hugo/releases). As of this writing, the latest version is [v0.117.0](https://github.com/gohugoio/hugo/releases/tag/v0.117.0). Thus, you can run:

``` bash
wget https://github.com/gohugoio/hugo/releases/download/v0.117.0/hugo_extended_0.117.0_linux-amd64.deb
sudo dpkg -i hugo_extended_0.117.0_linux-amd64.deb
```

### Copy the Hugo file

By default, using the above method, hugo is saved under `/usr/local/bin`. You can verify that by running `which hugo` command. But this needs to be copied to the `/usr/bin` folder. Thus, run:

``` bash
sudo cp /usr/local/bin/hugo /usr/bin/
```

### Check version

You can double check if indeed you have the latest version by running:
```bash
hugo version
```

## Updating Hugo to the latest release

Redo all the installation instructions above including the `sudo cp /usr/local/bin/hugo /usr/bin/`  command.
