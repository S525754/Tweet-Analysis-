f = open("Tweets.csv","r")  # open file, read-only
o = open("mOutput.txt", "w") # open file, write-only
for line in f:  
    data = line.strip().split(",") # Split the input data based on ',' seperated
    print data
    print len(data)
    if len(data) == 15: # assign data
        tweet_id, airline_sentiment, airline_sentiment_confidence, negativereason, negativereason_confidence, airline, airline_sentiment_gold, name, negativereason_gold, retweet_count, text, tweet_coord, tweet_created, tweet_location, user_timezone = data  
        o.write("{0}\t{1}\n".format(airline, airline_sentiment))
f.close() # Closing file1
o.close() # CLosing outputfile
