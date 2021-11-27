import tweepy
from keys import *
import time




auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


mentions = api.mentions_timeline() # 1 Req
last_seen_mention = mentions[0].id # the purpose is to constantly query the latest mention



# constantly listen for new mentions
while True:

    print('Sending Request...')
    mentions = api.mentions_timeline(since_id = last_seen_mention)
    print('Request Sent...')


    print('Scanning Tweets...')
    for tweet in mentions: # Helloworld #helloWorld
        if tweet:
            if '#helloworld' in tweet.text.lower():
                print('Found #HelloWorld.')
                print('Replying Back...')
                api.update_status(f'@{tweet.user.screen_name} #HelloWorld back to you!', in_reply_to_status_id=tweet.id)
                print('Reply Send...')
            last_seen_mention = tweet.id
            
    print('Sleeping for 30 seconds....')
    time.sleep(30)


# USER OBJECTS
# TWEET OBJECTS


##################################
# Games ? --->> PUBG
# Designing ?
# Chess ?
# Coding ?
# Debugging ? 
##################################