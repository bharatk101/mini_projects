import tweepy
from textblob import TextBlob

consumer_key = 'Nc6ssdZQ69zjGVGK84mIZWjvZ'
consumer_secret = 'DIcT5z3oJJn8WNoM6hzarfGpf0OJCf8sjvi2rl0CbV2Olr6Ks4'

access_token = '598291615-lPyQPc8xfg2kOlWnoqZL0bNPEy5enV4uPLuMEvMm'
access_token_secret = 'XPBegGny2CbCnOIiWOTn9PKMRpbzdgsc9I1CuQmIo1tHu'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Pewdiepie')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
