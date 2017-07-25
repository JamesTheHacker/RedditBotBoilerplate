# Reddit Bot Boilerplate

This is a simple boilerplate that uses [praw](praw.readthedocs.io) to create a Reddit bot. I've only recently started getting into Reddit bot development so expect this boilerplate to improve over time.


## Uses:

* praw: Reddit API
* argparse: Command line arguments

## Configuration

Modify `praq.ini` with your credentials:

    [bot1]
    client_id=
    client_secret=
    password=
    username=
    user_agent=

If you want to use multiple accounts with the bot add a new section like so:

    [bot2]
    client_id=
    client_secret=
    password=
    username=
    user_agent=

To select which configuration to use with the bot simple pass the bot name to the script like so:

    bot.py -b 'bot2'

