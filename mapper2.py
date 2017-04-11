#opening input file and output files
f = open("Tweets.csv","r")  
o = open("moutput2.txt", "w")
value = 1
#storing the input data based on comma seperated values
for line in f:  
    data = line.strip().split(",") 
    
    print len(data)
#Assigning data into variables if length is a valid value    
    if len(data) == 15:
        tweet_id, airline_sentiment, airline_sentiment_confidence, negativereason, negativereason_confidence, airline, airline_sentiment_gold, name, negativereason_gold, retweet_count, text, tweet_coord, tweet_created, tweet_location, user_timezone = data
        if  negativereason:
            print "{0}\t{1}".format(negativereason, value)
            o.write("{0}\t{1}\n".format(negativereason, value))
#Closing input and output files
f.close()
o.close()
