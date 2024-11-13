---
title: Streaming Movies and TV Shows on Kodi
date: 2022-10-21T21:28:50+08:00
summary: This may not work currently on my setup, but leaving it here anyway.
tags:
  - plex
  - tv-shows
  - vps-hosting
  - websites
  - kodi
  - emby
  - jellyfin
slug: streaming-movies-tv-shows-kodi
draft: false
description: You can set up Kodi to stream media from a VPS or local server using Apache or Nginx. See the video for details on adding remote media sources in Kodi.
---

When I started hoarding movies and TV shows back when streaming services were not yet a thing, of course I played them using VLC. But you can only do that on a computer. These media are better consumed over TV, right?

Then, the rise of Netflix showed us a glipmse of how your media should be better managed &mdash; with posters or thumbnails, description or summary, genre, casts list, and even related movies to watch after. I remember I used to have several hard drives with duplicate movies from several sources or several different versions and video codecs. Worse, it was so hard to keep track back then which movies you've already watched or what episode of a show did you last watch.

Then came Kodi. And you can sync your collection and watch status with Trakt. But Kodi was supposed to manage your local files only &mdash; or so I knew.

If you have a VPS or even a local server with your media files while running Apache or Nginx to serve webpages and/or files, you can actually add those folders as a media source to your Kodi app. The video below will show you how:

***
&nbsp;
{{< youtube yREBMpLC4QY >}}
&nbsp;
***

Of course, now there are media servers like Plex, Emby and Jellyfin to help you manage and stream your media files. But Kodi has a lot to offer over these other apps, and that's a totally different topic.

### FAQ
#### Will this work with HTTP Basic Authentication on Nginx server?
I actually have yet to try this out, and will update this post when I find out. But feel free to mention me [@deuts](https://twitter.com/deuts) if you know the answer.
