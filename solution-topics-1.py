# Modify twitter3.py to produce a list of 1000 tweets about a topic of
# your choice.

# Note: I've changed it to search for "community data" instead of "data science."

import encoding_fix
import tweepy
from twitter_authentication import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import time

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# 100 is the maximum number taht can be returned according to:
# https://dev.twitter.com/rest/reference/get/search/tweets

counter = 0
for page in tweepy.Cursor(api.search, "community data", count=100).pages():
    counter = counter + len(page)
    for tweet in page:
        print(tweet.user.screen_name + "\t" + str(tweet.created_at) + "\t" + tweet.text)
    # end this loop if we've gotten 1000
    if counter == 1000:
        break

    # This page suggests we can do one request every 5 seconds:
    # https://dev.twitter.com/rest/reference/get/search/tweets
    time.sleep(5)

