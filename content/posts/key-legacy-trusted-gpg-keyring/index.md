---
title: Key Is Stored in Legacy Trusted.gpg Keyring
date: 2023-08-09T08:21:31+08:00
summary: How to get rid of this deprecation error in Ubuntu or Debian?
tags:
  - linux
  - ubuntu
  - debian
slug: key-legacy-trusted-gpg-keyring
draft: false
description: This post addresses the issue of legacy keyrings on fresh installs of Debian or Ubuntu, where an error message warns about keys stored in the deprecated trusted.gpg keyring. The solution is to copy the keyring to the trusted.gpg.d directory and update the system using sudo apt update.
---

Have you ever encountered issues with legacy keyrings when running a fresh install of Debian or Ubuntu?

> W: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details

### The Quick Fix

```bash
cd /etc/apt
sudo cp trusted.gpg trusted.gpg.d
sudo apt update
```

More info can be read [here](https://stackoverflow.com/questions/73570418/w-key-is-stored-in-legacy-trusted-gpg-keyring-etc-apt-trusted-gpg-see-the-d).
