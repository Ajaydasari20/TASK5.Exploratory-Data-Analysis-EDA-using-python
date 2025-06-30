# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("gender_submission.csv")

# Basic info
print("📄 Dataset Info:")
print(df.info(), "\n")

# Display first few rows
print("🔍 First 5 Records:")
print(df.head(), "\n")

# Descriptive statistics
print("📊 Statistical Summary:")
print(df.describe(), "\n")

# Countplot of Survived
plt.figure(figsize=(6, 4))
sns.countplot(x='Survived', data=df, palette='viridis')
plt.title('Survival Count')
plt.xlabel('Survived (1 = Yes, 0 = No)')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Histogram of PassengerId
plt.figure(figsize=(8, 4))
sns.histplot(df['PassengerId'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Passenger IDs')
plt.xlabel('Passenger ID')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Boxplot of PassengerId grouped by Survived
plt.figure(figsize=(6, 4))
sns.boxplot(x='Survived', y='PassengerId', data=df, palette='Set2')
plt.title('PassengerId Distribution by Survival')
plt.xlabel('Survived')
plt.ylabel('Passenger ID')
plt.tight_layout()
plt.show()

# Heatmap of correlation (limited here)
plt.figure(figsize=(4, 3))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

# Summary of findings
print("📝 Summary of Insights:")
print("""
1. Around 36% of passengers in this test set are predicted to have survived.
2. The survival count plot shows that non-survivors are significantly more.
3. No direct pattern in PassengerId and survival, but ID range is evenly spread.
4. Correlation heatmap shows minimal correlation due to only 2 numeric fields.

Note: For deeper insights, include additional features like Age, Sex, Pclass etc.
""")
