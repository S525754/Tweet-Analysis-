f = open("Tweets.csv","r")  
o = open("moutput2.txt", "w") 
for line in f:  
    data = line.strip().split(",") 
    print data
    print len(data)
    if len(data) == 15:
		value = 1
        tweet_id, airline_sentiment, airline_sentiment_confidence, negativereason, negativereason_confidence, airline, airline_sentiment_gold, name, negativereason_gold, retweet_count, text, tweet_coord, tweet_created, tweet_location, user_timezone = data
        print "{0}\t{1}".format(negativereason, value)
        o.write("{0}\t{1}\n".format(negativereason, value))
f.close()
o.close()
