## Followers

1. Write a program to find out how many people a particular user follows?
2. For each of your followers, find out how many followers they have.
3. Make a "famous ratio" for a given user which I'll define as 'number of followers a person has divided by number of people they follow. Try out @makoshark, and @pontifex (the Pope). Who is higher?
4. [SKIPPED] Identify the follower you have that also follows the most of your followers.
5. [SKIPPED] How many users follow you but none of your followers?
6. [SKIPPED] Repeat these analyses for people you follow, rather than that follow you.
7. Identify the "famous ratio" for every one of your followers or friends? Who has the highest one?

## Topics and Trends

1. Modify twitter3.py to produce a list of 1000 tweets about a topic of your choice.
2. Look at those tweets. How does twitter interpret a two word query like "data science"
3. Do the previous step but eliminate retweets [hint: look at the tweet object!]
4. For each original tweet, list the number of times you see it retweeted.
5. Get a list of the URLs that are associated with your topic using Twitter.

## Geolocation

1. Alter the streaming code to include a "locations" filter. You need to use the order sw_lng, sw_lat, ne_lng, ne_lat for the four coordinates.
2. What are people tweeting about in Times Square today?
3. Set up a bounding box around TS and around NYC as a whole.
4. Do "static" (i.e., not using the streaming API) geolocation search using code like this:  d = api.search(geocode='37.781157,-122.398720,1mi')
