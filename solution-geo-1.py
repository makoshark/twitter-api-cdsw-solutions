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

# This should grab tweets within Seattle:
streamer.filter(locations=[-122.459696, 47.481002, -122.224433, 47.734136])

