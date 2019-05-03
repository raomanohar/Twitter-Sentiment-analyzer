# Twitter-Sentiment-analyzer

Description

  Portuguese tweets are filtered on a track word ard streamed in realtime. The sentiment analysis of the tweet are done in three 
stages, If the polarity is more than 0 its considered as positive, if its equal to 0 its considered as Neutral and if its less than 
0 its considered as negative. 

The output is printed in this format
_____________________________________
**Portuguese Tweets **
** English Tweet **
** Sentiment of the tweet **
_____________________________________

I have used three pre built libraries for this project.
1. Tweepy
2. Googletrans
3. TextBlob

Tweepy

  Tweepy is an library used to stream live tweets using twitter API.
  
Googletrans
  
  Googletrans basically Works as google translator. Since I had to stream tweets in Portuguese I take the portuguese and
  convert it to English so that it is easier for Sentiment analysis.
  
TextBlob

  Is a library used to analyze the sentiment of the tweet which was translated from Portuguese to english using googletrans.

