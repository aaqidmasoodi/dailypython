import tweepy
from keys import *
import time

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

def save_last_status_id(id):
	with open('last_seen_id.txt', 'w') as f:
		f.write(str(id))

def get_last_status_id():
	with open('last_seen_id.txt', 'r') as f:
		status_id = int(f.read())

	return status_id

mentions = api.mentions_timeline()
last_mention_id = mentions[0].id

save_last_status_id(last_mention_id)

while True:
	print('Woke Up:')
	print('\tFetching mentions...')
	mentions = api.mentions_timeline(since_id=get_last_status_id())

	if mentions:
		for tweet in mentions:
			if '#helloworld' in tweet.text.lower():
				print(f'\tFound a tweet with #HelloWorld from @{tweet.user.screen_name}')
				print('\tReplying back...')
				reply = api.update_status(f'@{tweet.user.screen_name} #HelloWorld back to you', in_reply_to_status_id=tweet.id)
				print('\tSent.')
		save_last_status_id(tweet.id)

	else:
		print('\tNo new mentions.')

	print('Sleeping...')

	time.sleep(60)
