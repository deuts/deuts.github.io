---
title: Implementing Basic Auth in Caddy
date: 2024-11-14T09:12:40+08:00
tags:
  - caddy
  - docker
  - security
  - authentication
summary: 
description: 
slug: caddy-basic-auth
draft: true
ShowToc: false
TocOpen: false
---
## Notes
### Why use?
- Basic auth is insecure because it sends credentials in a format that’s easy to decode if intercepted. However, using HTTPS adds a layer of encryption, making it suitable for simple cases, like staging sites, where high security isn’t critical.

### Your scenario
- You have Caddy Docker container with `caddy` as container name
- You have Nginx container with `nginx` as container name running on port `8080` in its container
- Both containers belong to the same Docker network
- You want to limit access to the Nginx service with HTTP basic authentication
### Simple Caddyfile
- As a starting point, let's say you have the following Caddyfile
```Caddyfile
example.com {
  reverse_proxy nginx:8080
}
```

