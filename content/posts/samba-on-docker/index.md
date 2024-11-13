---
title: Samba Docker or Native
date: 2024-03-16T17:41:18+08:00
tags:
  - docker
  - samba
  - selfhosted
summary: Many say Samba on Docker doesn't make sense. But does it?
slug: samba-on-docker
---

There is a 2-year old [thread](https://www.reddit.com/r/selfhosted/comments/t2x1fy/samba_server_docker_or_native/) on Reddit. Many in the comments say it doesn't make sense.

I've successfully implemented Samba natively in the past. The problem with native implementation is that you can take note of the procedures you've made to make it running, but when you need to reinstall your Linux OS or install in another box, you have to go through all [those procedures again](https://ubuntu.com/tutorials/install-and-configure-samba). With Docker, especially if you already have a working docker compose file, you just need to back up and/or carry over that yml file to the new box.

So here are the resources I will need to revisit in the future for a Docker implementation of Samba:
- [Crazy Max](https://github.com/crazy-max/docker-samba) - [docker compose file](https://github.com/crazy-max/docker-samba/blob/master/examples/compose/compose.yml)
- [ServerContainers Samba](https://github.com/ServerContainers/samba) - sample [docker compose file](https://github.com/ServerContainers/samba/blob/master/docker-compose.yml)
