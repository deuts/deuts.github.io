---
title: Building an Efficient Blogging Workflow with Hugo, Obsidian, and GitHub Pages
date: 2024-11-13T23:44:23+08:00
tags:
  - obsidian
  - hugo
  - github
  - git
  - blogging
  - wordpress
summary: After the recent WordPress community controversies, I've found myself leaning toward Hugo for blogging, primarily because of its performance, security, and simplicity. My workflow now revolves around Obsidian and Hugo, with minimal plugin dependency to keep the process reliable over time. While moving my existing WordPress content is complex, Hugo offers a forward-looking alternative for streamlined, self-hosted blogging.
slug: build-hugo-obsidian-github-pages-workflow
description: Exploring Hugo, Obsidian and Github Pages as a flexible and efficient blogging setup, focusing on low dependency and high control, with a look at potential WordPress migration challenges.
ShowToc: true
TocOpen: true
draft: false
---

Recent controversies surrounding Matt Mullenweg and WP Engine have led me to rethink my blogging platform. While WordPress has long been a popular CMS, I’m increasingly drawn to the simplicity and control of static site generators like Hugo.

### Why Consider Hugo Over WordPress?
Hugo’s performance and security benefits are difficult to ignore:

- **Performance**: Hugo serves static HTML files without any backend load, delivering high-speed access.
- **Security**: Without a database or PHP reliance, Hugo sites inherently avoid many vulnerabilities that affect WordPress.
- **Customization**: Total control over templates and layouts eliminates the plugin bloat that can slow down WordPress.
- **Version Control**: Working with Git keeps my changes organized and easy to revert if needed.
- **Low Maintenance**: No frequent updates or patches—Hugo just works as-is, saving time on upkeep.

Despite these advantages, I hesitated because managing content directly in Hugo, especially from the terminal, felt clunky compared to the WordPress dashboard. Using VS Code helped, but it was still missing that CMS simplicity.

### My New Workflow: Obsidian and Hugo with Minimal Dependencies
I've now found a balance that works without tying me to specific plugins that may become obsolete or unsupported. Here’s what my current workflow looks like:

1. **Obsidian with Templater and Dataview Plugins**:
   - I use Obsidian for creating and editing posts, keeping my Hugo directory aligned with my Obsidian vault. With Templater, I can build posts from templates and generate shortcodes. The Dataview plugin helps me get an overview of post summaries without impacting the publishing process.
   - Notably, I’ve chosen **not** to use plugins like [Hugo Publish or Static Site MD Exporter](/hugo-and-obsidian-workflow/). Relying on such plugins could cause future complications if they’re discontinued, so I’ve kept my setup as independent as possible.

2. **Building with Hugo**:
   - After editing posts, I use Hugo to generate HTML files, configured to output to a `docs` folder for simplicity.

3. **Publishing to GitHub Pages**:
   - Pushing my Hugo directory, including the `docs` folder, to GitHub triggers publishing through GitHub Pages. This approach enables a completely self-managed site without relying on an external CMS.
   - If I don’t have Obsidian access, I can still edit content through GitHub’s web interface, pull the changes, run Hugo to build, and push the updated site back.

4. **Direct Edit Links**:
   - For convenience, each site page includes a subtle edit button linking to the GitHub page source, making updates simple.

### Considering Migration
While I’m currently set on Hugo for future posts, the complexity involved in migrating [my WordPress content](https://deuts.net/) &mdash; nearly 900 posts and 2,500 comments &mdash; makes me pause. Migrating everything isn’t an easy task, so for now, I’m planning to blog on Hugo going forward while exploring efficient ways to gradually bring over my legacy content.

This workflow with Hugo, Obsidian and Github Pages has struck the right balance, letting me blog on my terms without depending on plugins or external services. Obsidian, Hugo, and GitHub all rely on Markdown, creating a seamless experience where these tools work in perfect harmony. For anyone seeking a lean, self-reliant approach to publishing, this setup might be the perfect fit.