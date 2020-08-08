import tweepy
import time

from secrets import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
api = tweepy.API(auth)

api.update_status("Hello Tweepy")
