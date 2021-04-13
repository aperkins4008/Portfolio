# Data Modeling with Postgres

## Purpose and Context
In this hypothetical scenario a startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis.

## Schema

### Fact Table
**songplays** - records in log data associated with song 

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
*sql_queries.py* -> contains sql queries for dropping and creating fact and dimension tables. Also, contains insertion query template. 

*create_tables.py* -> contains code for creating up database. Running this file creates sparkifydb as well as the corresponding tables.

*etl.ipynb* -> a jupyter notebook file to analyze and simulate ETL before performing actual ETL.

*etl.py* -> Extract Transform Load

*test.ipynb* -> a notebook to connect to postgres db and validate and text some data.

## Design and Justification
Due to the star schema methodology, the data has been optimized to include only a select few dimension tables that protrude of the centralized fact table. This table is also known as the bridge table. This type of form also allows for a seamless NF3 normalization for the database.

The ETL process itself is simplified through the functions created in the *etl.py* file. It essentially read the JSON files and as it parses the data seamlessly inserts the data into the already created tables.

Note: If you would like to run the project, simply pool down all the files an first run them in the following sequential order:
    *create_tables.py* 
    *etl.py*
    *test.ipynb*

#### Tools used
In the creation of this project I used Python in conjunction with Postgres (a type of open source SQL). 