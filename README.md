# Twitter Bot

## General info
To encourage people to continue sharing their programming journey online, I developed a Twitter bot that likes 400 tweets a day under the following hashtags: #100DaysOfCode and #CodeNewbie. The bot also tweets coding-related jokes that are meant to be funny. I leave the latter to your judgement 😂.

The bot uses Tweepy to accomplish all its features. 1) To find tweets with certain hashtags and like them. 2) Automatically follow back all users that follow the bot's account. 3) Publish funny tweets on the bot's behalf. These features are scheduled using AWS Lambda's CloudWatch Events to repeat daily. 

To generate a funny tweet, I wrote several sentences with one word missing. The missing word is obtained from [Random word API](https://random-word-api.herokuapp.com/home) and then semantically tagged (i.e., POS tagging) using the NLTK library, which generates a label corresponding to its part of speech. This word is then placed into the sentences, accordingly, obeying the rules of semantics.

## Technologies
- Python 3
- Tweepy
- random
- requests
- NLTK (Natural Language Toolkit)
- AWS Lambda

## Preview
<img src="IMG_0237.jpeg" alt="Twitter timeline" width="30%" height="30%"/>
Click <a href="https://twitter.com/bitemybot">here</a> to see this project in your browser.

## Setup
`pip install tweepy && pip install random && pip install requests && pip install nltk`

## Inspiration
- [Programmer puns](https://punstoppable.com/Programmer-puns)
- [Programming jokes](http://www.devtopics.com/best-programming-jokes/)
