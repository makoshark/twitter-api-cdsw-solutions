# For each original tweet, list the number of times you see it retweeted.

import encoding_fix
import tweepy
from twitter_authentication import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import time

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

counter = 0
for page in tweepy.Cursor(api.search, "community data", count=100).pages():
    counter = counter + len(page)
    for tweet in page:

        # urls seem to be stored in tweet.entities["urls"]
        for url in tweet.entities["urls"]:
            print(url["expanded_url"])
            
    # end this loop if we've gotten 1000
    if counter >= 1000:
        break

    # This page suggests we can do one request every 5 seconds:
    # https://dev.twitter.com/rest/reference/get/search/tweets
    time.sleep(5)
