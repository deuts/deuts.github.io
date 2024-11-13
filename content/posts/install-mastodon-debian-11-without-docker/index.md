---
title: How to Install Mastodon on Debian 11 Without Docker
date: 2022-12-12T10:26:42+08:00
summary: This is how ChatGPT would install Mastodon on a bare metal VPS.
tags:
  - mastodon
  - debian
  - docker
  - chatgpt
slug: install-mastodon-debian-11-without-docker
---

With all the hype about ChatGPT nowadays, I really have to try it. And I'm still wondering how to install Mastodon on Debian 11 without Docker. And here's the AI's response:

## How to Install Mastodon on Debian 11 Without Docker (instructions generated from ChatGPT)

To install Mastodon, the open-source, decentralized social networking platform, on Debian 11 without using Docker, you can follow these steps:

1. First, make sure you have the necessary dependencies installed on your system. This includes PostgreSQL, Redis, and Yarn. You can install these using the following commands:
```
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
sudo apt-get install redis-server
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt-get update && sudo apt-get install yarn
```

2. Next, clone the Mastodon Git repository to your local machine using the following command:
```
git clone https://github.com/tootsuite/mastodon.git
```

3. Navigate to the Mastodon directory and install the necessary dependencies using Yarn:
```
cd mastodon
yarn install
```

4. Next, you will need to configure Mastodon by copying the .env.production.sample file to .env.production and editing it to set the appropriate values for your environment. This includes setting up your database, caching, and other options.

5. Once the configuration is complete, you can compile the Mastodon assets using the following command:
```
RAILS_ENV=production bundle exec rails assets:precompile
```

6. Finally, you can start the Mastodon server using the following command:
```
RAILS_ENV=production bundle exec rails s
```

Mastodon should now be running on your system. You can access it in your web browser at `http://localhost:3000`.

Note: The steps outlined above are a simplified version of the installation instructions for Mastodon. For more detailed instructions and additional options, please refer to the Mastodon documentation.

## I still have to try this
And I still have to try this soon. Will provide feedback if this instuction prove helpful.
