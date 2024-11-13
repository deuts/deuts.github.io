---
title: Hugo and Obsidian workflow
date: 2024-11-12T21:44:50+08:00
tags:
  - obsidian
  - hugo
  - linux
summary: A guide on how to use Obsidian in conjunction with Hugo for a
  streamlined blogging workflow, highlighting the issues with existing Obsidian
  plugins and their impact on Hugo builds.
description: This post highlights issues with Obsidian plugins like Hugo Publish
  and Static Site MD Exporter when used in a Hugo blogging workflow.
slug: hugo-and-obsidian-workflow
---

When combining Obsidian with Hugo for a streamlined blogging workflow, several plugins claim to offer an easy publishing process, but some fall short due to misalignment with Hugo’s expectations. In this post, I’ll highlight some common issues with the plugins I’ve encountered.

## The Problem with Available Obsidian Plugins

### [Hugo Publish](https://github.com/kirito41dd/obsidian-hugo-publish)

One plugin that attempts to bridge the gap between Obsidian and Hugo is **Hugo Publish**. This plugin lets you assign tags to notes, which it then processes into Markdown files that can be used with Hugo. However, there's a significant flaw: if you assign a `blog` tag to your notes for processing, the plugin carries this tag over to the output `.md` files. This means that every post, when built with Hugo, will include the `blog` tag, which is not only redundant but goes against the purpose of using tags as categories or topics.

The problem here is that **Hugo Publish** does not account for the need to handle tags dynamically for each post. In Hugo, tags are often used for grouping and categorization, and repeating the same tag across all posts diminishes their value.

### [Static Site MD Exporter](https://github.com/yy4382/obsidian-static-site-export)

Another plugin, **Static Site MD Exporter**, offers a different approach by publishing the processed `.md` files directly to GitHub. From there, you can use `git pull` to bring them into your Hugo project and build the site.

This plugin offers a useful feature: by adding `published: true` in the frontmatter of a note, it marks the note for processing and publishing. However, this is where things start to break down when using Hugo. The `published` property is actually an alias for `publishDate` in Hugo, which expects a date value, not a boolean. As a result, when you run the `hugo` build command, Hugo throws an error because it cannot interpret `published: true` correctly.

---

## Summary

Both the **Hugo Publish** and **Static Site MD Exporter** plugins offer valuable functionality, but they fall short in handling tags and frontmatter properties according to Hugo’s conventions. The inability of these plugins to properly manage `publishDate` and `tags` leads to errors when building the Hugo site and creates unnecessary redundancy in post tags. These are important issues that need to be addressed in order for the workflow to function smoothly with Hugo.
