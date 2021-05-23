import tweepy
import time

# KEYS
auth = tweepy.OAuthHandler('XUAGz64NEy6deSYf4eOrTEXs0','ujFaK0wnEQ8WWq7d4BH6A9WWYB4ORPynWDGHAnvYFCI5boxN9J')

auth.set_access_token('1356366441612599297-JTOlqpQIGIKJkI3UpP5jGEGiR9YNFc','5ql6FmYG6YIq9qe94PvRUO66sbKrD93jaKZcJWkxXJPrb')

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