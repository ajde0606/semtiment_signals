'''
Created on Dec 17, 2016

@author: Janice
'''
import nltk
import pandas as pd
import json


tweets_data_path = '../data/twitter_fed.txt'
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        if (tweet['lang'] != 'en'):
            continue
        tweets_data.append(tweet['text'])
    except:
        continue


#Structuring Tweets
#print 'Structuring Tweets\n'
#tweets = pd.DataFrame()
#tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
#tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
print tweets_data


