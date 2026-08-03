"""
Program 9: Correlation Heatmaps and Categorical Cross-tabulations
--------------------------------------------------------------------
Aim:
    To write a Python program to visualize a correlation matrix and a
    categorical cross-tabulation using Seaborn heatmaps with annotations
    and custom color maps.

Concepts Covered:
    - Correlation matrix
    - Seaborn heatmap()
    - Diverging vs sequential colormaps
    - Cross-tabulation (pd.crosstab)
    - Masking the upper triangle
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# Step 1: Create a synthetic student dataset
# ---------------------------------------------------------------
np.random.seed(42)
n = 200

# Numeric columns (correlated on purpose so the heatmap is interesting)
study_hours = np.random.normal(5, 1.5, n)
attendance = study_hours * 8 + np.random.normal(0, 5, n)          # +ve corr with study_hours
sleep_hours = 9 - 0.4 * study_hours + np.random.normal(0, 0.8, n) # -ve corr with study_hours
marks = study_hours * 10 + attendance * 0.3 + np.random.normal(0, 8, n)
screen_time = 6 - 0.5 * study_hours + np.random.normal(0, 1, n)   # -ve corr with study_hours

# Categorical columns
gender = np.random.choice(['Male', 'Female'], size=n)
grade = pd.cut(marks, bins=[-np.inf, 50, 65, 80, np.inf],
               labels=['D', 'C', 'B', 'A'])

df = pd.DataFrame({
    'Study_Hours': study_hours,
    'Attendance': attendance,
    'Sleep_Hours': sleep_hours,
    'Marks': marks,
    'Screen_Time': screen_time,
    'Gender': gender,
    'Grade': grade
})

print("Sample of the dataset:")
print(df.head(), "\n")

# ---------------------------------------------------------------
# Step 2: Compute the correlation matrix (numeric columns only)
# ---------------------------------------------------------------
numeric_cols = ['Study_Hours', 'Attendance', 'Sleep_Hours', 'Marks', 'Screen_Time']
corr_matrix = df[numeric_cols].corr()
print("Correlation matrix:")
print(corr_matrix.round(2), "\n")

# Mask the upper triangle (keep the diagonal + lower triangle visible)
mask = np.triu(np.ones_like(corr_matrix, dtype=bool), k=1)

# ---------------------------------------------------------------
# Step 3: Compute the Grade x Gender cross-tabulation
# ---------------------------------------------------------------
cross_tab = pd.crosstab(df['Grade'], df['Gender'])
print("Grade x Gender cross-tabulation:")
print(cross_tab, "\n")

# ---------------------------------------------------------------
# Step 4: Plot both heatmaps side by side
# ---------------------------------------------------------------
sns.set_style("white")
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Left panel: lower-triangular correlation heatmap (diverging colormap)
sns.heatmap(
    corr_matrix,
    mask=mask,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    vmin=-1, vmax=1,
    center=0,
    square=True,
    linewidths=0.5,
    cbar_kws={"shrink": 0.8, "label": "Correlation coefficient"},
    ax=axes[0]
)
axes[0].set_title("Correlation Matrix (Lower Triangle)\nDiverging colormap: coolwarm",
                   fontsize=12, fontweight="bold")

# Right panel: Grade x Gender cross-tab heatmap (sequential colormap)
sns.heatmap(
    cross_tab,
    annot=True,
    fmt="d",
    cmap="GnBu",
    linewidths=0.5,
    cbar_kws={"shrink": 0.8, "label": "Count"},
    ax=axes[1]
)
axes[1].set_title("Grade x Gender Cross-tabulation\nSequential colormap: GnBu",
                   fontsize=12, fontweight="bold")
axes[1].set_ylabel("Grade")
axes[1].set_xlabel("Gender")

plt.tight_layout()
plt.savefig("/DV/program9_heatmaps.png", dpi=150)
plt.show()

print("Plot saved as program9_heatmaps.png")