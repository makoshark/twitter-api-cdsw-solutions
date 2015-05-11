# For each of your followers, find out how many followers they have.

import encoding_fix
import tweepy
from twitter_authentication import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import time

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.get_user("makoshark")

for follower in user.followers():
    print("%s : %s" % (follower.screen_name, follower.followers_count))
    
    # According to this page, we can make 180 requests for user
    # information each 15 minute period or one every 5 seconds:
    #
    # https://dev.twitter.com/rest/reference/get/users/show
    time.sleep(5)
          
