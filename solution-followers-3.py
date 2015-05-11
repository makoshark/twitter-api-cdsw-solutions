# Make a "famous ratio" for a given user which I'll define as 'number
# of followers a person has divided by number of people they
# follow. Try out @makoshark, and @pontifex (the Pope). Who is higher?

import encoding_fix
import tweepy
from twitter_authentication import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def famous_ratio(username):
    user = api.get_user(username)
    return(user.followers_count / user.friends_count)

print("mako: %s" % famous_ratio('makoshark'))
print("the pope: %s" % famous_ratio('pontifex'))

