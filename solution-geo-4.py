# Do "static" (i.e., not using the streaming API) geolocation search
# using code like this: d = api.search(geocode='37.781157,-122.398720,1mi')

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
for page in tweepy.Cursor(api.search, "party", geocode='37.781157,-122.398720,1mi',  count=100).pages():
    counter = counter + len(page)
    for tweet in page:
        print(tweet.user.screen_name + "\t" + str(tweet.created_at) + "\t" + tweet.text)
    # end this loop if we've gotten 1000
    if counter == 1000:
        break

    # This page suggests we can do one request every 5 seconds:
    # https://dev.twitter.com/rest/reference/get/search/tweets
    time.sleep(5)
