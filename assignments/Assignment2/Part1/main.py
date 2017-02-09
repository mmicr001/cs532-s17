#! /usr/bin/python

import tweepy_testing as tt

dd = tt.collectTheTweets(50)
tt.saveTweets(dd,'tweets')
tweets = tt.loadTweets('tweets')
links = tt.extractLinksFromTweets(tweets)
finalURIs = tt.getAllTheFinalURI(links)
tt.saveUris(finalURIs, 'Lin_1000')
