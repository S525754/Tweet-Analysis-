# Tweet-Analysis---Airline-Sentiment
This project analysis the dataset which has tweets from airlines customers on its service.
Customers will give either positive, negative or neutral feedback to the airline service. We would like to analyze these tweets for different airlines.

# Dataset we have referred:

We have got this dataset from Kaggle. com and link to this repository is as below

https://www.kaggle.com/crowdflower/twitter-airline-sentiment

Total file size: 3MB

We will also analyse the following mapreduce problems

# MapRedce Problem1:
What is the positive feedback percentage for the United Airlines?
Solution:
We have given United airlines with postive and negative feedback

# MapRedce Problem2:
Which type of issues made customers give negative feedback and its values?
Solution:
We have given statistics for different negative feedback

# MapRedce Problem3:
Which airline has most negative feedback and which airline has most positive feedback?
Solution:
We have provided all the airlines with positive and negative feedback details. 

Using the Tortoise SVN and GIT clone command you can pull the repository into your local system. Link is mentioned below.
https://github.com/S525754/Tweet-Analysis---Airline-Sentiment.git

How to execute the scripts in Pythonshell:
We need to keep input file in the project folder for all three mapreduce problems. We can execute python scripts with the following commands. 
Map reduce problem1:
1) Run Mapper.py by using the following command --> execfile('mapper.py')
# Sample mapper1 output:
United	positive
United	positive
United	neutral
United	positive
United	negative
United	positive
United	negative
United	positive
United	negative
United	positive
United	negative
United	negative
United	neutral
United	negative
United	negative

2) Run reducer.py by using the following command --> execfile('reducer.py')
# Sample reducer1 output:
United 	1218 	366 	238

Map reduce problem2:
1) Run Mapper2.py by using the following command --> execfile('mapper2.py')
# Sample mapper1.py output:
Cancelled Flight	1
17
17
15
Bad Flight	1
15
16
17
15

2) Run reducer2.py by using the following command --> execfile('reducer2.py')
# Sample reducer2 output:
Bad Flight	300
Can't Tell	584
Cancelled Flight	391
Customer Service Issue	1447
Damaged Luggage	31
Flight Attendant Complaints	237
Flight Booking Problems	235
Late Flight	798
Lost Luggage	348
longlines	72
negativereason 	1

Map reduce problem3:
1) Run Mapper3.py by using the following command --> execfile('mapper3.py')
# Sample mapper3.py output:
US Airways	negative
US Airways	negative
US Airways	negative
US Airways	negative
US Airways	negative
US Airways	neutral
American	negative
American	neutral
American	negative
American	negative
American	negative
American	neutral
American	negative
American	negative
American	positive
American	negative
2) Run reducer3.py by using the following command --> execfile('reducer3.py')
# Sample reducer3.py output:
American	924	232	155
Delta	484	451	288
Southwest	573	360	284
US Airways	1159	201	123
United	1218	366	238
Virgin America 	85 	90 	64

To execute above scripts in hadoop we can follow the steps as mentioned below.

1)hadoop fs -put Tweets.CSV -->  This command will place the CSV file in HDFS


2)hs mapper.py reducer.py myinput joboutput  -> Will generate the output

# MR1 Graph:

















![mr1 graph](https://cloud.githubusercontent.com/assets/25062249/25032610/202b91ec-209b-11e7-8735-12fcc579fdf1.JPG)

# MR2 Graph:


































![mr2 graph](https://cloud.githubusercontent.com/assets/25062249/25032629/5690a646-209b-11e7-88c6-429287dd90c0.JPG)

# MR3 Graph:

































![mr3 graph](https://cloud.githubusercontent.com/assets/25062249/25032628/568fc0d2-209b-11e7-9609-e7ca223393bf.JPG)


