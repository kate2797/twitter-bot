from re import search
import tweepy
import time

from secrets import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Twitter authorisation
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
try:
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
except tweepy.TweepError:
    print('Error! Failed to get access token.')


def get_friends():
    """ Gets list of all followers. """
    return [friend.screen_name for friend in api.friends()]


def follow_back():
    """ Follows back all users that followed the bot. """
    for follower in tweepy.Cursor(api.followers).items():
        if follower.screen_name not in get_friends():
            try:
                follower.follow()
                print(f"Followed {follower.screen_name} back!")
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break


follow_back()
