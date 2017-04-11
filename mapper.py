f = open("Tweets.csv","r")  
o = open("moutput.txt", "w") 
for line in f:  
    data = line.strip().split(",") 
      
    if len(data) == 15:
        tweet_id, airline_sentiment, airline_sentiment_confidence, negativereason, negativereason_confidence, airline, airline_sentiment_gold, name, negativereason_gold, retweet_count, text, tweet_coord, tweet_created, tweet_location, user_timezone = data
        print "{0}\t{1}".format(airline, airline_sentiment)
        if airline = "United":
            o.write("{0},{1}\n".format(airline, airline_sentiment))
f.close()
o.close()
