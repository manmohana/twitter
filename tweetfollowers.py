from twython import Twython
import ConfigParser,os,sys

#Reading credentials from config file
CC = ConfigParser.ConfigParser()
if not os.path.exists("keys.cfg"):
    print "Cannot find keys file"
    sys.exit(1)
CC.read("keys.cfg")
consumer_key = CC.get("keys", "consumer_key")
consumer_secret = CC.get("keys", "consumer_secret")
auth_token = CC.get("keys", "auth_token")
auth_token_secret = CC.get("keys", "auth_token_secret")

twitter = Twython(consumer_key, consumer_secret, auth_token, auth_token_secret)
class TwitterFollowers(object):

	def get_followers(self,user_name): 

		try:
			followers = twitter.get_followers_list(screen_name = user_name)
		except Exception as e:
			print e
			sys.exit(1)
		user = followers['users']
		follower_names = [i['screen_name'] for i in user]
		#returns all names of followers
		return follower_names

	def common_followers(self,user_a,user_b):
		

		#calling get_follower to get all follower names
		follower_names_a = self.get_followers(user_a)
		follower_names_b = self.get_followers(user_b)
		# inner join to get common followers
		followers = list(set(follower_names_a) & set(follower_names_b))
		#returning list of common followers
		return followers

class TwitterUserKeyword(object):
	
	def tweets(self,user_name):

		try:
			tweets=twitter.get_user_timeline(screen_name=user_name, count=100)
		except Exception as e:
			print e
			sys.exit(1)
		# returns 100 tweets
		return tweets
		

	def tweet_keyword(self,user_name,word):

		tweets = self.tweets(user_name)
		#list of tweets with word in it
		word_in_tweet = [i['text'] for i in tweets if word.lower() in i['text'].lower()]
		#returning all tweets where word in it.
		return word_in_tweet

if __name__ == '__main__':

	if len(sys.argv) != 4:
		print './<your-program> common-followers <username1> <username2>'
		print 'or'
		print './<your-program> tweet-keyword <username1> <string>'

	elif sys.argv[1] == 'common-followers':
		get = TwitterFollowers()
		#calling common_follwers function
		print get.common_followers(sys.argv[2],sys.argv[3])
		
	elif sys.argv[1] == 'tweet-keyword':
		get = TwitterUserKeyword()
		#calling tweet_keyword function
		print get.tweet_keyword(sys.argv[2],sys.argv[3])
	else:
		print 'please check your arguments'
		