#!/usr/bin/env python
# coding: utf-8

# # Salary_Predictor_GUI

# # Table of Contents
# 
# * [A. Context](#context)
# * [B. Data Collection](#collection)
# * [C. Package Execution and Data Import](#extract)
# * [D. Machine Learning and GUI Product](#ml) 
#     * [I. K-Nearest Neighbor (KNN) Model Training](#KNN)
#     * [II. Graphical User Interface (GUI) Product](#GUI)

# # A. Context <a class="anchor" id="context"></a>

# This parallel program is a tool which implements a KNN learning algorithm as fitted within a connected body of work. The study that was ran in parallel with this tool is named “Random Forest on IT Salary Data Set,” and was produced as a Capstone project for my Masters in Data Analytics in conjunction with Wester Governors University. KNN was selected as opposed to the MLP neural network alternative, as it is much faster and is also less likely to be subject to over-fitting.
# 
# This program uses the streamlit API as a GUI in order to provide WGU students a way to predict their Salary Tier in future years. The tool uses the final clean dataset from the original study, in order to quickly train the KNN algorithm and produce fast results. Think of the program as a condensed version to the original study, with meaningful value to others. The GUI this program produces allows the KNN algorithm to accept user inputs. After selection of inputs the user can then execute the machine learning algorithm and can predict what pay band they may fall into, in the years to come. 
# 
# **TO RUN**
# 
# To run this program, do the following:
# 
# * Download folder called “Predictor_GUI” and place in directory location of your choice
# * Open “Salary_Predictor_GUI.py” and change the directory location in the code to the location where you placed the folder above
# * Save the file
# * Upload this newly saved file into your Jupyter Notebook tree
# * Open your anaconda prompt and type “streamlit run Salary_Predictor_GUI.py” -- then press enter.
# * That’s it!!! Now predict your future pay band.

# # B. Data Collection <a class="anchor" id="collection"></a>

# The data for this program was originally obtained and is publicly-available information provided by Brent Ozar Unlimited and is a survey of Data Professional’s salaries dating back to 2017 (Ozar, 2020). Before removing outlying records, the dataset contained 8,628 rows.
# 
# Brent Ozar Unlimited has made this data publicly available as a part of public domain. There is no private information of any kind within the dataset that restricts use or identifies specific individuals. Additionally, since this is a survey, some information could have easily been mis-keyed or mis-represented. One limitation of this dataset is that this study is a collection of only four years of survey data. Another limitation of this dataset is that values are missing for certain fields.  Any challenges with the data are directly related to the fact that survey data is often not as accurate as other means of collection.

# # C. Package Execution and Data Import <a class="anchor" id="extract"></a>

# In[1]:


# Importing packages at beginning of file as standard best practice
# Standard packages
import pandas as pd
import numpy as np
import os

# Processing packages
from sklearn.preprocessing import (OneHotEncoder, MaxAbsScaler)
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split

# Supervised package
from sklearn.neighbors import KNeighborsClassifier

#Fixing Chained false positive, and warnings later in code.
pd.options.mode.chained_assignment = None 

# Streamlit API GUI specific
import streamlit as st
from PIL import Image
from pandas import DataFrame


# ### Below are the Modules and their corresponding version numbers utilized during this study.
# 
# *Note:* Any versions not included below are module classes utilized by Python’s base package. 

# | Package/Module | Version |
# | :----------- | -----------: |
# | conda | 4.9.2 |
# | Python | 3.7.9 |
# | pandas | 1.1.3 |
# | numpy | 1.19.2 |
# | sklearn | 0.23.2 |
# | streamlit | 0.72.0 |

# In[2]:


# Declaring the Directory using OS to ensure the ease of use in working with the directory location
# THIS NEEDS CHANGED TO YOUR DIRECTORY LOCATION IN ORDER TO RUN WITHOUT ERROR!!!!!
DirectoryLocation = r'C:\Users\andre\Desktop\Extras\WGU\Masters\Capstone\Predictor_GUI'
os.chdir(DirectoryLocation)

# Import Cleaned Data
cleanedData = pd.read_csv('Salary_Predictor_GUI_DF.csv')

# Removing Salary from cleaned data set
cleanedData.drop('SalaryUSD', axis=1, inplace=True)


# # D. Machine Learning and GUI Product <a class="anchor" id="ml"></a>

