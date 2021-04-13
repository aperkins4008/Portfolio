# Data Lakes with PySpark

## Purpose and Context
In this hypothetical scenario a music streaming startup, Sparkify, has grown their user base and song database even more and want to move their data warehouse to a data lake. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As their data engineer, you are tasked with building an ETL pipeline that extracts their data from S3, processes them using Spark, and loads the data back into S3 as a set of dimensional tables. This will allow their analytics team to continue finding insights in what songs their users are listening to.
They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis.

#### Tools used
In the creation of this project I used Python in conjunction with PySpark. This particular python package is used with the popular big data distributive-processing tool, Spark. I also used Amazon's EMR cluster and S3 services to implement this project from a storage standpoint.

## Schema

### Fact Table
**countall_facts_songplays** - records in log data associated with song 

     songplayId, user_id, start_time, level, song_id, artist_id, sessionId, userAgent, month, year
    
### Dimension Tables
**users** - users in the application

    userId, firstName, lastName, gender, level
    
**songs** - songs in music database

    title, artist_id, year, duration, song_id
    
**artists** - artists in music database

    artist_id, artist_name, artist_location, artist_latitude, artist_longitude
    
**time** - timestamps of records in songplays 

    timestamp, hour, day, week, weekday, month, year
    
## Project Files
*etl.py* -> Extract Transform Load. This file does all the work from building the Spark session to breaking up the files into parquet files and transferring from Udacity's S3 to my personal S3.

*dl.cfg* -> this is the configuration file to appropriately connect to AWS's in S3. Values have been removed to ensure security concerns. 


## Design and Justification
Due to the star schema methodology, the data has been optimized to include only a select few dimension tables that protrude of the centralized fact table. This table is also known as the bridge table. This type of form also allows for a seamless NF3 normalization for the database. 


The ETL process itself is simplified through the two main functions created in the *etl.py* file. It essentially copies the data from Udacity's S3 store, partitions out the appropriate tables for distributive  process and inserts the data appropriately into my personal S3 stores in AWS.

Note: If you would like to run the project, the best way is to run this project on an Amazon EMR cluster. You must first create an amazon account and purchase an EMR cluster (if you already don't have one created). 
There is also a pythonic way to do this via code through amazon's purchasing API, if you would like to automate this in the future. You can view how to set up an EMR cluster at [this link.](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs-launch-sample-cluster.html) Once you have your Spark cluster up and running you can connect and kick off your Spark job using the steps provided [here.](https://github.com/cs327e-fall2017/snippets/wiki/Connect-and-Configure-EMR-Cluster) Make sure to add your AWS IAM keys to the configuration file before execution.



    

