# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tweepy as twitter
import time, datetime
print('my first line of code')

auth=twitter.OAuthHandler('VS3fREIKB89Y5xZGD8j53RZ4y', 'CVYUdsR0Z52olJjuKF1g0IaHgJtpbm904NO2fuKf6xRIv5n4NY')
auth.set_access_token('3220121588-mOR7ayIVPTfpA6CoIXjnFIZ7dOFK0SqSewMcLFi','KvqZ1FnD1md4LnT5bhXDoSB98wBEmAT2zLaQ7Y5CeQ5W4')

api=twitter.API(auth)

def twitter_bot(hashtag, delay):
    while True:
        print(datetime.datetime.now())
        
        for tweet in twitter.Cursor(api.search, q=hashtag, rpp=10).items(5):
            try:
                
                tweet_id = dict(tweet._json)["id"]
                tweet_text = dict(tweet._json)["text"]
            
                print("id: " + str(tweet_id))
                print("text: " + str(tweet_text))
            
                api.retweet(tweet_id)
                
            except twitter.TweepError as error:
                print(error.reason)
                
        time.sleep(delay)        
        
twitter_bot("#retweeter", 10)