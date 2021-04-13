## Udacity Data Engineer Nano Degree

### My Data Engineering Projects
![image](https://github.com/aperkins4008/My_Projects/blob/master/Data_Engineer_Nano_Degree_(PySpark,%20Airflow,%20Cassandra,%20Postgres,%20AWS%20Redshift,%20AWS%20S3,%20AWS%20EMR)/Data_Engineering_Home.jpg?raw=true)

### Overview

These are individual projects that contributed to the entirety of my Udacity Nano Degree as a Data Engineer.  Each folder contains the given data for each project (if applicable) and the different deliverables comprising each sub-project. If you haven't seen or completed a Udacity Nano Degree, I highly recommend it; fantastic experience! If you have any questions, as always, please don't hesitate to reach out.

<br/><br/>

### What is a Data Engineer???

When you hear Data Engineer does it sound confusing? If you exclude the word data, an Engineer handles infrastructures and architecture specific to a domain. This is the same for a Data Engineer. A Data Engineer helps to create and maintain the architectures for support of Data Analyst and Data Scientist. According to dataquest.com a Data Engineer "transforms data into a useful format for analysis. A skilled Data Engineer will be able to build a pipeline and ensure that the data is always up to date."

<br/><br/>

### What do Data Engineers do???

A Data Engineer's role and responsibilities can vary from role to role or company to company. At a high level a Data Engineer must be good at:

"
* Architecting distributed systems
* Creating reliable pipelines
* Combining data sources
* Architecting data stores
* Collaborating with data science teams and building the right solutions for them


"
<br/><br/>

### Project 1: Data Modeling with Postgres

In this project, I applied what I learned on data modeling with Postgres and built an ETL pipeline using Python. To complete the project, I needed to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transferred data from files in two local directories into these tables in Postgres using Python and SQL.

Link: [Data Modeling with Postgres](https://github.com/aperkins4008/My_Projects/tree/master/Data_Engineer_Nano_Degree_(PySpark%2C%20Airflow%2C%20Cassandra%2C%20Postgres%2C%20AWS%20Redshift%2C%20AWS%20S3%2C%20AWS%20EMR)/Data_Modeling_With_Postgres)

<br/><br/>

### Project 2: Data Modeling with Apache Cassandra

In this project, I applied what I learned on data modeling with Apache Cassandra and completed an ETL pipeline using Python. To complete the project, I needed to model my data by creating tables in Apache Cassandra to run queries. I was provided with part of the ETL pipeline that transferred data from a set of CSV files within a directory to create a streamlined CSV file to model and inserted data into Apache Cassandra tables.

Link: [Data Modeling with Apache Cassandra](https://github.com/aperkins4008/My_Projects/tree/master/Data_Engineer_Nano_Degree_(PySpark%2C%20Airflow%2C%20Cassandra%2C%20Postgres%2C%20AWS%20Redshift%2C%20AWS%20S3%2C%20AWS%20EMR)/Data_Modeling_With_Apache_Cassandra)

<br/><br/>

### Project 3: Implementing a Data Warehouse

In this project, I applied what I learned on data warehouses and AWS to build an ETL pipeline for a database hosted on Redshift. To complete the project, I needed to load data from S3 to staging tables on Redshift and execute SQL statements that would create the analytics tables from these staging tables.

Link: [Implementing a Data Warehouse](https://github.com/aperkins4008/My_Projects/tree/master/Data_Engineer_Nano_Degree_(PySpark%2C%20Airflow%2C%20Cassandra%2C%20Postgres%2C%20AWS%20Redshift%2C%20AWS%20S3%2C%20AWS%20EMR)/Implementing_A_Data_Warehouse)

<br/><br/>

### Project 4: Spark Data Lake

In this project, I applied what I learned on Spark and data lakes to build an ETL pipeline for a data lake hosted on S3. To complete the project, I needed to load data from S3, process the data into analytics tables using Spark, and load them back into S3. I deployed this Spark process on a cluster using AWS.

Link: [Spark Data Lake](https://github.com/aperkins4008/My_Projects/tree/master/Data_Engineer_Nano_Degree_(PySpark%2C%20Airflow%2C%20Cassandra%2C%20Postgres%2C%20AWS%20Redshift%2C%20AWS%20S3%2C%20AWS%20EMR)/Spark_Data_Lake)

<br/><br/>

### Project 5: Data Pipelines with Apache Airflow
This project introduced me to the core concepts of Apache Airflow. To complete the project, I needed to create my own custom operators to perform tasks such as staging the data, filling the data warehouse, and running checks on the data as the final step.

Udacity provided me with a project template that takes care of all the imports and provides four empty operators that need to be implemented into functional pieces of a data pipeline. The template also contains a set of tasks that need to be linked to achieve a coherent and sensible data flow within the pipeline. I executed it with my own customer operations. 

Link: [Apache Airflow Pipeline](https://github.com/aperkins4008/My_Projects/tree/master/Data_Engineer_Nano_Degree_(PySpark%2C%20Airflow%2C%20Cassandra%2C%20Postgres%2C%20AWS%20Redshift%2C%20AWS%20S3%2C%20AWS%20EMR)/DataPipelines_w_Apache_Airflow)

<br/><br/>

## CAPSTONE Project

#### Overview
The purpose of the data engineering capstone project is to give me a chance to combine what I learned throughout the program. In this project, I was given the option to choose to complete the project provided for you, or define the scope and data for a project of your own design.

##### Udacity Provided Project
In the Udacity provided project, I'd work with four datasets to complete the project. The main dataset will include data on immigration to the United States, and supplementary datasets will include data on airport codes, U.S. city demographics, and temperature data. I was also welcome to enrich the project with additional data if I wanted to set your project apart.

###### Open-Ended Project
If I decided to design my own project, I was able find useful information in the Project Resources section within Udacity. Rather than go through steps below with the data Udacity provides, I would gather your own data, and go through the same process.


### Decision
I chose to do an open-ended project to collect and store Covid-19 data. See more at the link below.


Link: [Capstone Project](https://github.com/aperkins4008/My_Projects/tree/master/Data_Engineer_Nano_Degree_(PySpark%2C%20Airflow%2C%20Cassandra%2C%20Postgres%2C%20AWS%20Redshift%2C%20AWS%20S3%2C%20AWS%20EMR)/Capstone_Project)

### AWS Connections

While some connection are localized within your jupyter notebook connection, this project frequently makes use of Amazon's AWS capabilities. I have created a [folder of various information](https://github.com/aperkins4008/My_Projects/tree/master/Data_Engineer_Nano_Degree_(PySpark%2C%20Airflow%2C%20Cassandra%2C%20Postgres%2C%20AWS%20Redshift%2C%20AWS%20S3%2C%20AWS%20EMR)/AWS_Information) on AWS which was provided to me by Udacity. I found this material very helpful!



### Source

[dataquest.com, 2019](https://www.dataquest.io/blog/what-is-a-data-engineer/)


