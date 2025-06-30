# %%
# import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# %%
# load database
df=pd.read_csv("test.csv")

# %%
# basic info
print("dataset info")
print(df.info(),"\n")

# %%
# display the 1st 5 rows 
print("first 5 rows")
print(df.head(),"\n")

# %%
# display the statitics 
print("statistical summary")
print(df.describe(include="all"))

# %%
# missing values 
print("\n ? missingvalue")
print(df.isnull().sum())

# %%
# count of the passengers with sex
plt.figure(figsize=(6,4))
sns.countplot(data=df,x='Sex', palette='Set2')
plt.tittle("passengers count with sex")
plt.xlabel('sex')
plt.ylabel('count')
plt.taight_layout()
plt.show()

# %%
# visual age distribution
plt.figure(figsize=(8, 4))
sns.histplot(df['Age'].dropna(), bins=30, kde=True, color='skyblue')
plt.title('Age Distribution of Passengers')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# %%
# pclass vs age
plt.figure(figsize=(8, 5))
sns.boxplot(x='Pclass', y='Age', data=df, palette='pastel')
plt.title('Age Distribution by Passenger Class')
plt.tight_layout()
plt.show()


# %%
# heat map 
plt.figure(figsize=(6, 4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

# %%
# Summary of insights
print("\n📝 EDA Summary:")
print("""
- The dataset contains test set data for Titanic survivors.
- Missing values commonly found in 'Age', 'Fare', and 'Cabin'.
- Most passengers in this test set are in Pclass 3.
- Majority of passengers are male.
- There's some correlation between Fare and Pclass.
""")

# %%



