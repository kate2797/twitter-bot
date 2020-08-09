from re import search
import tweepy
import time

from secrets import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Twitter authorisation
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Handle linking tweets based on multiple search terms
number_of_tweets = 10
terms_list = ["100DaysOfCode", "CodeNewbie",
              "codenewbie", "100daysofcode"]

for search_term in terms_list:
    for tweet in tweepy.Cursor(api.search, search_term).items(number_of_tweets):
        try:
            print("Liked!")
            tweet.favorite()
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
