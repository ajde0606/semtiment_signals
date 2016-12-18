'''
Created on Dec 18, 2016

@author: Janice
'''
import nltk
import pandas as pd
import json


#tweets_data_path = '../data/twitter_fed.txt.bak'
tweets_data_path = '../data/twitter_ube.txt'
tweets = []
tweets_file = open(tweets_data_path, "r")

for line in tweets_file:
    try:
        tweet = json.loads(line)
        if (tweet['lang'] != 'en'):
            continue
        #words=[]
        #for word in tweet['text'].split():
        #    words.append(word)
        tweets.append(tweet['text'])
        #tweets.append(words)
    except:
        continue
tweets_file.close()

print len(tweets)
print "Opening the file..."
filename = tweets_data_path+'.out'
f = open(filename, 'w')

for i in range(0,len(tweets)):
    f.write(str(i))
    f.write(": ")
    f.write(tweets[i].encode('utf-8'))
    f.write("\n")

f.close()

tweets_filtered=[]
for words in tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    words_filtered = [e for e in words_filtered if e[0] != '@' and e[0:5] != 'https']
    words_filtered = [e for e in words_filtered if e[0] != '#'] + [e[1:len(e)] for e in words_filtered if e[0] == '#']
    tweets_filtered.append(words_filtered)
    #print words
    #print words_filtered
    
tweets_training = tweets_filtered[:81]

def get_words_in_tweets(tweets):
    all_words = []
    for words in tweets_filtered:
        all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist=nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return wordlist

wordlist = get_word_features(get_words_in_tweets(tweets_filtered))
print wordlist.most_common(50)



