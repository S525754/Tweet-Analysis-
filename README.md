# Tweet-Analysis---Airline-Sentiment
This project analysis the dataset which has tweets from airlines customers on its service.
Customers will give either positive, negative or neutral feedback to the airline service. We would like to analyze these tweets for different airlines.
We will also analyse the following mapreduce problems
MapRedce Problem1:
What is the positive feedback percentage for the United Airlines?
MapRedce Problem2:
Which type of issues made customers give negative feedback and its values?
MapRedce Problem3:
Which airline has most negative feedback and which airline has most positive feedback?

Using the Tortoise SVN and GIT clone command you can pull the repository into your local system. Link is mentioned below.
https://github.com/S525754/Tweet-Analysis---Airline-Sentiment.git

How to execute the scripts in Pythonshell:
1) Run Mapper.py by using the command execfile('mapper.py')
2) Run reducer.py by using the following command execfile('reducer.py')


hadoop fs -put Tweets.CSV  This command will place the CSV file in HDFS
hs mapper.py reducer.py myinput joboutput  -> Will generate the output


