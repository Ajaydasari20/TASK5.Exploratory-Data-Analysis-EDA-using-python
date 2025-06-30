# 🧠 Titanic Survival EDA using Python

This repository contains an exploratory data analysis (EDA) of the Titanic prediction dataset using Python. The analysis was conducted using pandas, seaborn, and matplotlib.

## 📁 Files

- `Exploratory Data Analysis (EDA) script.py` — Python script for EDA.
- `EDA data analysis using python.pdf` — PDF report with visuals and insights.

## 🔍 Key Insights

- Approximately 36% of passengers in this test dataset survived.
- Passenger ID does not correlate with survival outcome.
- Visualization techniques like countplots, histograms, boxplots, and heatmaps were used.

## 🛠️ Libraries Used

- pandas
- seaborn
- matplotlib

## 📌 Note

For deeper analysis, consider combining with the full Titanic dataset (`train.csv`) that includes features like age, sex, class, etc.

---

📬 Feel free to fork or star ⭐ this repo!

# 🧠 Titanic Test Dataset - Exploratory Data Analysis (EDA)

This repository contains an exploratory data analysis of the **Titanic test dataset (`test.csv`)** using Python, including visual and statistical exploration.

## 📂 Files Included

| File Name              | Description |
|------------------------|-------------|
| `EDA .TEXT SCRIPT.py`  | Python script with step-by-step EDA |
| `EDA .TEXT analysis.pdf` | PDF version of the analysis report |
| `test.csv`             | Dataset used for EDA (should be added manually if not visible) |

## 🛠️ Libraries Used

- `pandas` – for data manipulation
- `seaborn` – for data visualization
- `matplotlib` – for plotting charts

## 🔍 Key EDA Steps Performed

- Dataset structure and summary statistics
- Handling missing values
- Count plots (e.g., Gender distribution)
- Histogram for Age
- Boxplots for Age vs Pclass
- Correlation heatmap

## 🧾 Sample Insights

- Missing values are mostly in `Age`, `Fare`, and `Cabin`.
- Most passengers in the test set belong to **Pclass 3**.
- The majority of passengers are **male**.
- Some correlation exists between **Fare** and **Pclass**.

## 📌 Note

This is part of the Titanic Machine Learning project. For deeper insights or model-building, consider merging this test set with `train.csv`.

---

## 👨‍💻 How to Run

```bash
# Step 1: Install dependencies
pip install pandas seaborn matplotlib

# Step 2: Run the Python script
python "EDA .TEXT SCRIPT.py"

