#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset (replace 'data.csv' with your actual dataset)
df = pd.read_csv(r"C:\Users\Menda Tejaswini\Downloads\data_file.csv",encoding = 'utf-8')
# Display first few rows of the dataframe
print(df.head())

# Summary statistics
print(df.describe())
# Plot histograms for numerical variables
print(df.columns)

# Plot histograms for numerical variables
plt.figure(figsize=(10, 6))
plt.hist(df['Country'], bins=20, edgecolor='black')
plt.title('Histogram of Country')
plt.xlabel('Country')
plt.show()

# Boxplot to visualize distribution and outliers
plt.figure(figsize=(10, 6))
sns.boxplot(x='Country', y='Salary', data=df)
plt.title('Boxplot of Country by Salary')
plt.show()
# Scatter plot to identify outliers
plt.figure(figsize=(10, 6))
plt.scatter(df['Country'], df['Age'])
plt.title('Scatter Plot of Country vs. Age')
plt.xlabel('Country')
plt.ylabel('Age')
plt.show()
# Calculate correlation matrix
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns

# Calculate correlation matrix for numeric columns only
correlation_matrix = df[numeric_columns].corr()

# Plot heatmap of correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix of Numeric Variables')
plt.show()


# In[ ]:




