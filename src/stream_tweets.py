import os
import tweepy
import queue
import threading
import json

TWEET_QUEUE = queue.Queue()

def on_status(status):
    if hasattr(status, 'text'):
        TWEET_QUEUE.put(status.text)

def stream_tweets():
    api_key = os.getenv('TWITTER_API_KEY')
    api_secret = os.getenv('TWITTER_API_SECRET')
    access_token = os.getenv('TWITTER_ACCESS_TOKEN')
    access_secret = os.getenv('TWITTER_ACCESS_SECRET')

    auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
    stream_listener = tweepy.StreamListener()
    stream_listener.on_status = on_status
    stream = tweepy.Stream(auth=auth, listener=stream_listener)
    stream.filter(track=['AI', 'Big Data', 'Machine Learning'], languages=['en'])

if __name__ == "__main__":
    threading.Thread(target=stream_tweets).start()