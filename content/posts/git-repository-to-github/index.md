---
title: Setting Up a Git Repository for Pushing to GitHub
date: 2024-11-13T11:44:23+08:00
tags:
  - git
  - github
summary: A guide on initializing a Git repository in Linux with main as the default branch and securely pushing to GitHub using a Personal Access Token (PAT), ideal for those looking to streamline their Git setup.
slug: git-repository-to-github
description: This post provides a step-by-step guide for setting up a new Git repository with main as the initial branch and linking it to a GitHub repository without relying on the default origin label. It includes details on staging and committing files, pushing to a custom remote, and handling authentication with GitHub’s Personal Access Token (PAT) system. This streamlined approach helps ensure secure and efficient repository management on GitHub, making it easier to use common Git commands (push and pull) without needing to specify a remote every time.
ShowToc: true
TocOpen: true
---
When starting a new project, it's best practice to initialize the Git repository with `main` as the default branch (instead of the usual `master`). This post will walk you through how to set up your local repository, link it to a GitHub repository, and push your changes, including the setup for authentication using GitHub’s Personal Access Token (PAT).

### 1. Initialize a Git Repository with `main` as the Default Branch

Begin by navigating to the directory where your project is located. Run the following commands to initialize Git with the `main` branch directly.

```bash
cd /path/to/your/project
git init --initial-branch=main
```

### 2. Stage and Commit Your Files

Next, add all files to the staging area and commit them:

```bash
git add .
git commit -m "Initial commit"
```

### 3. Link Your Local Repository to GitHub

Now, set up a connection to your GitHub repository. Instead of using the default `origin` label for the remote, you can specify a custom label like `github`, which will allow flexibility with multiple remotes if needed.

```bash
git remote add github https://github.com/deuts/deuts.github.io.git
```

### 4. Push to GitHub without Using `origin`

For the first push, use the `-u` flag to set `github` as the default remote:

```bash
git pull github main --rebase
git push -u github main
```

After this initial push, you can use `git push` and `git pull` directly without specifying the remote every time, as Git will use `github` by default for this branch.

### 5. Authentication: When You'll Need Your Email and Personal Access Token (PAT)

When pushing to GitHub for the first time, Git will prompt you to set up authentication. Here’s what to expect:

- **Email**: If this is the first time using Git on your machine, Git will ask you to set your email and name:
  ```bash
  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"
  ```
  This is required for all commits, as GitHub associates your email with your GitHub account.

- **Personal Access Token (PAT)**: Instead of your GitHub password, Git now requires a PAT for authentication. When prompted to log in, enter your username and the PAT as the password.

  To create a PAT:
  1. Go to [GitHub’s PAT settings](https://github.com/settings/tokens).
  2. Generate a token with `repo` access.
  3. Use this token in place of your password when Git requests authentication.

### Common Commands Summary

- **Initialize a Git repository with `main`**:
  ```bash
  git init --initial-branch=main
  ```
- **Add and commit changes**:
  ```bash
  git add .
  git commit -m "Commit message"
  ```
- **Add a custom remote (`github`) and push**:
  ```bash
  git remote add github https://github.com/deuts/deuts.github.io.git
  git push -u github main
  ```
- **Push and pull with defaults**:
  ```bash
  git push    # no need for origin
  git pull    # no need for origin
  ```

With this setup, you'll be using the `main` branch, avoiding the default `origin` label, and ensuring secure access with GitHub’s Personal Access Token (PAT) system.