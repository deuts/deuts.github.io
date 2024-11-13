---
title: How to Create a Bash Script and Make it Executable?
date: 2022-10-20T20:55:43+08:00
summary: Put long commands in a bash script so you don't have to remember them.
tags:
  - linux
slug: create-bash-script-executable
draft: false
---

## Long commands are hard to memorize

Let's say for example you want to run `hugo server`, but instead of on the localhost you want to run it over your VPS server (or even from your home server). Without the bash script, you'll need to run:

```shell
hugo server --bind=<IP ADDRESS> --baseURL=http://<IP ADDRESS>:1313
```

## Create a bash script

### Create the bash file

Let's name the bash file `serve.sh`

```bash
nano serve.sh
```

### Enter your commands

```bash
#!/bin/bash

hugo server --bind=<IP ADDRESS> --baseURL=http://<IP ADDRESS>:1313
```

Don't forget to include `#!/bin/bash` at the first line.

### Multiple Commands

If you need to make multiple commands, enter each command in separate lines, and end the file with `exec bash`, like for example:

```bash
#!/bin/bash
cd appdata/app/subfolder
PS1='$(whoami)@$(hostname):$(pwd)# '
exec bash
```

`Ctrl+O` to save the file  
`Ctrl+X` to close the file

## Make it executable

```shell
sudo chmod +x serve.sh
```

Enter password as may be necessary.

## Run the script

```shell
./serve.sh
```

Assuming we don't get into permission problems, our script should be working well.
