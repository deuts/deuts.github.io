---
title: Insert Shortcodes in Deuts Log
date: 2024-11-27T07:42:54+08:00 
tags: 
summary: 
description: Details on how to insert shortcodes in deuts.org
slug: insert-shortcodes
draft: false
ShowToc: true
TocOpen: true
type: page
menu: 
  footer:
    name: "Shortcodes"
    weight: 50
editPost:
  URL: "https://filepath.deuts.org/files/deutslog-site/staging/content"
  Text: "Edit" # edit text
  appendFilePath: true # to append file path to Edit link
---
## Insert a Youtube Video

{{< insertcode "youtube.txt" >}}

## Insert a Hugo Shortcode
{{< insertcode "insertcode.txt" >}}

You may use the `folder/file.txt`, and they should be located in the `assets` directory of your Hugo site.

## Add Comments in Markdown Files
{{< insertcode "comment.txt" >}}
Documentation: [Shortcodes#comment](https://gohugo.io/content-management/shortcodes/#comment)

## Insert Reference to another post
{{< insertcode "reflink.txt" >}}

Result: [Post 1]({{% ref "/posts/blood-vs-name/" %}})

## Insert a linkcard
{{< insertcode "linkcard.txt" >}}

## Insert callouts
{{< insertcode "callouts/info.txt" >}}
***
{{< insertcode "callouts/success.txt" >}}
***
{{< insertcode "callouts/error.txt" >}}
***
{{< insertcode "callouts/warning.txt" >}}
***
{{< insertcode "callouts/others.txt" >}}

## Insert an applink
{{< insertcode "applink.txt" >}}