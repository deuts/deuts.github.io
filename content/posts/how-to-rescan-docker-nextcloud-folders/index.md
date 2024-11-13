---
title: How to Rescan Your Docker Nextcloud Folders
date: 2023-07-25T21:50:59+08:00
summary: Wait, where did my files go?
tags:
  - docker
  - nextcloud
slug: how-to-rescan-docker-nextcloud-folders
draft: false
description: If you can't see files or subfolders in Nextcloud after creating them or restoring from a backup, running the command docker exec -u www-data nextcloud_app php occ files:scan --all will fix the issue. This works for Nextcloud version 27.0.1 when installed via Docker.
---

What if:
- You installed Nextcloud via Docker
- You created files or subfolders in the Nextcloud folder of a user
  - This is also true if you're restoring files and folders from a backup
- You can't see the files or subfolders in the Nextcloud web interface

Just run the following command, replacing `nextcloud_app` with the actual container name of your Nextcloud Docker install: 


```
docker exec -u www-data nextcloud_app php occ files:scan --all
```

This is working for me, on Nextcloud version 27.0.1.
