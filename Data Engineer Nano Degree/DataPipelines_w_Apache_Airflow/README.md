# Data Pipelines with Apache Airflow

## Purpose and Context
In this hypothetical scenario a music streaming company, Sparkify, has decided that it is time to introduce more automation and monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow.

They have decided to bring me into the project and expected me to create high grade data pipelines that are dynamic and built from reusable tasks, can be monitored, and allow easy backfills. They have also noted that the data quality plays a big part when analyses are executed on top the data warehouse and want to run tests against their datasets after the ETL steps have been executed to catch any discrepancies in the datasets.

The source data resides on AWS S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. The source datasets consist of JSON logs that tell about user activity in the application and JSON metadata about the songs the users listen to.

#### Tools used
In the creation of this project I used Python in conjunction with Postgres (a type of open source SQL). I also used clustering to create a database warehouse utilizing Amazon's Redshift capability. Additionally, I used Apache Airflow to create Directed Acyclic Graphs (DAGs), in order to push and parallelize the ETL process. You can see what my DAG looks like below.

![MY_DAG](https://github.com/aperkins4008/My_Projects/blob/master/Data_Engineer_Nano_Degree_(PySpark,%20Airflow,%20Cassandra,%20Postgres,%20AWS%20Redshift,%20AWS%20S3,%20AWS%20EMR)/DataPipelines_w_Apache_Airflow/pictures/DAG.PNG?raw=true)

![Tree_Dag](https://github.com/aperkins4008/My_Projects/blob/master/Data_Engineer_Nano_Degree_(PySpark,%20Airflow,%20Cassandra,%20Postgres,%20AWS%20Redshift,%20AWS%20S3,%20AWS%20EMR)/DataPipelines_w_Apache_Airflow/pictures/dag_tree.PNG?raw=true)

## Schema

### Fact Table
**public.songplays** - records in log data associated with song 

     playid, start_time, userid, level, songid, artistid, sessionid, location, user_agent
    
### Dimension Tables
**public.users** - users in the application

    userid, first_name, last_name, gender, level
    
**public.songs** - songs in music database

    songid, title, artistid, year, duration
    
**public.artists** - artists in music database

    artistid, name, location, latitude, longitude
    
**public.time** - timestamps of records in songplays 

    start_time, hour, day, week, month, year, dayofweek
    
## Project Files
*udac_example_dag.py* -> The file is located within the dag folder. It is essentially the mastering module used to run the operators and facilitates the DAG itself that is pulled into Airflow’s UI. This is what is executed in Airflow.

*create_tables.py* -> Contains code for creating schema and appropriate tables for staging, facts and dimension tables. Also located in the dag folder, this was supplied by Udacity and altered by myself. 

*sql_queries.py* -> This file was supplied to me within the plugins >> helpers folder. This is essentially used during the process to make selects and inserts after the fact and dimension tables are built. 

*stage_redshift.py* -> This is an operator file that was given as a template by Udacity. Airflow uses these types of files in a modular fashion to facilitate scalable processes and ETLs over time. This file is located within the plugins >> operators folder and is used to parse the AWS S3 files into Redshift during a staging phase.

*load_fact.py* -> This is an operator file that was given as a template by Udacity. Airflow uses these types of files in a modular fashion to facilitate scalable processes and ETLs over time. This file is located within the plugins >> operators folder and is used to insert data into the fact table from the staging tables.

*load_dimension.py* -> This is an operator file that was given as a template by Udacity. Airflow uses these types of files in a modular fashion to facilitate scalable processes and ETLs over time. This file is located within the plugins >> operators folder and is used to insert data into the different dimension tables from the staging tables.

*data_quality.py* -> This is an operator file that was given as a template by Udacity. Airflow uses these types of files in a modular fashion to facilitate scalable processes and ETLs over time. This file is located within the plugins >> operators folder. Last but not least, this is used to ensure the tables are not null at the end of any ETL process.


## Design and Justification
Due to the star schema methodology, the data has been optimized to include only a select few dimension tables that protrude of the centralized fact table. This table is also known as the bridge table. This type of form also allows for a seamless NF3 normalization for the database. 

The ETL process itself is managed mostly through the udac_example_dag.py file. You can think of this file as a mastering file. All the other files are modular connected to this file itself.
Note: If you would like to run the project, you must first create an amazon account and buy a cluster (if you already don't have one created). There is also a pythonic way to do this via code through amazon's purchasing API, if you would like to automate this in the future. After created, you will need to add connection appropriately within Airflow, in order to ensure your access and secret keys are encrypted appropriately. Once you have connected to Airflow's UI I have some pictures below that will help describe which connections and passwords you will need to add in order to get this project to run appropriately. This will encrypt your credentials as well.

![Connection](https://github.com/aperkins4008/My_Projects/blob/master/Data_Engineer_Nano_Degree_(PySpark,%20Airflow,%20Cassandra,%20Postgres,%20AWS%20Redshift,%20AWS%20S3,%20AWS%20EMR)/DataPipelines_w_Apache_Airflow/pictures/Connection1.PNG?raw=true)

![Connection](https://github.com/aperkins4008/My_Projects/blob/master/Data_Engineer_Nano_Degree_(PySpark,%20Airflow,%20Cassandra,%20Postgres,%20AWS%20Redshift,%20AWS%20S3,%20AWS%20EMR)/DataPipelines_w_Apache_Airflow/pictures/C2.PNG?raw=true)

![Connection](https://github.com/aperkins4008/My_Projects/blob/master/Data_Engineer_Nano_Degree_(PySpark,%20Airflow,%20Cassandra,%20Postgres,%20AWS%20Redshift,%20AWS%20S3,%20AWS%20EMR)/DataPipelines_w_Apache_Airflow/pictures/C3.PNG?raw=true)

![Connection](https://github.com/aperkins4008/My_Projects/blob/master/Data_Engineer_Nano_Degree_(PySpark,%20Airflow,%20Cassandra,%20Postgres,%20AWS%20Redshift,%20AWS%20S3,%20AWS%20EMR)/DataPipelines_w_Apache_Airflow/pictures/C4.PNG?raw=true)

![Connection](https://github.com/aperkins4008/My_Projects/blob/master/Data_Engineer_Nano_Degree_(PySpark,%20Airflow,%20Cassandra,%20Postgres,%20AWS%20Redshift,%20AWS%20S3,%20AWS%20EMR)/DataPipelines_w_Apache_Airflow/pictures/C5.PNG?raw=true)

![Connection](https://github.com/aperkins4008/My_Projects/blob/master/Data_Engineer_Nano_Degree_(PySpark,%20Airflow,%20Cassandra,%20Postgres,%20AWS%20Redshift,%20AWS%20S3,%20AWS%20EMR)/DataPipelines_w_Apache_Airflow/pictures/C6.PNG?raw=true)

![Connection](https://github.com/aperkins4008/My_Projects/blob/master/Data_Engineer_Nano_Degree_(PySpark,%20Airflow,%20Cassandra,%20Postgres,%20AWS%20Redshift,%20AWS%20S3,%20AWS%20EMR)/DataPipelines_w_Apache_Airflow/pictures/C7.PNG?raw=true)