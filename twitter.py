import tweepy
import time
from os import environ

# KEYS

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

# AUTH

auth = tweepy.OAuthHandler(CONSUMER_KEY , CONSUMER_SECRET)

auth.set_access_token(ACCESS_KEY , ACCESS_SECRET)

# auth and set bot to sleep when reach the max twitter actions permitted

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()


# show followers names
# for follower in tweepy.Cursor(api.followers).items():
#    print(follower.name)

search = '#100DaysOfCode'
nrTweets = 10

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Retweeted')
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)    
    except StopIteration:    
        break