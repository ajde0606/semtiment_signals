#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os
key_word = os.environ['KEY_WORD']

#Variables that contains the user credentials to access Twitter API 
access_token = "809054374559358978-Hjd34SbKBMlUfPOOZ4uuzHAdwJqwQsC"
access_token_secret = "C2vSxITMKG2MRGKxV0zYlkyNC53ySmI8nzCzdM6tWgJmD"
consumer_key = "2ksUt2cGCVTukSnwnqp1FbZAk"
consumer_secret = "fMUfHnyX52572giO3ZAy4dSfipyknbIYSRS2bW3LWxJEig6MSl"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
  def on_data(self, data):
    print data
    return True

def on_error(self, status):
  print status


if __name__ == '__main__':
  #This handles Twitter authetification and the connection to Twitter Streaming API
  l = StdOutListener()
  auth = OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  stream = Stream(auth, l)
  stream.filter(track=[key_word])