# ## b. I. K-Nearest Neighbor (KNN) Model Training <a class="anchor" id="KNN"></a>

# In[3]:


# Setting predictor and response variables
y = cleanedData.pop('Salary_Cat')
X = cleanedData


# In[4]:


# Splits the data into training data set and validation data set
seed = 50  # so that the result is reproducible
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state = seed)

#One final assurance on NA values
X_train = X_train.fillna('na')
X_test = X_test.fillna('na')


# In[5]:


# Creates features to encode that are not numeric
# Manage staff implicitly has been changed to Boolean, so defining it as an object to ensure encoding
X_train['ManageStaff'] = X_train['ManageStaff'].astype('object')
features_to_encode = X_train.columns[X_train.dtypes==object].tolist()


# In[6]:


# Creates encoder object
col_trans = make_column_transformer(
                        (OneHotEncoder(),features_to_encode),
                        remainder = "passthrough"
                        )

# Feature scaling
scaler = MaxAbsScaler ()


# In[7]:


# Changing to strings for test and train data

# Train
X_train[['SurveyYear', 'Country', 'EmploymentStatus', 'JobTitle', 'ManageStaff',
        'OtherPeopleOnYourTeam', 'Education', 'EmploymentSector', 'Gender']] = X_train[['SurveyYear', 
        'Country', 'EmploymentStatus', 'JobTitle', 'ManageStaff',
        'OtherPeopleOnYourTeam', 'Education', 'EmploymentSector', 'Gender']].astype('string')


#Test
X_test[['SurveyYear', 'Country', 'EmploymentStatus', 'JobTitle', 'ManageStaff',
        'OtherPeopleOnYourTeam', 'Education', 'EmploymentSector', 'Gender']] = X_test[['SurveyYear', 
        'Country', 'EmploymentStatus', 'JobTitle', 'ManageStaff',
        'OtherPeopleOnYourTeam', 'Education', 'EmploymentSector', 'Gender']].astype('string')


# In[8]:


# K-Nearest Neighbor (KNN)
knn = KNeighborsClassifier(n_neighbors = 2)

# Creates combined machine learning object
pipe = make_pipeline(col_trans, scaler, knn)

# Fits and predicts score
pipe.fit(X_train, y_train)


# ## II. Graphical User Interface (GUI) Product <a class="anchor" id="GUI"></a>

# In[12]:


#Add streamlit title, add descriptions and load an attractive image
st.title('Predict your Salary Pay Band!')
st.write('This is a Machine Learning GUI. It is built to take your user input and predict your future salary category (pay band), based upon a Data Professional Survey Data set.')
image = Image.open('Service_1_Pic.jpg')
st.image(image, use_column_width=True)
st.write('Accurately answer the inputs on the left hand side of the screen. Try and base your answers at the time of degree completion or two years from today. Then press the button below to initiate the machine learning model prediction. Note: Make sure to input all value variables in order to get a prediction. Additionally, erroneous values will cause an error (aka 100 years, etc.).')         


# In[13]:


# Creates input statement variables
SurveyYear                =    "2020"

Country                   =    st.sidebar.multiselect("What Country to you live or work?", 
                                                      options=['Australia', 'Canada', 'India', 'Germany', 'Netherlands', 
                                                               'New Zealand', 'South Africa', 'Sweden', 'United Kingdom', 
                                                               'United States', 'Other'])

PrimaryDatabase           =    st.sidebar.multiselect("What is the primary database type you work with most regularly (or hope to work with in the future)?", 
                                                        options=['Amazon RDS (any flavor)', 'Azure SQL DB', 'DB2',
                                                                 'Microsoft Access', 'Microsoft SQL Server', 'MySQL/MariaDB', 
                                                                 'Oracle', 'PostgreSQL', 'Other'])
      
YearsWithThisDatabase     =    st.sidebar.number_input("How many years have you (or will you) have worked with the above database type?", min_value=1)
                                                       

EmploymentStatus          =    st.sidebar.multiselect("Please Select Employment Status", 
                                                    options=['Contractual work', 'Full time employee', 'Part time'])

EmploymentSector          =    st.sidebar.multiselect("What is (or will be) your employment sector?", 
                                                      options=['Education (K-12, college, university)', 'Federal government',
                                                               'Local government', 'Non-profit', 'Private business',  
                                                               'State/province government', 'Student'])

