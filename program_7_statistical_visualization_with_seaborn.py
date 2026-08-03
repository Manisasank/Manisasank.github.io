import matplotlib.pyplot as plt
import seaborn as sns
# Set a clean default style for Seaborn
sns.set_theme(style="whitegrid")
# ==========================================
# 1. Load Data & Display Summary Statistics
# ==========================================
# Load the classic Iris dataset directly from Seaborn
iris = sns.load_dataset("iris")
print("--- First 5 Rows of the Iris Dataset ---")
print(iris.head())
print("\n" + "=" * 50 + "\n")
print("--- Grouped Descriptive Statistics (Mean & Std) ---")
grouped_stats = iris.groupby("species").agg(["mean", "std"])
print(grouped_stats)
print("\n" + "=" * 50 + "\n")
# ==========================================
# 2. Figure 1: Distribution & Violin Plots
# ==========================================
# Create a figure with 2 side-by-side subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
# Subplot 1: Step Histogram with KDE overlay for Petal Length across Species
sns.histplot(
    data=iris,
    x="petal_length",
    hue="species",
    element="step",
    kde=True,
    ax=axes[0],
)
axes[0].set_title(
    "Distribution of Petal Length by Species", fontsize=12, fontweight="bold"
)
axes[0].set_xlabel("Petal Length (cm)")
axes[0].set_ylabel("Count")
# Subplot 2: Violin Plot comparing Sepal Width spread per Species
sns.violinplot(
    data=iris,
    x="species",
    y="sepal_width",
    hue="species",
    palette="Set2",
    inner="quartile",
    ax=axes[1],
)
axes[1].set_title(
    "Sepal Width Spread by Species", fontsize=12, fontweight="bold"
)
axes[1].set_xlabel("Species")
axes[1].set_ylabel("Sepal Width (cm)")
plt.tight_layout()
plt.show()
# ==========================================
# 3. Figure 2: Pairwise Relationship Plot
# ==========================================
# Create a full corner pairplot color-coded by species
pair_fig = sns.pairplot(
    iris, hue="species", corner=True, diag_kind="kde", palette="bright"
)
pair_fig.figure.suptitle(
    "Pairwise Feature Relationships in Iris Dataset",
    y=1.02,
    fontsize=14,
    fontweight="bold",
)
plt.show()