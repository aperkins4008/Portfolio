# Data Modeling with Apache Cassandra

## Purpose and Context
In this hypothetical scenario a startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.

They'd like a data engineer to create an Apache Cassandra database which can create queries on song play data to answer the questions, and wish to bring you on the project. Your role is to create a database for this analysis. You'll be able to test your database by running queries given to you by the analytics team from Sparkify to create the results.

## High Level ETL Pipeline outline:
If you would like to execute the execution of this project, please do the following.

1. Implement the logic in section Part I of the .ipynb notebook template to iterate through each event file in event_data to process and create a new CSV file in Python
2. Make necessary edits to Part II of the notebook template to include Apache Cassandra CREATE and INSERT statements to load processed records into relevant tables in your data model
3. Test by running SELECT statements after running the queries on your database
4. Finally, drop the tables and shutdown the cluster

### Tools used
In the creation of this project I used Python in conjunction with Apache Cassandra (a type of open source NoSQL Database). In addition I used CQL, which is essentially a very light SQL language used solely for Cassandra. 