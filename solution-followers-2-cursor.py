# For each of your followers, find out how many followers they have.

import encoding_fix
import tweepy
from twitter_authentication import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import time

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.get_user("makoshark")

# I found the list of functions in Tweepy here:
#   https://tweepy.readthedocs.org/en/v3.2.0/api.html

# I found the idea of how to the user the Cursor here:
#   https://tweepy.readthedocs.org/en/v3.2.0/cursor_tutorial.html

follower_ids = []
for page in tweepy.Cursor(api.followers_ids, screen_name="makoshark").pages():
    for follower in page:
        follower_ids.append(follower)


# the answer is using the api.lookup_users() code. unfortunately, this
# seems to only work with 100 users at a time. the following code makes that
# work
counter = 0
tmp_ids = []
users = []
for follower in follower_ids:
    tmp_ids.append(follower)
    counter = counter + 1

    # if we've hit 100, we grab data and then reset things and keep going
    if counter == 100:
        tmp_users = api.lookup_users(user_ids=tmp_ids)
        users = users + tmp_users

        counter = 0
        tmp_ids = []

# run once more when we're done
tmp_users = api.lookup_users(user_ids=tmp_ids)
users = users + tmp_users

# run through and print out the list of followers
for user in users:
    print("%s : %s" % (user.screen_name, user.followers_count))

          
