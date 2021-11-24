import tweepy
from keys import *


# try to minimize the amount of request you send


auth = tweepy.OAuthHandler(API_KEY, API_SECRET) # your api access
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


api = tweepy.API(auth)
new_status = api.update_status('@aaqidmasoodi - #HelloWorld from Python! ')


