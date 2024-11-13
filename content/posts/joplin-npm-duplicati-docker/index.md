---
title: Make Joplin work with Nginx Proxy Manager and Duplicati (Docker)
date: 2022-10-24T22:03:23+08:00
summary: The ultimate way to install the Joplin server while using NPM and Docker.
tags:
  - joplin
  - vps-hosting
  - npm
  - duplicati
  - docker
  - linux
slug: joplin-npm-duplicati-docker
draft: false
---

I was wondering why Docker apps don't come as easy to install like [Linuxserver](https://www.linuxserver.io/)'s? Case in point: Joplin. 

Well, I really do think Joplin server's [documentation](https://github.com/laurent22/joplin/blob/dev/docker-compose.server.yml) needs a lot more polishing. Fortunately I was able to make it work in my system, even without exposing additional ports to the public, which I'm sharing below.

## Why Joplin Server instead of Webdav, Dropbox, OneDrive, NextCloud, etc.
According to [Noted](https://noted.lol/install-joplin-server-using-docker-compose/):
- Speed up the sync  
*I still have to find out if this really is true*
- Sharing a note with anyone, using a URL  
*This is actually my favorite feature. This enables me to share notes that are not so private to other people by just sharing a link to the public page. Then as I update my note, the page also updates.*
- User access  
*I still have to evangelize other people about Joplin so I could add users to my Joplin server, if ever they need a sync server.* 
- Sharing a notebook with a user on the same Joplin Server  
*This is also a great feature, especially if I have other users I can share my Joplin server with.*

## Docker Compose for Joplin Server
### Docker Network
Make sure that you already have a ready Docker Network for your Joplin app and database. This will make sure that you don't expose additional ports to the public. If you don't have a dedicated network yet, just run:
```bash
sudo docker network create -d bridge examplenetwork
```

### Nginx Proxy Manager
I would assume that you already have the Nginx Proxy Manager installed and it's running in the same `examplenetwork` . Now, add a new Proxy Host with your domain name, e.g. `joplin.example.com`, then hostname should be `joplin_app` (container name below) and port `22300`.

### Install Joplin App and DB

On your favorite directory, just create the `docker-compose.yml` file, which should contain:

```yml
version: '3'

services:
    db:
        image: postgres:13
        container_name: joplin_db
        volumes:
            - ./data/postgres:/var/lib/postgresql/data
#        ports:		we don't need this anymore because we're reverse proxying anyway
#            - "5432:5432"
        restart: unless-stopped
        environment:
            - POSTGRES_PASSWORD=yHZ4TbsyKJI0Xi2sUmXDuz
            - POSTGRES_USER=Barrier1542
            - POSTGRES_DB=Sudden9997
        networks:
            - examplenetwork
    app:
        image: joplin/server:latest
        depends_on:
            - db
        container_name: joplin_app
#        ports:		we don't need this anymore because we're reverse proxying anyway
#            - "22300:22300"
        restart: unless-stopped
        environment:
            - APP_PORT=22300
            - APP_BASE_URL=https://joplin.example.com
            - DB_CLIENT=pg
            - POSTGRES_PASSWORD=yHZ4TbsyKJI0Xi2sUmXDuz
            - POSTGRES_DATABASE=Sudden9997
            - POSTGRES_USER=Barrier1542
            - POSTGRES_PORT=5432
            - POSTGRES_HOST=db
        networks:
            - examplenetwork 

networks:
        examplenetwork:
            external: true
```

Don't worry about the usernames and passwords in my sample `docker-compose.yml` file, they were just randomly generated and not used for production elsewhere.

Then run `sudo docker-compose up -d`

Did you know that the Joplin docker image alone is worth 1.2GB of storage in your server? Postgres is another 373MB.

## Backup with Duplicati
As Joplin populates your `/data/postgres` folder in the initial setup, as well as along the way as you actually use your server, it creates files and directories with user and group permissions assigned to `systemd-coredump`. Worse, they are readable and writable by the user only. That is usually fine, until you try backing them up using Duplicati.

The solution: run your Duplicati docker app with root privileges. 

I know the rule about not running apps as root. But that's the only way I see so far that work. Perhaps, Joplin could give us an option to create and update files in the persistent volumes as a regular user. That way, I can run Duplicati as that same user and could access the files for backup.

## Update as of Mar. 24, 2024
For whatever reason, recently I noticed my Joplin server was down. The GUI is not accessible, and the sync process is not pushing though. Looked at the log, and it appears the Joplin app container is having trouble connecting to the Postgres database. 

In order to fix it, I needed to remove all the reference to the examplenetwork and uncomment all ports to make them active. Moreover, I needed to point directly the hostname in Nginx Proxy Manager (NPM) to the server's IP address.
```yml
version: '3'

services:
    db:
        image: postgres:13
        container_name: joplin_db
        volumes:
            - ./data/postgres:/var/lib/postgresql/data
        ports:
            - "5432:5432"
        restart: unless-stopped
        environment:
            - POSTGRES_PASSWORD=yHZ4TbsyKJI0Xi2sUmXDuz
            - POSTGRES_USER=Barrier1542
            - POSTGRES_DB=Sudden9997
    app:
        image: joplin/server:latest
        depends_on:
            - db
        container_name: joplin_app
        ports:
            - "22300:22300"
        restart: unless-stopped
        environment:
            - APP_PORT=22300
            - APP_BASE_URL=https://joplin.example.com
            - DB_CLIENT=pg
            - POSTGRES_PASSWORD=yHZ4TbsyKJI0Xi2sUmXDuz
            - POSTGRES_DATABASE=Sudden9997
            - POSTGRES_USER=Barrier1542
            - POSTGRES_PORT=5432
            - POSTGRES_HOST=db
```
