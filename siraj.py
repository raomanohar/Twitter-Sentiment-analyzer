from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
import json
import re

ACCESS_TOKEN = "859108424-kXjc2uF9Q97O8oJlJswKJSyZK0jQAveXeg4NNjzs"
ACCESS_TOKEN_SECRET = "5mzmbOhsmT5Mshz7DBiSBCW3Qop9RuVztgsfe64Lqt8QQ"
CONSUMER_KEY = "LMTTQcPtYRvEFkBHXSNH53Ilp"
CONSUMER_SECRET = "RpJbJM7Z5LcXOZwdQYWka1j9l71WkpQS64LpV1BYiaNVYttNYI"

class StdOutListener(StreamListener):

    def clean_tweet(self, data):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", data).split())

    def on_data(self, data):
        #z = self.clean_tweet(data)
        #print(z)
        # print("___________")
        # print(type(data))
        y = json.loads(data,encoding='UTF-8')
        # print(type(y))
        # print("___________")
        try:
            y = y['extended_tweet']['full_text'] #.encode(encoding='UTF-8')
            #print(type(y))
            URLless_string = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', y)
            print(URLless_string)
        except KeyError:
            y = y['text']#.encode(encoding='UTF-8')
            #print(type(y))
            URLless_string = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', y)
            print(URLless_string)
            #except Exception as e:
                #print(e)

        return True

    def on_error(self,status):
        print(status)


if __name__ == "__main__":
    listener=StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    stream = Stream(auth, listener)
    stream.filter(track=['python'])
