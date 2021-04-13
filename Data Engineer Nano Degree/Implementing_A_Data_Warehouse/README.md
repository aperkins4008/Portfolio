# Implemeneting a Data Warehouse

## Purpose and Context
In this hypothetical scenario a music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As their data engineer, I was tasked with building an ETL pipeline that extracts their data from S3 (an Amazon storage service), staged them in Redshift, and transformed the data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to. 

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis.

#### Tools used
In the creation of this project I used Python in conjunction with Postgres (a type of open source SQL). I also used clustering to create a database warehouse utilizing Amazon's Redshift capability. 

## Schema

### Fact Table
**countall_facts_songplays** - records in log data associated with song 

     songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
    
### Dimension Tables
**users** - users in the application

    user_id, first_name, last_name, gender, level
    
**songs** - songs in music database

    song_id, title, artist_id, year, duration
    
**artists** - artists in music database

    artist_id, name, location, latitude, longitude
    
**time** - timestamps of records in songplays 

    start_time, hour, day, week, month, year, weekday
    
## Project Files
*sql_queries.py* -> contains SQL queries for dropping and creating fact and dimension tables. Also contains queries for the copy of staging tables, data insertion and post creation audit queries.

*create_tables.py* -> contains code for creating schema and appropriate tables for data warehouse. 

*dwh.cfg* -> this is the configuration file to appropriately connect to AWS's in redshift and S3. Some values have been removed to ensure security concerns. If you would like to run the project you will need to create a cluster in Redshift, fill out this configuration file accordingly.

*etl.py* -> Extract Transform Load

*auditing_analytics.ipynb* -> a python file with a function to iterate through the count all queries that were creating in "sql_queries.py". 

## Design and Justification
Due to the star schema methodology, the data has been optimized to include only a select few dimension tables that protrude of the centralized fact table. This table is also known as the bridge table. This type of form also allows for a seamless NF3 normalization for the database. In addition I have added sort keys which speeds up the call on joins and group bys. Sort keys tell the table in what sequential order a row should be inserted. 

The ETL process itself is simplified through the functions created in the *etl.py* file. It essentially copies the data from the staging tables and inserts the data appropriately into the created schema.

Note: If you would like to run the project, you must first create an amazon account and buy a cluster (if you already don't have one created). There is also a pythonic way to do this via code through amazon's purchasing API, if you would like to automate this in the future. After created, fill out the dwh.cfg configuration file appropriately. You may then run the files in the following sequential order:
    *create_tables.py* 
    *etl.py*
    *auditing_analytics.ipynb*
    
    
## Queries and Results
8056  staging_events

14896  staging_songs

333  fact_songplays

105  users

14896  songs

10025  artists

8023  time

## Udacity's Review High-Level

* You did a great job on this project.
* The code was quite modular which made it easy to read and debug.
* You have a keen eye on the domain knowledge and required parameters to get the job done.
 



