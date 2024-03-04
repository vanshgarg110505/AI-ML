#!/usr/bin/env python
# coding: utf-8

# In[2]:


import mysql.connector as sql
import pandas as pd

db_connection = sql.connect(host='localhost', database='ai-ml',user='root', password='vansh')

query= 'SELECT * FROM salaries'

df=pd.read_sql(query, con=db_connection)
df


# In[3]:


import mysql.connector as sql
import pandas as pd

db_connection = sql.connect(host='localhost', database='ai-ml', user='root' , password='vansh')

query= 'SELECT * from train'

df1 = pd.read_sql(query, con = db_connection)

df1


# In[4]:


# DISPLAY TOP 5 ROWS OF THE DATASET
df.head(5)


# In[5]:


# CHECK LAST 3 ROWS OF THE DATASET
df.tail(3)


# In[6]:


# FIND SHAPE OF OUR DATASET(NUMBER OF ROWS & NUMBER OF COLUMNS)
print ("Number of Rows" , df.shape[0])
print ("Number of Columns" , df.shape[1])


# In[7]:


# GET INFORMATION ABOUT OUR DATASET LIKE TOTAL NUMBER ROWS,TOTAL NUMBER OF COLUMNS,DATATYPE OF EACH COLUMN AND MEMORY REQUIREDMENT
df.info()


# In[8]:


# GET OVERALL STATISTICS ABOUT THE DATAFRAME
df.describe()


# In[14]:


# DATA FILTERING
df1.filter(["Survived"])


# In[10]:


# CHECK NULL VALUES IN THE DATASET
df.isnull()


# In[11]:


# DROP THE COLUMN
df.drop(['Benefits'], axis=1)


# In[15]:


# HANDLE MISSING VALUES

missing_values = df1.isnull().sum()
print("Missing values:\n", missing_values)


# In[17]:


# CATEGORICAL DATA ENCODING


# In[1]:


# WHAT IS UNIVARIATE ANALYSIS

# Univariate analysis is a statistical method used to analyze data sets containing only one variable. 


# In[13]:


# HOW MANY PEOPLE SURVIVED AND HOW MANY DIED PLOT ON GRAPH

import matplotlib.pyplot as plt

# Group the data by the 'Survived' column and count the occurrences of each category
survived_count = df1['Survived'].value_counts()

# Plot the counts
plt.figure(figsize=(8, 6))
plt.bar(survived_count.index, survived_count.values, color=['red', 'green'])
plt.xticks(survived_count.index, ['Died', 'Survived'])
plt.xlabel('Outcome')
plt.ylabel('Number of People')
plt.title('Number of People Survived and Died')
plt.show()


# In[10]:


# HOW MANY PASSENGERS WERE IN FIRST CLASS,SECOND CLASS AND THIRD CLASS PLOT THOSE FIGURES ON GRAPH

import matplotlib.pyplot as plt

# Assuming 'class' column contains categorical values for passenger class (e.g., 'First', 'Second', 'Third')
class_counts = df1['Pclass'].value_counts()

# Plot
plt.bar(class_counts.index, class_counts.values, color=['blue', 'orange', 'green'])
plt.xlabel('Passenger Class')
plt.ylabel('Number of Passengers')
plt.title('Number of Passengers in Each Class')
plt.show()


# In[11]:


# NUMBER  OF MALE AND FEMALE PASSENGERS

male_count = df1[df1['Sex'] == 'male'].shape[0]
female_count = df1[df1['Sex'] == 'female'].shape[0]
print("Number of males:", male_count)
print("Number of females:", female_count)


# In[ ]:


# BIVARIATE ANALYSIS

# Bivariate analysis is a statistical method used to analyze the relationship between two different variables. Unlike univariate analysis, which focuses on analyzing one variable at a time, bivariate analysis examines how the variation in one variable may be related to the variation in another variable.


# In[15]:


# WHO HAS BETTER CHANCE OF SURVIVAL MALE OR FEMALE
import matplotlib.pyplot as plt
import pandas as pd

# Calculate survival rates for males and females
survival_rates = df1.groupby('Sex')['Survived'].mean()

print("Survival Rates by Gender:")
print(survival_rates)


survival_rates.plot(kind='bar', color=['blue', 'pink'])
plt.xlabel('Gender')
plt.ylabel('Survival Rate')
plt.title('Survival Rates by Gender')
plt.xticks(rotation=0)
plt.show()


# In[14]:


# WHICH PASSENGER CLASS HAS BETTER CHANCE OF SURVIVAL(FIRST,SECOND,OR THIRD CLASS)?
import matplotlib.pyplot as plt
import pandas as pd


# Calculate survival rates for each passenger class
survival_rates_by_class = df1.groupby('Pclass')['Survived'].mean()

print("Survival Rates by Passenger Class:")
print(survival_rates_by_class)

survival_rates_by_class.plot(kind='bar', color=['green', 'blue', 'red'])
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.title('Survival Rates by Passenger Class')
plt.xticks(rotation=0)
plt.show()


# In[ ]:


# FEATURE ENGINEERING

#Feature engineering is a crucial step in the machine learning pipeline where you create new features or transform existing ones to improve the performance of your model.

