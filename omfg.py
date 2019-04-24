import tweepy
from textblob import TextBlob

ACCESS_TOKEN = "REMOVED"
ACCESS_TOKEN_SECRET = "REMOVED"
CONSUMER_KEY = "REMOVED"
CONSUMER_SECRET = "REMOVED"

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
