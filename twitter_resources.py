import os
from dotenv import load_dotenv
import tweepy
import time
import pandas as pd

load_dotenv()
consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def get_tweets(city, resource):
    query = "verified {} {} -not verified -un verified -urgent -unverified -needed -required -need -needs".format(city, resource)
    count = 15

    try:
        tweets = api.search(q = query,count = count, tweet_mode = 'extended')

        #tweets_list = [[tweet.created_at, tweet.id, tweet.full_text] for tweet in tweets]
        #tweets_df = pd.DataFrame(tweets_list)
        tweets_list=[]
        for tweet in tweets:
            if 'retweeted_status' in tweet._json:
                tweets_list.append([tweet.id_str, tweet.user.name, tweet.user.screen_name, tweet._json['retweeted_status']['full_text']])
            else:
                tweets_list.append([tweet.id_str, tweet.user.name, tweet.user.screen_name, tweet.full_text])
    except BaseException as e:
        print("failed", str(e))
        time.sleep(3)

    return tweets_list
    
# url: https://twitter.com/twitter/statuses/+status_id
    #print(tweets_df)
    

