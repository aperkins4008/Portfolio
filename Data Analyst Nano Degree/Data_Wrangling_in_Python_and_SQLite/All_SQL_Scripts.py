import pandas as pd
import sqlite3
conn = sqlite3.connect(r"Data_Wrangling_DB.db")

#This following code reads is looking for any postal codes that don't match a 5 length format -- the expected outcome should
# be 0 rows returned.
pd.read_sql_query("Select * from nodes_tags where [key] = 'postcode' and length(value) < 5;", conn)


#The following code prints all County_names -- the expected outcome should be "Jefferson"
pd.read_sql_query("Select * from nodes_tags where [key] = 'county_name';", conn)


#The following code should return values where the city is distinctly (Louisville, Shively, Parkway Village, Audubon Park, 
# Lynnview, Watterson Park or Poplar Hills)
pd.read_sql_query("Select distinct [value] from nodes_tags where [key] = 'city';", conn)


#Reads any phone number where the length would include the country code or a space to exclude it
pd.read_sql_query("Select distinct [value] from nodes_tags where [key] = 'phone' and length(value) > 12;", conn)

#Reads any phone number where the value doesn't include the dashes for easy readability.
pd.read_sql_query("Select distinct [value] from nodes_tags where [key] = 'phone' and value not like '%-%';", conn)


# This query is looking to see which street has the most hits for address data
pd.read_sql_query("SELECT t.value, COUNT(*) as count FROM (SELECT * FROM nodes_tags UNION SELECT * FROM ways_tags) t WHERE t.key = 'street' GROUP BY t.value ORDER BY count DESC;", conn)


pd.read_sql_query("SELECT COUNT(*) FROM nodes;", conn)

pd.read_sql_query("SELECT COUNT(*) FROM ways;", conn)

pd.read_sql_query("SELECT COUNT(DISTINCT(users.uid)) FROM (SELECT uid FROM nodes UNION SELECT uid FROM ways) users;", conn)

pd.read_sql_query("SELECT t.value, COUNT(*) as num FROM nodes_tags t INNER JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value='restaurant') i ON t.id=i.id WHERE t.key='cuisine' GROUP BY t.value ORDER BY num DESC;", conn)