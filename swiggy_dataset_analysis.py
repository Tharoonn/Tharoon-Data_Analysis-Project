# -*- coding: utf-8 -*-
"""swiggy Dataset Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1O0nmDPpe2UlY3dODgRQWzFZmhoDcXGik
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

swg = pd.read_csv('/content/swiggy.csv')
swg.head()

swg.shape

swg.describe()

swg.info()

swg.isnull().sum()

swg['City'].nunique()

swg['City'].unique()

swg.City.value_counts()
# finding restaurants in each city count

swg['Restaurant'].nunique()
#finding total number of restaurents

swg.groupby('Restaurant')['Avg ratings'].mean().sort_values().head(10)
# finding bottom 10 restaurants with lowest ratings

swg.groupby('Restaurant')['Avg ratings'].mean().sort_values(ascending=False).head(10)
#Top 10 restarents with highest ratings

swg.groupby('Food type')['Avg ratings'].mean().sort_values(ascending = False).head(10)
# Top 10 food type with Highest ratings

food_order = swg['Food type'].value_counts().head(10)
food_order
#Top ordered Foods

city_hotel = swg.City.value_counts()
plt.bar(city_hotel.index, city_hotel.values, color = 'blue')
plt.xlabel('City')
plt.ylabel('Count of Hotels')
plt.xticks(rotation = 'vertical')
plt.show()

#Showing bar graph of hotels in each city

swg['Price'].hist(bins = 50)
plt.show()

#Finding frequency of food price

swg['Delivery time'].hist(bins=100)
plt.show()

plt.boxplot(swg['Delivery time'])
plt.show()

swg.plot(kind='scatter', x = 'Price', y = 'Avg ratings', color = 'red')
plt.xlabel('Price')
plt.ylabel('Ratings given')
plt.show()

swg.plot(kind='scatter', x = 'Delivery time', y = 'Avg ratings', color ='green')
plt.xlabel('Delivery time')
plt.ylabel('Rating given')
plt.show()

plt.figure(figsize=(10,5))
sns.countplot(data=swg, x='Avg ratings')
plt.xlabel('Rating value', weight = 'bold', fontsize = 12)
plt.ylabel('count', weight = 'bold', fontsize = 12)
plt.xticks(rotation = 50)
plt.show()

#Count plot

swg['Avg ratings'].hist()
plt.show()

city_count = swg.City.value_counts()
plt.pie(city_count, labels = city_count.index, autopct = '%1.1f%%')
plt.show()

plt.figure(figsize=(5,8))
plt.pie(city_count.values, labels=[f'{city} ({count})' for city, count in zip(city_count.index, city_count.values)])
plt.title('City Distribution')
plt.show()

