# coding: utf-8
# test_pymongo.py
  
import pymongo
	   
con = pymongo.Connection('localhost', port=27017)
		   
		   
tweets = con.db.tweets
			   
import requests, json
				  
url = 'http://search.twitter.com/search.json?q=python&20pandas'
data = json.loads(requests.get(url).text)
	  
for tweet in data['results']:
	tweets.save(tweet)
	  
cursor = tweets.find({'from_user': 'wesmckinn'})
	    
tweet_fields = ['created_at', 'from_user', 'id', 'text']
result = DataFrame(list(cursor), columns=tweet_fields)


