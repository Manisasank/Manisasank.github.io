import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Iris Dataset
iris = sns.load_dataset("iris")

# Display first 5 rows
print("First 5 Rows of Iris Dataset:")
print(iris.head())

# Grouped Descriptive Statistics
print("\nGrouped Descriptive Statistics:")
print(iris.groupby("species").describe())

# -------------------------------
# Histogram with KDE
# -------------------------------
plt.figure(figsize=(8,5))
sns.histplot(
    data=iris,
    x="petal_length",
    hue="species",
    kde=True,
    element="step"
)
plt.title("Distribution of Petal Length")
plt.xlabel("Petal Length")
plt.ylabel("Count")
plt.show()

# -------------------------------
# Violin Plot
# -------------------------------
plt.figure(figsize=(8,5))
sns.violinplot(
    data=iris,
    x="species",
    y="sepal_width"
)
plt.title("Sepal Width Spread by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Width")
plt.show()

# -------------------------------
# Pair Plot
# -------------------------------
sns.pairplot(
    iris,
    hue="species",
    diag_kind="kde"
)

plt.show()