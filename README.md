# A Discord implementation of Buttbot
[Buttbot](https://code.google.com/archive/p/buttbot/) was an old IRC bot that replaces random nouns in a sentence with the noun "butt". This is a Discord version of the same idea. I couldn't figure out how to make [this](https://github.com/sct/buttbot-discord) one work so I made my own.

# Usage
## Installation
You'll need Python 3, and you'll have to install the necessary dependencies with `pip3 install -r requirements.txt`. Buttbot also uses a library called `nltk` which requires you to separately download datafiles (specifically, language analysis data in order to identify which words are nouns). To install these you can just run `python3 install.py`.

## Running
Put all the files as they are in some folder somewhere, then in that folder create a file called `config.yaml` with these contents:
```
token: <your discord bot token>
```
If you don't know what a discord bot token is, go find out. Then just run `python3 main.py`.

You can also run `python3 butt.py "This is a sentence"` to buttify sentences on the command line without actually running the bot.