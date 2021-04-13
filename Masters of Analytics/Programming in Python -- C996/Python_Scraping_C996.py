#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import all necessary packages
import requests
import bs4 as bs
import csv


# In[2]:
# Set the URL object
Url = 'https://www.census.gov/programs-surveys/popest.html'

# Send request 
r = requests.get(Url)

# Create response object 
responseHtml = r.text

# Printing object (below can be used to print object in necessary)
# This was used to pull original HTML file as requested
# print(responseHtml)


# In[3]:
# retrieved documentation from below to set up soup:
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
soup = bs.BeautifulSoup(responseHtml,features='html.parser')

#Setting blank list for later population
List = []


# In[4]:
# Finding all links by lookins for anchors (original count)
hyper_links = soup.find_all("a")

# printing number of links found
print('This scraping tool found an original number totaling', len(hyper_links), 'links.')


# In[5]:
# Using uri (Uniform resoruce identifiers) 
for url in hyper_links:
    uri_var = url.get('href')
    if type(uri_var) is str:
        if uri_var.startswith('http'):
            List.append(url.get('href'))
        if uri_var.startswith('/'):
            List.append('https://www.census.gov%s' % uri_var)


# In[6]:
# must remove any remaining slashes
for i in range(len(List)):
    if List[i].endswith('/'):
        List[i] = List[i][:-1]


# In[7]:
# removing duplicates from list
List = list(dict.fromkeys(List))

# writing list to csv
with open('uriList.csv','w') as uriFile:
    writer = csv.writer(uriFile, quoting=csv.QUOTE_ALL)
    writer.writerow(List)


# In[8]:
# Final Audit
print('After duplicates and others were removed, there were a total of', len(List), 'links.')
print('Script Successful!')




