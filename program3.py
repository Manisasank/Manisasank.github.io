# Program 4: Box plots and outlier detection
# Aim: Study the marks distribution of 4 sections (A, B, C, D) using
# descriptive statistics and visualize spread and outliers with box plots.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(7)
sectionA = np.random.normal(loc=70, scale=5, size=40)
sectionB = np.random.normal(loc=65, scale=8, size=40)
sectionC = np.random.normal(loc=60, scale=10, size=40)
sectionD = np.random.normal(loc=72, scale=6, size=40)

# Manually insert extreme outliers into Section C for verification
sectionC = np.concatenate([sectionC, [15, 20, 98, 99]])

data = {
    "Section A": sectionA,
    "Section B": sectionB,
    "Section C": sectionC,
    "Section D": sectionD,
}


def find_outliers(values):
    q1 = np.percentile(values, 25)
    q3 = np.percentile(values, 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = values[(values < lower_bound) | (values > upper_bound)]
    return outliers, lower_bound, upper_bound

print("Descriptive statistics per section:\n")

for name, values in data.items():
    series = pd.Series(values)
    print(f"--- {name} ---")
    print(f"Count: {series.count():.0f}")
    print(f"Mean: {series.mean():.2f}")
    print(f"Std Dev: {series.std():.2f}")
    print(f"Min: {series.min():.2f}")
    print(f"Q1: {series.quantile(0.25):.2f}")
    print(f"Median: {series.median():.2f}")
    print(f"Q3: {series.quantile(0.75):.2f}")
    print(f"Max: {series.max():.2f}")
    outliers, lower_bound, upper_bound = find_outliers(values)
    if len(outliers) > 0:
        print(
            f"Outliers: {np.round(outliers, 2).tolist()} "
            f"(bounds: {lower_bound:.2f} to {upper_bound:.2f})"
        )
    else:
        print("Outliers: None")
    print()

print("Y Mani sasank reddy (24CAM1071) - B.Tech CSE(AI&ML) 6")

# Visualizing via side-by-side boxplots
fig, ax = plt.subplots(figsize=(9, 6))
colors = ["#25af45", "#174da3", "#B70F1F", "#d48e14"]
box = ax.boxplot(
    list(data.values()),
    patch_artist=True,
    flierprops=dict(marker="o", markerfacecolor="black", markersize=5, alpha=0.6),
)
ax.set_xticklabels(list(data.keys()))
for patch, color in zip(box["boxes"], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.6)

ax.set_title("Box Plots of Marks Across Sections")
ax.set_xlabel("Section")
ax.set_ylabel("Marks")
ax.yaxis.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("program4_boxplot.png", dpi=150)
plt.show()
