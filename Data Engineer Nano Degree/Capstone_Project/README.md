# Data Engineering Capstone Project

## Project Summary
During the pandemic of 2020, the ability to track and use data to ensure the safety of others is/was crucial. This project takes some of that data collected by others, and houses it in a cluster on AWS. The benefit of this collection would allow others to use this data in its normalized format to perform analytical queries. For ease of use during this ETL process the data was downloaded from the corresponding sites and loaded directly onto my AWS S3 bucket. The data itself was pulled from the two source listed below. Additionally, when combined in tabular form this data was over a million rows meeting the requirement of the project. I will be limiting my scope to that of the United States, which will be filtered out later during the ETL process.

#### Google Community Mobility Reports
This data aims to provide insights into how movement has shifted and changed throughout the pandemic. The data was collected through Google's store of location data throughout the world and was downloaded as a CSV file. In tabular form this data is approximately 470,000 rows of data (at the time of ingestion.) If you would like to know more about this data set, please visit Google's page [here.](https://www.google.com/covid19/mobility/)


#### AWS Covid 19 Data Lake
This data is an open source data lake collected by various parties and loaded onto AWS. The data itself contains population, confirmed and death cases data. I used tableau's collection of three Json files. In tabular form this data would be approximately 940,000 rows of data (at the time of ingestion.) It appears to have been gathered by John Hopkins University using a robotic collect and store methodology. You can find out more about the collection means by John Hopkins University [here.](https://github.com/CSSEGISandData/COVID-19) Additionally, you can find the actual data lake where the Json files were downloaded at [this AWS location.](https://dj2taa9i652rf.cloudfront.net/)


#### Getting Started
To get started I downloaded the files above and placed them in my Jupyter Notebook directory. I have them placed in this folder for convenience. 

* The steps to find the John Hopkins data once clicking the link is to navigate to the following directory: covid19-lake/ tableau-jhu / json  -- Note: I would discourage downloading this data as it is subject to column change often and should use what is already downloaded. You will see later where column adjustment had to be made
* To download the Google data from the link mentioned above, simply click the "Download global CSV" button
* Please use the Capstone_Project_StepbyStep.ipynb to walk through the ETL process step by step. There will need to be two configuration files changes and one S3 bucket location to get the project to execute effectively.
* Using Version Python 3.7.6

![High Level Architecture](https://github.com/aperkins4008/My_Projects/blob/master/Data_Engineer_Nano_Degree_(PySpark,%20Airflow,%20Cassandra,%20Postgres,%20AWS%20Redshift,%20AWS%20S3,%20AWS%20EMR)/Capstone_Project/Pictures/Arch.PNG?raw=true)

## Steps Taken

#### Step 1: Scope the Project and Gather Data
    
    * Identify and gather the data you'll be using for your project (at least two sources and more than 1 million rows). 
    * Explain what end use cases you'd like to prepare the data for (e.g., analytics table, app back-end, source-of-truth database, etc.)
    
#### Step 2: Explore and Assess the Data

    * Explore the data to identify data quality issues, like missing values, duplicate data, etc.
    * Document steps necessary to clean the data

#### Step 3: Define the Data Model

    * Map out the conceptual data model and explain why you chose that model
    * List the steps necessary to pipeline the data into the chosen data model

#### Step 4: Run ETL to Model the Data

    * Create the data pipelines and the data model
    * Include a data dictionary
    * Run data quality checks to ensure the pipeline ran as expected

#### Step 5: Complete Project Write Up

    * What's the goal? What queries will you want to run? How would Spark or Airflow be incorporated? Why did you choose the model you chose?
    * Clearly state the rationale for the choice of tools and technologies for the project.
    * Document the steps of the process.
    * Propose how often the data should be updated and why.
    * Include a description of how you would approach the problem differently under the following scenarios:
        If the data was increased by 100x.
        If the pipelines were run on a daily basis by 7am.
        If the database needed to be accessed by 100+ people.


#### Tools used
I plan to take the data from my local computer and load the files into S3. From there I will be doing some light transformation on my local machine just for formatting purposes. The rest of the transformation process will take place in AWS Redshift (cloud data warehouse solution.) The data will be in a normalized for hypothetical data analysis purposes. 

## Schema

### Fact Table
**demographics** - records of demographic information for dimension tables 

     compositekey, state, county, fips, latitude, longitude
    
### Dimension Tables
**covidCaseData** - Confirmed and Death cases over time in the United States

    compositekey, caseType, cases, difference, date
    
**googleMobility** - Google Mobility Report percentage change from some baseline, using Google's location data

    compositekey, date, retail_and_recreation_percent_change, grocery_and_pharmacy_percent_change, parks_percent_change, transit_stations_percent_change, workplaces_percent_change, residential_percent_change
    
![RedShift Tables](https://github.com/aperkins4008/My_Projects/blob/master/Data_Engineer_Nano_Degree_(PySpark,%20Airflow,%20Cassandra,%20Postgres,%20AWS%20Redshift,%20AWS%20S3,%20AWS%20EMR)/Capstone_Project/Pictures/TableInfo.PNG?raw=true)

![Google Staging Table](https://github.com/aperkins4008/My_Projects/blob/master/Data_Engineer_Nano_Degree_(PySpark,%20Airflow,%20Cassandra,%20Postgres,%20AWS%20Redshift,%20AWS%20S3,%20AWS%20EMR)/Capstone_Project/Pictures/staging_google.PNG?raw=true)
![John Hopkins Staging Table](https://github.com/aperkins4008/My_Projects/blob/master/Data_Engineer_Nano_Degree_(PySpark,%20Airflow,%20Cassandra,%20Postgres,%20AWS%20Redshift,%20AWS%20S3,%20AWS%20EMR)/Capstone_Project/Pictures/staging_covid.PNG?raw=true)

![Demographic Table](https://github.com/aperkins4008/My_Projects/blob/master/Data_Engineer_Nano_Degree_(PySpark,%20Airflow,%20Cassandra,%20Postgres,%20AWS%20Redshift,%20AWS%20S3,%20AWS%20EMR)/Capstone_Project/Pictures/demo.PNG?raw=true)
![Covid Cases Table](https://github.com/aperkins4008/My_Projects/blob/master/Data_Engineer_Nano_Degree_(PySpark,%20Airflow,%20Cassandra,%20Postgres,%20AWS%20Redshift,%20AWS%20S3,%20AWS%20EMR)/Capstone_Project/Pictures/CovidCaseData.PNG?raw=true)
![Google Mobility Table](https://github.com/aperkins4008/My_Projects/blob/master/Data_Engineer_Nano_Degree_(PySpark,%20Airflow,%20Cassandra,%20Postgres,%20AWS%20Redshift,%20AWS%20S3,%20AWS%20EMR)/Capstone_Project/Pictures/googleM.PNG?raw=true)

    
## Project Files
*Capstone_Project_StepbyStep.ipynb* -> The is the step by step walk through of how I did my capstone to the correct specifications. By walking through this Jupyter notebook, you will execute the following module queries below and perform the ETL from start to finish.

*sql_queries.py* -> contains SQL queries for dropping and creating fact and dimension tables. Also contains queries for the copy of staging tables, data insertion and post creation audit queries.

*create_tables.py* -> contains code for creating schema and appropriate tables for data warehouse. 

*dwh.cfg* -> this is the configuration file to appropriately connect to AWS's in redshift and S3. Some values have been removed to ensure security concerns. If you would like to run the project you will need to create a cluster in Redshift, fill out this configuration file accordingly after creating your cluster.

*dl.cfg* -> this file is used only initially to load the data into S3 

*etl.py* -> Extract Transform Load

*PNGs*  -> Diagrams

*Other files* -> All the other files should be data or version of that same data


## Design and Justification
Due to the star schema methodology, the data has been optimized to include only a select few dimension tables that protrude of the centralized fact table. This table is also known as the bridge table. This type of form also allows for a seamless NF3 normalization for the database. In addition I have added sort keys which speeds up the call on joins and group bys. Sort keys tell the table in what sequential order a row should be inserted. 

The ETL process itself is simplified through the functions created in the *etl.py* file. It essentially copies the data from the staging tables and inserts the data appropriately into the created schema.

Note: If you would like to run the project, you must first create an amazon account and buy a cluster (if you already don't have one created). There is also a pythonic way to do this via code through amazon's purchasing API, if you would like to automate this in the future. After created, fill out the dwh.cfg configuration file appropriately. You may then run the *Capstone_Project_StepbyStep.ipynb* file by executing each block of code accordingly. Please also note, there are a couple of variables along the way that will needs changed other than the conjugation files for Redshift. The main one is the S3 bucket location which I've called out in the comments.
    

## Queries and Results

1887256  *staging_covidCase*

954644  *staging_googleMobility*

6518  *demographics*

1746824  *covidCaseData*

564102  *googleMobility*


## Udacity's Review High-Level

* You did a wonderful job in this submission, you nailed all the rubrics
* So far this is one of the best projects I have reviewed so far, you should be proud.
* Here at Udacity we are proud to have bright students like you in our community we look to continue this journey together.
* You are a hard worker, the quality of your work can tell. I encourage you to never stop learning and always give in your best.
* I wish you good luck in pursuing the path you have chosen.
