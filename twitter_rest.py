import requests
from requests_oauthlib import OAuth1
import sys,os
import ConfigParser 

#Reading credentials from config file
CC = ConfigParser.ConfigParser()
if not os.path.exists("keys.cfg"):
    print "Cannot find keys file"
    sys.exit(1)
CC.read("keys.cfg")
url_followers = CC.get("keys", "url_followers")
url_tweets = CC.get("keys", "url_tweets")
consumer_key = CC.get("keys", "consumer_key")
consumer_secret = CC.get("keys", "consumer_secret")
auth_token = CC.get("keys", "auth_token")
auth_token_secret = CC.get("keys", "auth_token_secret")

auth = OAuth1(consumer_key, consumer_secret, auth_token, auth_token_secret)

def get_followers(user_name):

	r = requests.get(url_followers +'screen_name= %s'%user_name, auth=auth)
	data = r.json()
	#returns all names of followers
	return data

def get_tweets(user_name):

	r = requests.get(url_tweets +'q=%s'%user_name, auth=auth)
	data = r.json()
	data = data['statuses']
	tweets = [i['text'] for i in data]
	#return all tweets
	return tweets

def common_followers(name_a,name_b):
	#calling get_follower to get all follower names
	user_a_data = get_followers(name_a)
	user_b_data = get_followers(name_b)
	user_a_data = user_a_data['users']
	user_b_data = user_b_data['users']

	user_a_followers = [i['screen_name'] for i in user_a_data]
	user_b_followers = [i['screen_name'] for i in user_b_data]
	#list of common followers 
	common_followers = list(set(user_b_followers).intersection(user_a_followers))
	#returning list of common followers
	return common_followers

def tweet_keyword(user_name,word):
	
	tweets = get_tweets(user_name)
	#list of tweets with word in it
	word_in_tweet = [i for i in tweets if word.lower() in i.lower()]
	return word_in_tweet

if len(sys.argv) != 4:
	print './<your-program> common-followers <username1> <username2>'
	print 'or'
	print './<your-program> tweet-keyword <username1> <string>'

elif sys.argv[1] == 'common-followers':
	#printing common_follwers 
	print common_followers(sys.argv[2],sys.argv[3])
	
elif sys.argv[1] == 'tweet-keyword':
	#printing tweet_keyword 
	print tweet_keyword(sys.argv[2],sys.argv[3])
else:
	print 'please check your arguments'
	
	