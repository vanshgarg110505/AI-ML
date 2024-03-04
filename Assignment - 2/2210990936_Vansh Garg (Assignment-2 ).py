#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

df = pd.read_csv("C:\\Users\\vansh\\OneDrive\\Desktop\\Salaries.csv")
df


# In[3]:


# Display top 10 rows of dataset
df.head(10)


# In[4]:


# Check last 10 rows of dataset
df.tail(10)


# In[5]:


# Find the number of rows and columns
print ("Number of Rows" , df.shape[0])
print ("Number of Columns" , df.shape[1])


# In[6]:


# Getting info about dataset
df.info()


# In[7]:


# Check null values in the dataset
df.isnull()


# In[9]:


# Drop Id, notes, agency and status columns
df.drop(['Id' , 'Notes' , 'Agency', 'Status'] , axis = 1)


# In[12]:


# Find occurence of the employee name (top 5)
df['EmployeeName'].value_counts().head(5)


# In[13]:


# Find the number of Unique Job Titles
df['JobTitle'].nunique()


# In[27]:


# Total number of Jobs Titles contains Captain
#df[df['JobTitle'].str.contains('CAPTAIN')]
df.columns
df['JobTitle'].str.contains('CAPTAIN')
df[df['JobTitle'].str.contains('CAPTAIN')]
len(df[df['JobTitle'].str.contains('CAPTAIN')])


# In[32]:


# Display all the employee names from fire department
df.columns
df['JobTitle'].str.contains('FIRE DEPARTMENT')
df[df['JobTitle'].str.contains('FIRE DEPARTMENT')]['EmployeeName']


# In[57]:


# Replace 'NOT PROVIDED' in EmployeeName column to NaN

df.columns
df['EmployeeName'].replace('Not provided', 'NaN')
df


# In[6]:


# Drop the rows having more than 5 missing values
df = df.dropna(thresh=df.shape[1]-5)
df


# In[17]:


# find the job title of ALBERT PARDINI
df.columns
df['JobTitle']
df[df['EmployeeName']=='ALBERT PARDINI']['JobTitle'].values[0]


# In[19]:


# HOW MUCH ALBERT PARDINI MAKE (INCULDE BENEFITS)?
df.columns
df[df['EmployeeName']=='ALBERT PARDINI']['TotalPayBenefits'].values[0]


# In[21]:


# DISPLAY NAME OF THE PERSON HAVING THE HIGHEST BASEPAY
df.columns
df[df['BasePay'] == df['BasePay'].max()]['EmployeeName'].values[0]


# In[22]:


# FIND AVERGE BASEPAY OF ALL EMPLOYEE PER YEAR
df[df['BasePay'] == df['BasePay'].mean()]['EmployeeName'].values[0]


# In[23]:


# FIND AVERGE BASEPAY OF ALL EMPLOYEE PER JOB TITLE
df[df.groupby('JobTitle')['BasePay'].mean()]


# In[28]:


# FIND AVERGE BASEPAY OF EMPLOYEE HAVING JOB TITLE ACCOUNTANT
df.columns
df['JobTitle'] == 'ACCOUNTANT'
df[df['JobTitle'] == 'ACCOUNTANT']['BasePay'].mean()


# In[34]:


# FIND TOP5 MOST COMMON JOBS
df.columns
df['JobTitle']
df['JobTitle'].value_counts() #Count occurence of each job title
df['JobTitle'].value_counts().head(5)

