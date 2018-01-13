# Zeca
Zeca is a Discord bot for the [Portuguese Learning and Discussion](https://discord.gg/xMwmBZe) server.

## Creating a bot

1. Go to https://discordapp.com/developers/applications/me;
2. Click on New App;
3. Enter a name for your bot (and a description) and click on *Create App*;
4. Scrool down and click on *Create a Bot User*;
5. Click on *Save changes*.
6. Under *Bot* click on *click to reveal* to show your Token. Copy it and save it somewhere safe.\*

\* Don't let anyone see your token or they will be able to access your bot.


## Adding the bot to your server

1. On the same page click on *Generate OAuth2 URL*. Under *Bot Permissions* select *Administrator*.
2. Copy the link and paste it on your browser.
3. Select the server you want to join the bot and click on Authorize.

Your bot should now appear on your server.

## Installation

Download and install *Python 3.6*.

You'll need to install the following modules:

**discord** (*rewrite version*)\*

..```pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip```

\* The version on *pip* is not currently maintained

And for the module *dicinformal*:

**bs4 (BeautifulSoup)**

```pip install bs4```

**requests (http requests)**

```pip install requests```

In the file private.py insert the token you got for the bot you created.

## Current Goals

 - Implement a global check to make room for moderation tools.
 - Create a Utilities and a Moderation command category.
