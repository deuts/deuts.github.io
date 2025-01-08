---
title: Create a new post in Deuts Log
date: 2024-11-15T10:42:54+08:00 
tags: 
summary: 
description: Details on how to create new posts in deuts.org
slug: create-new-post
draft: false
ShowToc: true
TocOpen: true
type: page
menu: 
  footer:
    name: "New Post"
    weight: 52
editPost:
  URL: "https://filepath.deuts.org/files/deutslog-site/staging/content"
  Text: "Edit" # edit text
  appendFilePath: true # to append file path to Edit link
---
## Create folder and index.md file
- Create a new folder in [content/posts](https://filepath.deuts.org/files/deutslog-site/content/posts/)
- Under the newly created folder, create an `index.md` file

## Enter the Frontmatter
```yml
---
title: Draft Title for Staging # edit this as may be necessary
date: 2024-11-15T10:42:54+08:00 # edit this as may be necessary
tags:
  - github # add your tags here
summary: 
description: 
slug: staging-draft # edit this as may be necessary
ShowToc: false
TocOpen: false
draft: true
---
```
## Enter your content
You know what to do here.

## Check the post in staging
- In the terminal:
```bash
cd /home/deuts/deutslog/site
hugo -e staging
```
- Check the new post at [Deuts Log Staging](https://staging.deuts.org)
- When you're satisfied, you're ready to move to the next step

## Publish your post
- Edit the frontmatter, set `draft: false`
- In the terminal, run:
```bash
cd /home/deuts/deutslog/site
hugo
git add .
git commit -m "new post"
git push
```
- Wait for the pages to deploy to Github, then  check the post at [Deuts Log](https://deuts.org)

## Insert Shortcodes
[Insert Shortcodes]({{% ref "/staging/insert-shortcodes.md" %}})