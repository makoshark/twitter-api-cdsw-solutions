# Set up a bounding box around Times Square and around NYC as a whole.

# Alter the streaming code to include a "locations" filter. You need
# to use the order sw_lng, sw_lat, ne_lng, ne_lat for the four
# coordinates.

# Note: to answer this, I used this website to find a good box:
# http://boundingbox.klokantech.com/

import encoding_fix
import tweepy
from twitter_authentication import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

class StreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        print(tweet.author.screen_name + "\t" + tweet.text)

    def on_error(self, status_code):
        print('Error: ' + repr(status_code))
        return False

l = StreamListener()
streamer = tweepy.Stream(auth=auth, listener=l)

# This should grab tweets in Times Square /and/ NYC as a whole
streamer.filter(locations=[-73.9864799803,40.7575460197,-73.9837820197,40.7602439803,
                          -74.25909,40.477399,-73.700171,40.917577])

