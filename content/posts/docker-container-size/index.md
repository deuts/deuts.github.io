---
title: Docker Command to Check the Sizes of your Containers
date: 2023-08-12T08:07:49+08:00
tags:
  - docker
summary: Which image occupies my VPS storage the most?
slug: docker-container-size
---

## Quickly

The easy approach is to use:

```bin
docker ps --size
```

But this will output a long table with columns:
- Container ID
- Image
- Command
- Created
- Status
- Ports
- Names
- Size

### Let's refine the command

More likely, you're just curious about these columns:
- Container ID
- Names
- Image
- Size

In order to do so, just run:

```bin
docker ps -a --size --format "table {{.ID}}\t{{.Names}}\t{{.Image}}\t{{.Size}}"
```

- [Source](https://code2care.org/docker/check-size-of-docker-container)
