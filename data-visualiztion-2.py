#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import all the libaries.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


# In[2]:


os.chdir("C:\\Users\\khush\\OneDrive\\Documents\\")
dataset = pd.read_csv("Iris.csv")
dataset.head()


# In[3]:


dataset.info()


# In[4]:


dataset.shape


# In[5]:


#from above we can say there is no null value in the dataset.
dataset.describe()


# In[6]:


dataset.count()


# In[7]:


dataset.value_counts("Species")


# In[8]:


#all the species has same count lets visualize this using seaborn.
sns.countplot(x="Species", data=dataset)
plt.plot()


# In[9]:


sns.scatterplot(x="SepalLengthCm", y="SepalWidthCm", hue="Species", data=dataset)
plt.xlabel("Sepal length (in cm)")
plt.ylabel("Sepal width (in cm)")
plt.plot()


# In[10]:


#iris-setosa have smaller speal length and larger width.
#versicolor have niether too smaller nor too larger speal length and width.
#virginica have larger length and smaller length.

#now we find relation between petal width and length.
sns.scatterplot(x='PetalLengthCm', y='PetalWidthCm', 
                hue='Species', data=dataset, ) 

plt.plot()


# In[11]:


'''from above picture we can observe the following things:
1.) iris-setosa have smaller petal length and width.
2.) versicolor have niether too large nor too small petal width.
3.) virginica have larger petal petal width and length.'''


# In[12]:


#checking the correlation between all the variables.
data = dataset




# In[13]:


data.drop('Species', axis="columns", errors='ignore',inplace=True)
data


# In[14]:


relation = data.corr(method="pearson")


# In[15]:


sns.heatmap(relation, annot=True)


# In[ ]:


#heatmap is used to visualy represent correlation between the variable menas its the visual 
#represenation of the above correlation table that we get from pearson method there is one more method called kandella
#The higher the value the good the correlation is and lies between -1 and 1(including). same varibales have corr = 1.


# In[18]:


#cheking for the outliers:
#the outliers are those data/objects whose value daviates from average value of other data item.
#example the average human age is 60-70 but if in a dataset the age is 200 this age is called the outlier.
#outlier can be detected using the boxplot.
sns.boxplot(x="SepalLengthCm", data=dataset)


# In[19]:


#there is no otulier in sepalLength.
sns.boxplot(x="SepalWidthCm", data=dataset)


# In[20]:


#in sepal width the data below 2 and above 4 act as outliers.
sns.boxplot(x="PetalLengthCm", data=dataset)


# In[21]:


#No outlier in petal length.
sns.boxplot(x="PetalWidthCm", data=dataset)


# In[22]:


#no outlier in petalWidth.

#outlier can be removed with IQR(Interquartile range) method.


# In[ ]:




