import tweepy
from textblob import TextBlob

ACCESS_TOKEN = "859108424-kXjc2uF9Q97O8oJlJswKJSyZK0jQAveXeg4NNjzs"
ACCESS_TOKEN_SECRET = "5mzmbOhsmT5Mshz7DBiSBCW3Qop9RuVztgsfe64Lqt8QQ"
CONSUMER_KEY = "LMTTQcPtYRvEFkBHXSNH53Ilp"
CONSUMER_SECRET = "RpJbJM7Z5LcXOZwdQYWka1j9l71WkpQS64LpV1BYiaNVYttNYI"

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
API = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print("--------------------")
        print(status.text)
        analysis = TextBlob(status.text)

        if analysis.sentiment.polarity > 0:
            print("sentiment is positiv")
        elif analysis.sentiment.polarity == 0:
            print("sentiment is Neutral")
        else:
            print("sentiment is Negative")
        print("--------------------\n")

    def on_error(self, status):
        print(status)


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = API.auth, listener=myStreamListener, tweet_mode='extended', lang='pt')

myStream.filter(track=['python'])
