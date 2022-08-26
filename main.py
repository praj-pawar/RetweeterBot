import tweepy as twitter
import time, datetime


API_KEY = "TcBIaNyX4Y4kbdqN8fe1TxF3P"
API_SECRET_KEY = "ayDmV53D4kLKewfYJiDv3F1iN1HMeGbGFPbrZuwdvpOeb8f1e9"
ACCESS_TOKEN = "1563058515706802177-PgOee9SPuyPbuhf70mTiLcUv1kl6Fv"
SECRET_ACCESS_TOKEN = "3zl50tYyAy6nUOWOhrgGcucjHWhphtl9uCTKFcG9WThm2"


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