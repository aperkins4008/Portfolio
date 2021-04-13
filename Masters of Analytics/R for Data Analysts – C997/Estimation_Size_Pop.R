 # Make sure I import all the correct libraries and that they are installed
library(tinytex)
library(dplyr)
library(tidyverse)
library(ggplot2)
library(ggthemes)
library(rmarkdown)
library(XLConnect)
library(readxl)
library(devtools)


# Read in excel data source using readxl library
original_est_file <- read_excel("C:\\Users\\andre\\Desktop\\Extras\\WGU\\Masters\\R for Data Analysts\\nst-est2019-alldata.xlsx")
# This original data set includes 57 observations and 151 variables

# Removing all but the data for Kentucky
df2 <- original_est_file[23,]

#Confirming Kentucky has been pulled (visual audit)
df2
df2[,5]

# Reduces columns to population estimates 2010-2019
df3 <- df2[,1:17]

#Confirming column reductions (visual audit)
df3

# Removes first four columns (unnecessary)
df4 <- df3[,5:17]

#Confirming column reductions (visual audit)
df4 

# Creating final data set for analysis (this is only 2010-2019 pop estimates, 1 observation with 10 variables)
data <- df4[-(1:3)]

# One final visual audit
data

# Doing initial summary of each year's observation
summary(data)


###################################PLOT######################################################
# This is Population over year for the state of Kentucky

# Creating population values based upon data frame 
pop <- c(4348181,	4369821,	4386346,	4404659,	4414349,	4425976,	4438182,	4452268,	4461153,	4467673)

# Visual audit of population
pop

# Creating year values based upon data frame
year <- c(2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019)

# Visual audit of year
year

#Actually creating the plot using the previously created values
plot(year, pop,xlab="Year",ylab="Population", main = "Population Over Year for Kentucky", type = "b")


###################################MODEL######################################################
# Setting the model parameters
model <- lm(pop~year, data = data)
future <- data.frame(year=c(2020, 2021, 2022, 2023, 2024, 2025))
pred <- predict(model, future)

# View the prediction numbers
pred

# Summarizing descriptive analytics of the model 
# (you can see high R value, indicating a strong linear correlation even if you weren't able to look at the plot)
summary(model)

# Combining both population and year data sets for historical and predictive values
total_pop <- c(pop, pred)
total_years <- c(year, 2020, 2021, 2022, 2023, 2024, 2025)

# Visual Audit of both above
total_pop
total_years

# Plotting data with predictive values
plot(total_years, total_pop, xlab="Year",ylab="Population", main = "Population Over Year for Kentucky", type = "b")