JobTitle                  =    st.sidebar.multiselect("What's your current or future job title?", 
                                                      options=['Analyst', 'Architect', 'Data Scientist', 'DBA',
                                                               'DBA (Development Focus - tunes queries, indexes, does deployments)',
                                                               'DBA (Production Focus - build & troubleshoot servers, HA/DR)',
                                                               'Developer: App code (C#, JS, etc)', 
                                                               'Developer: Business Intelligence (SSRS, PowerBI, etc)', 'Developer: T-SQL', 
                                                               'Engineer', 'Manager', 'Other'])

YearsWithThisTypeOfJob    =    st.sidebar.number_input("By rounding, how many years have you (or you will) have worked in this type of role?", min_value=1)
                                                      
ManageStaff               =    st.sidebar.select_slider("Do you (or will you) manage staff?", options=['True', 'False'])

                                                       
OtherPeopleOnYourTeam     =    st.sidebar.multiselect("How many people are (or will be) on your team?", 
                                                        options=['None', '1', '2', '3', '4', '5', 'More than 5'])

Education                 =    st.sidebar.multiselect('What will be your highest post High-School education after attending WGU?', 
                                                        options=['None (no degree completed)','Associates (2 years)', 
                                                                 'Bachelors (4 years)', 'Masters', 'Doctorate/PhD'])
                                                      
Gender                    =    st.sidebar.multiselect("What's your gender?", 
                                                        options=['Female', 'Male', 'Prefer not to say'])

row = [SurveyYear, Country, PrimaryDatabase, YearsWithThisDatabase, EmploymentStatus, JobTitle, ManageStaff, 
       YearsWithThisTypeOfJob, OtherPeopleOnYourTeam, Education, EmploymentSector, Gender]

feat_cols = ['SurveyYear', 'Country', 'PrimaryDatabase', 'YearsWithThisDatabase', 'EmploymentStatus', 'JobTitle', 
             'ManageStaff', 'YearsWithThisTypeOfJob', 'OtherPeopleOnYourTeam', 'Education', 'EmploymentSector', 'Gender']

# Turns row into dataframe
row = DataFrame(row).transpose()
row.columns = feat_cols


# In[15]:


# Creates Prediction Button based upon above variables
if (st.button('Find Salary Tier')):
    
    row[['SurveyYear', 'Country', 'EmploymentStatus', 'JobTitle', 'ManageStaff',
        'OtherPeopleOnYourTeam', 'Education', 'EmploymentSector', 'Gender']] = row[['SurveyYear', 
        'Country', 'EmploymentStatus', 'JobTitle', 'ManageStaff',
        'OtherPeopleOnYourTeam', 'Education', 'EmploymentSector', 'Gender']].astype('string')
    
    row.SurveyYear = SurveyYear
    row.Country = Country
    row.EmploymentStatus = EmploymentStatus
    row.JobTitle = JobTitle
    row.ManageStaff = ManageStaff
    row.OtherPeopleOnYourTeam = OtherPeopleOnYourTeam
    row.Education = Education
    row.EmploymentSector = EmploymentSector
    row.Gender = Gender
    row.PrimaryDatabase = PrimaryDatabase
    row.YearsWithThisDatabase = YearsWithThisDatabase
    row.YearsWithThisTypeOfJob = YearsWithThisTypeOfJob

    
    result = pipe.predict(row)
    
  #display Tier and some information about the Tier
    st.write('Your predicted Salary Tier is...........', result[0],'!')
    st.write('There are five Tiers, each incremented in 50k segments. Tier 1 is the lowest and Tier 5 is the highest.')
    if result[0] == "Tier 1":
        st.write(f"\nYou are expected to make between $0-49.9k yearly, based upon your inputs.")
    elif result[0] == "Tier 2":
        st.write(f"\nYou are expected to make between $50,000-99.9k yearly, based upon your inputs.")
    elif result[0] == "Tier 3":
        st.write(f"\nYou are expected to make between $100,000-149.9k yearly, based upon your inputs.")
    elif result[0] == "Tier 4":
        st.write(f"\nYou are expected to make between $150,000-199.9k yearly, based upon your inputs.")
    else:
        st.write(f"\nFerrari's are in your future, you are expected to make over $200,000 yearly, based upon your inputs.")


# In[ ]:




