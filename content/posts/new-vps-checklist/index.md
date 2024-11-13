---
title: Checklist of things to do on a new VPS server
date: 2023-08-13T16:40:41+08:00
tags:
  - linux
  - vps-hosting
  - debian
  - ubuntu
  - portainer
  - duplicati
  - cloudflare
  - docker
summary: Got a new Ubuntu or Debian VPS server? Here are the things you should do to make the most out of it.
slug: new-vps-checklist
ShowToc: true
draft: false
---

## Update the system

From this moment, we'll assume you're still logged in as `root`. After all, this is a fresh install of Linux, right?

```bash
apt update
apt upgrade -y
```

## Install essential utilities
```bash
apt install sudo htop curl nano wget net-tools
```

## Change root password
This is just in case you don't think the assigned root password is not complex enough for your liking:
```bash
passwd
```
Then enter you new password twice.

## Update Timezone
```bash
dpkg-reconfigure tzdata
```

## Add non-root user
### Add user
Change `username` with the username of your choice:
```bash
adduser username
```

### Add user to sudoers group
```bash
usermod -aG sudo username
```

So, the non-root user is ready. From this moment on, we'll assume you're logged as that non-root user.

## Change the hostname

### Edit `/etc/hostname`
``` bash
sudo nano /etc/hostname
```
And change accordingly.

### Edit `/etc/hosts`
```bash
sudo nano /etc/hosts
```
And change accordingly.

### Reboot
```bash
sudo reboot
```

## Install Docker and Docker Compose

### Install Docker
Follow the instructions applicable for your system from the official Docker [documentation](https://docs.docker.com/engine/install/). My favorite systems are [Ubuntu](https://docs.docker.com/engine/install/ubuntu/) and [Debian](https://docs.docker.com/engine/install/debian/), and I actually prefer to use the [install using the repository](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository) method:

#### Set up Docker's Apt repository

##### For Ubuntu
```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

##### For Debian
```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

#### Install the Docker packages
```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Install Docker Compose
```bash
sudo apt install docker-compose
```

## Add user to the Docker group
- Check if docker group already exists: `grep docker /etc/group`
- Add user to the docker group: `usermod -aG docker username` (don't forget to change `username` to the username of your choice)

## Create a network bridge for Docker Containers
From now on, the instructions here is if you plan to expose your applications via Cloudflare Tunnel.

```bash
docker network create -d bridge cloudflared
```

## Install Cloudflare Tunnel
- Make a directory: `mkdir appdata/cloudflared` *(the directory structure is up to you)*
- CD to that directory: `cd appdata/cloudflared`
- Create the `docker-compose.yml` file: `nano docker-compose.yml`

Then paste the following:

```yml
version: "3.3"
services:
  tunnel:
    container_name: cloudflared-tunnel
    image: cloudflare/cloudflared
    restart: unless-stopped
    command: tunnel --no-autoupdate run
    environment:
      - TUNNEL_TOKEN=[paste_here_your_actual_token]
    networks:
      - cloudflared

networks:
  cloudflared:
    external: true
```

Don't forget to paste your actual token that will be generated when you create a new tunnel in Cloudflare.

## Install Portainer
### Via Docker Compose
Same as above, mkdir for portainer, then create the `docker-compose.yml` file:

``` yml
version: '3'

services:
  portainer:
    image: portainer/portainer-ce:latest
    container_name: portainer
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Asia/Manila
    restart: unless-stopped
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - ./data:/data
#    ports:
#      - 9000:9000
#      - 8000:8000
#      - 9443:9443
    networks:
      - cloudflared
networks:
    cloudflared:
      external: true
```

Note that I commented out the ports portion of the `docker-compose.yml` because we're not exposing the ports to the internet. Instead, we're using Cloudflare Tunnel to expose the apps.

## Install Duplicati
All these efforts you do to set up Docker containers will go to waste if you don't do a proper backup of your config and data files.

```yml
version: "2.1"
services:
  duplicati:
    image: lscr.io/linuxserver/duplicati:latest
    container_name: duplicati
    environment:
      - PUID=0
      - PGID=0
      - TZ=America/Denver
    volumes:
      - ./config:/config
      - ./backups:/backups
      - /home/username:/source
#    ports:
#      - 8200:8200
    restart: unless-stopped
    networks:
      - cloudflared

networks:
    cloudflared:
      external: true
```

I prefer to run Duplicati as root so I won't have to deal with read permission issues in the future, so I set `PUID` and `PGID` to `0`. Needless to say, you have to change your `TZ` and your `source folder` to map to the container.
