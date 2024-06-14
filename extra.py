# All in one file

# Import python libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # Visualizing data
%matplotlib inline
import seaborn as sns

# Import csv file
df = pd.read_csv('Sales Data.csv', encoding='unicode_escape')

# Print the shape of the dataframe
print("Shape of the dataframe:", df.shape)

# Display the first few rows of the dataframe
print("First few rows of the dataframe:")
print(df.head())

# Display information about the dataframe
print("Information about the dataframe:")
print(df.info())

# Drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)

# Check for null values
print("Null values in the dataframe:")
print(pd.isnull(df).sum())

# Drop null values
df.dropna(inplace=True)

# Change data type
df['Amount'] = df['Amount'].astype('int')

# Print the data type of 'Amount' column
print("Data type of 'Amount' column:", df['Amount'].dtypes)

# Print column names
print("Column names:", df.columns)

# Rename column
df.rename(columns={'Marital_Status': 'Shaadi'}, inplace=True)

# Display descriptive statistics
print("Descriptive statistics of the dataframe:")
print(df.describe())

# Display descriptive statistics for specific columns
print("Descriptive statistics for specific columns:")
print(df[['Age', 'Orders', 'Amount']].describe())

# EDA

# Plot a bar chart for Gender and its count
ax = sns.countplot(x='Gender', data=df)
for bars in ax.containers:
    ax.bar_label(bars)

# Plot a bar chart for gender vs total amount
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Gender', y='Amount', data=sales_gen)

# Plot a bar chart for Age Group and Gender
ax = sns.countplot(data=df, x='Age Group', hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)

# Plot total amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Age Group', y='Amount', data=sales_age)

# Total number of orders from top 10 states
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.barplot(data=sales_state, x='State', y='Orders')

# Total amount/sales from top 10 states
sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.barplot(data=sales_state, x='State', y='Amount')

# Plot a bar chart for Marital Status
ax = sns.countplot(data=df, x='Marital_Status')
for bars in ax.containers:
    ax.bar_label(bars)

# Plot total amount by Marital Status and Gender
sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(data=sales_state, x='Marital_Status', y='Amount', hue='Gender')

# Plot a bar chart for Occupation
ax = sns.countplot(data=df, x='Occupation')
for bars in ax.containers:
    ax.bar_label(bars)

# Plot total amount by Occupation
sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(data=sales_state, x='Occupation', y='Amount')

# Plot a bar chart for Product Category
ax = sns.countplot(data=df, x='Product_Category')
for bars in ax.containers:
    ax.bar_label(bars)

# Plot total amount by Product Category
sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.barplot(data=sales_state, x='Product_Category', y='Amount')

# Plot total number of orders by Product ID
sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.barplot(data=sales_state, x='Product_ID', y='Orders')

# Plot top 10 most sold products
fig1, ax1 = plt.subplots(figsize=(12, 7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')

# Conclusion
print("""
Conclusion:
Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category 
""")
