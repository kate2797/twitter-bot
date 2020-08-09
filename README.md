# Twitter Bot

This Twitter bot likes 800 tweets a day under the following hashtags: **#100DaysOfCode** and **#CodeNewbie** to encourage people to continue sharing their programming journey online. The bots also tweets a funny/weird sentences that are coding-related.

# Prerequesities

- Python 3
- Tweepy
- random
- requests
- NLTK (The Natural Language Toolkit)

`pip install tweepy && pip install random && pip install requests && pip install nltk`

# How it works

The bot uses Tweepy to accomplish all of its functionalities – to find and like tweets containing certain hashtags and like them, to automatically follow back all users that follow the bot account and to publish tweets in the bots behalf.

To generate the funny tweet, I wrote several sentences with one word missing. This word is obtained from [Random word API](https://random-word-api.herokuapp.com/home) and then is semantically tagged (POS tagging) using the NLTK library which generates a label that corresponds to its part of speech. The word is then placed into sentences accordingly.

# Technologies

- Python
- Tweepy
- [Random word API](https://random-word-api.herokuapp.com/home)

# Inspiration for the funny tweets
