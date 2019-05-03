
# coding: utf-8

# In[28]:


import tweepy
from textblob import TextBlob
from googletrans import Translator

ACCESS_TOKEN = "859108424-kXjc2uF9Q97O8oJlJswKJSyZK0jQAveXeg4NNjzs"
ACCESS_TOKEN_SECRET = "5mzmbOhsmT5Mshz7DBiSBCW3Qop9RuVztgsfe64Lqt8QQ"
CONSUMER_KEY = "LMTTQcPtYRvEFkBHXSNH53Ilp"
CONSUMER_SECRET = "RpJbJM7Z5LcXOZwdQYWka1j9l71WkpQS64LpV1BYiaNVYttNYI"

## Creating a Translatop object
translator = Translator()

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):

        print("--------------------")
        try:
            m = status.extended_tweet["full_text"]
            m = ''.join(c for c in m if c <= '\uFFFF') #Removes Emojies for the googletrans API to work"""

            translations = translator.translate(m, dest='en')
            print('\033[1m{:10s}\033[0m'.format('Tweet in Portuguese \n'), translations.origin, "\n")
            print('\033[1m{:10s}\033[0m'.format("Tweet translated to English \n"),  translations.text)
            z = translations.text
                        
        except AttributeError:
            m = status.text
            m = ''.join(c for c in m if c <= '\uFFFF') #Removes Emojies for the googletrans API to work"""

            translations = translator.translate(m, dest='en')
            print('\033[1m{:10s}\033[0m'.format('Tweet in Portuguese \n'), translations.origin, "\n")
            print('\033[1m{:10s}\033[0m'.format("Tweet translated to English \n"),  translations.text)
            z = translations.text


        analysis = TextBlob(z)

        if analysis.sentiment.polarity > 0:
            print('\033[92m{:10s}\033[0m'.format("Sentiment of the tweet is Positiv"))
        elif analysis.sentiment.polarity == 0:
            print('\033[93m{:10s}\033[0m'.format("Sentiment of the tweet is Neutral"))
        else:
            print('\033[91m{:10s}\033[0m'.format("Sentiment of the tweet is Negative"))
        print("--------------------\n")

    def on_error(self, status):
        print(status)

if __name__ == "__main__":

    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    API = tweepy.API(auth)

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = API.auth, listener=myStreamListener, tweet_mode='extended')

    myStream.filter(track=['Avengers'],languages=['pt'])

