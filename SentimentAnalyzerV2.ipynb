import tweepy
from textblob import TextBlob
from googletrans import Translator
import csv
import matplotlib.pyplot as plt 
import pandas as pd

ACCESS_TOKEN = "859108424-kXjc2uF9Q97O8oJlJswKJSyZK0jQAveXeg4NNjzs"
ACCESS_TOKEN_SECRET = "5mzmbOhsmT5Mshz7DBiSBCW3Qop9RuVztgsfe64Lqt8QQ"
CONSUMER_KEY = "LMTTQcPtYRvEFkBHXSNH53Ilp"
CONSUMER_SECRET = "RpJbJM7Z5LcXOZwdQYWka1j9l71WkpQS64LpV1BYiaNVYttNYI"

## Creating a Translatop object
translator = Translator()
# Creating a DF to store the data

df = pd.DataFrame()

plt.ion()

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):

        print("--------------------")
        try:
            m = status.extended_tweet["full_text"]
            m = ''.join(c for c in m if c <= '\uFFFF') #Removes Emojies for the googletrans API to work

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
        global df
        if analysis.sentiment.polarity > 0:
            print('\033[92m{:10s}\033[0m'.format("Sentiment of the tweet is Positiv"))
            data = pd.DataFrame({"Tweets_in_Portuguese": [translations.origin],"Tweets_in_English": [translations.text], "Sentiment_Of_Tweet": 'Positiv'})
            df= df.append(data)

        elif analysis.sentiment.polarity == 0:
            print('\033[93m{:10s}\033[0m'.format("Sentiment of the tweet is Neutral"))
            data = pd.DataFrame({"Tweets_in_Portuguese": [translations.origin],"Tweets_in_English": [translations.text], "Sentiment_Of_Tweet": 'Neutral'})
            df = df.append(data)

        else:
            print('\033[91m{:10s}\033[0m'.format("Sentiment of the tweet is Negative"))
            data = pd.DataFrame({"Tweets_in_Portuguese": [translations.origin],"Tweets_in_English": [translations.text], "Sentiment_Of_Tweet": 'Negative'})
            df = df.append(data)

        print("--------------------\n")

        df.to_csv(r'Tweet_data.csv', index = None, header=True)

#Plotting the Sentiment
        #Sentiment_Data = pd.Series(df['Sentiment_Of_Tweet']).value_counts()
        CountStatus = pd.value_counts(df['Sentiment_Of_Tweet'].values, sort=True)
        CountStatus.plot.bar()
        #plt.barh(Sentiment_Data)
        plt.title('Sentiment of tweets which has Avengers word in it')
        plt.draw()
        plt.pause(0.1)
    

    def on_error(self, status):
        print(status)

if __name__ == "__main__":

    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    API = tweepy.API(auth)

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = API.auth, listener=myStreamListener, tweet_mode='extended')
    plt.show(block=True)
    #df.to_csv (r'Tweet_data.csv', index = None, header=True)
    myStream.filter(track=['Avengers'],languages=['pt'])
    
