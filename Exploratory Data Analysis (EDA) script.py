# %% [markdown]
# #  Exploratory Data Analysis (EDA) Report
# **Dataset:** gender_submission.csv (Titanic - Test Set)
# 

# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('gender_submission.csv')

# %%
print("📄 Dataset Info:")
print(df.info())
df.head()

# %%
print("📊 Statistical Summary:")
df.describe()

# %%
sns.set(style='whitegrid')
plt.figure(figsize=(6, 4))
sns.countplot(x='Survived', data=df, palette='viridis')
plt.title('Survival Count')
plt.xlabel('Survived (1 = Yes, 0 = No)')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# %%
plt.figure(figsize=(8, 4))
sns.histplot(df['PassengerId'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Passenger IDs')
plt.xlabel('Passenger ID')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# %%
plt.figure(figsize=(6, 4))
sns.boxplot(x='Survived', y='PassengerId', data=df, palette='Set2')
plt.title('PassengerId Distribution by Survival')
plt.xlabel('Survived')
plt.ylabel('Passenger ID')
plt.tight_layout()
plt.show()

# %%
plt.figure(figsize=(4, 3))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

# %% [markdown]
# ### 📝 Summary of Insights:
# - Approximately 36% of passengers in this dataset survived.
# - Countplot shows significantly more non-survivors than survivors.
# - Passenger IDs are uniformly distributed; no survival pattern observed by ID.
# - Boxplot indicates survival is independent of ID range.
# - Correlation heatmap confirms weak/no correlation between PassengerId and Survived.
# 
# 📌 **Note:** To draw stronger insights, join this with the full Titanic dataset containing `Age`, `Sex`, `Pclass`, etc.


