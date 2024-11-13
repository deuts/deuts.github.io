---
title: A few Nextcloud post-installation configurations
date: 2023-08-18T08:33:53+08:00
tags:
  - nextcloud
  - docker
summary: Get rid of several warnings in your Nextcloud admin dashboard.
slug: nextcloud-post-install-config
draft: false
description: Nextcloud installation via Docker may show warnings for service discovery and cron jobs. To fix the service discovery issue, update the .htaccess file. For cron jobs, set up a cron task on the host system to run cron.php every 5 minutes in the Nextcloud container.
---

After installing Nextcloud via [Docker](https://github.com/nextcloud/docker), and if you go to `/settings/admin/overview`, you might find some warnings that you need to do further configurations to get rid of.
***
## Service Discovery

> Your web server is not properly set up to resolve "/.well-known/caldav". 
> Your web server is not properly set up to resolve "/.well-known/carddav".

Go to the `app/` directory where you'll find the `.htaccess` file, and change the following lines:

```
  RewriteRule ^\.well-known/carddav /remote.php/dav/ [R=301,L]
  RewriteRule ^\.well-known/caldav /remote.php/dav/ [R=301,L]
```

To:

```
  RewriteRule ^\.well-known/carddav https://%{SERVER_NAME}/remote.php/dav/ [R=301,L]
  RewriteRule ^\.well-known/caldav https://%{SERVER_NAME}/remote.php/dav/ [R=301,L]
```

- [Source](https://github.com/nextcloud/docker/issues/528)

***
## Cron Jobs not working

You will need to setup a cron job from your host system. Try:

```bash
sudo crontab -e
```

Then add this line at the bottom:

```bash
*/5 * * * * docker exec -u www-data [containername] php /var/www/html/cron.php
```

Make sure to change `[containername]` to the actual name of your container.

- [Source](https://help.nextcloud.com/t/nextcloud-docker-container-best-way-to-run-cron-job/157734/4)
