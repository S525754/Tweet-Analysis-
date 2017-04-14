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
Solution:
We have provided all the airlines with positive and negative feedback details. 

Using the Tortoise SVN and GIT clone command you can pull the repository into your local system. Link is mentioned below.
https://github.com/S525754/Tweet-Analysis---Airline-Sentiment.git

How to execute the scripts in Pythonshell:
We need to keep input file in the project folder for all three mapreduce problems. We can execute python scripts with the following commands. 
Map reduce problem1:
1) Run Mapper.py by using the following command --> execfile('mapper.py')
2) Run reducer.py by using the following command --> execfile('reducer.py')

Map reduce problem2:
1) Run Mapper2.py by using the following command --> execfile('mapper2.py')
2) Run reducer2.py by using the following command --> execfile('reducer2.py')

Map reduce problem3:
1) Run Mapper3.py by using the following command --> execfile('mapper3.py')
2) Run reducer3.py by using the following command --> execfile('reducer3.py')

To execute above scripts in hadoop we can follow the steps as mentioned below.

1)hadoop fs -put Tweets.CSV -->  This command will place the CSV file in HDFS
2)hs mapper.py reducer.py myinput joboutput  -> Will generate the output




