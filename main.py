import tweepy as twitter
import time, datetime


API_KEY = ""
API_SECRET_KEY = ""
ACCESS_TOKEN = "-"
SECRET_ACCESS_TOKEN = ""


auth = twitter.OAuthHandler(API_KEY,API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN,SECRET_ACCESS_TOKEN)
api = twitter.API(auth)

def twitter_bot(hashtag,delay):
    while True:
        print(f"\n{datetime.datetime.now()}\n")

        for tweet in twitter.Cursor(api.search_tweets,q =  hashtag,rpp =10).items(5):
            try:
                tweet_id = dict(tweet._json)["id"]
                tweet_text = dict(tweet._json)["text"]
                print("id:  "+str(tweet_id))
                print("id:  "+str(tweet_id))

                api.retweet(tweet_id)

            except twitter.errors.TweepyException as error:
                 print(error)

        time.sleep(delay)


twitter_bot("#code",30)
