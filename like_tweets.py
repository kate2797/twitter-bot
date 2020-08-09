from re import search
import tweepy
import time

from secrets import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Handle linking tweets based on search term
search_list = ["100DaysOfCode", "CodeNewbie"]
search_term1, search_term2 = search_list
number_of_tweets = 100

for tweet in tweepy.Cursor(api.search, search_term1).items(number_of_tweets):
    try:
        print("Liked!")
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search_term2).items(number_of_tweets):
    try:
        print("Liked!")
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
