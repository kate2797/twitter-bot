from re import search
import tweepy
import time

from secrets import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Twitter authorisation
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
try:
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
except tweepy.TweepError:
    print('Error! Failed to get access token.')


def like_by_keywords(number_of_tweets, keywords):
    """ Likes tweets with specific keywords. """
    for keyword in keywords:
        for tweet in tweepy.Cursor(api.search, keyword).items(number_of_tweets):
            try:
                print("Liked!")
                tweet.favorite()
                time.sleep(3)
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break


like_by_keywords(20, ["100DaysOfCode", "CodeNewbie"])
