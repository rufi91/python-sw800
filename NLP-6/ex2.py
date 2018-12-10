"""
3. Take tweets from FIFACom or one of your choice and display 10 tweets.
4. Modify the above program and Classify if each tweet is Positive, Negative , Neutral.
5. Modify the above program and give a count of Positive , Negative and Neutral Tweets
"""

import tweepy
from textblob import TextBlob



consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
c_pos=0
c_neg=0
c_neu=0
count=0
public_tweets = api.user_timeline("@FIFAcom",count=10)

for tweet in public_tweets:
    t1=TextBlob(tweet.text)
    count+=1
    print "===================Tweet #%d======================\n"%count,t1, ": "
    if t1.sentiment.polarity>0:
        print "Positivie Tweet\n"
        c_pos+=1
    elif t1.sentiment.polarity<0:
        print "Negative Tweet\n"
        c_neg+=1
    elif t1.sentiment.polarity==0:
        print "Neutral Tweet\n"
        c_neu+=1

print "Total tweet sentiment count: \n","Positive: ",c_pos,"Negative: ",c_neg,"Neutral: ", c_neu

