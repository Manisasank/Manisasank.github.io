import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# 1. Create a Synthetic Dataset
np.random.seed(42)
n_students = 50

# Generated data: Study hours, Exam scores, and Attendance %
study_hours = np.random.uniform(2, 10, n_students)
# Exam scores generated with a positive linear relation + noise
exam_scores = 5 * study_hours + 35 + np.random.normal(0, 5, n_students)
exam_scores = np.clip(exam_scores, 0, 100) # Keep scores between 0 and 100
# Attendance correlated with study hours
attendance = np.clip(50 + 5 * study_hours + np.random.normal(0, 8, n_students), 40, 100)

df = pd.DataFrame({
    'Study_Hours': study_hours,
    'Exam_Score': exam_scores,
    'Attendance': attendance
})

# 2. Compute Pearson Correlation Coefficient
r_val, p_val = stats.pearsonr(df['Study_Hours'], df['Exam_Score'])
print(f"--- Correlation Analysis ---")
print(f"Pearson Correlation Coefficient (r): {r_val:.4f}")
print(f"p-value: {p_val:.4e}\n")

# 3. Fit Least-Squares Regression Line
slope, intercept, r_value, p_value, std_err = stats.linregress(df['Study_Hours'], df['Exam_Score'])
line_eq = f"Fit: y = {slope:.2f}x + {intercept:.2f}"

# 4. Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Scatter Plot with Regression Line
ax1.scatter(df['Study_Hours'], df['Exam_Score'], color='royalblue', alpha=0.7, label='Data Points')
x_vals = np.linspace(df['Study_Hours'].min(), df['Study_Hours'].max(), 100)
ax1.plot(x_vals, slope * x_vals + intercept, color='firebrick', linewidth=2, label=line_eq)

ax1.set_title("Study Hours vs Exam Score")
ax1.set_xlabel("Hours Studied")
ax1.set_ylabel("Exam Score")
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend()

# Plot 2: Bubble Chart (3rd variable encoded via Size & Color)
# Scaling size for visual appeal (marker area in points^2)
sizes = (df['Attendance'] / 10) ** 2.2 

scatter = ax2.scatter(
    df['Study_Hours'], 
    df['Exam_Score'], 
    s=sizes, 
    c=df['Attendance'], 
    cmap='viridis', 
    alpha=0.6, 
    edgecolors='black', 
    linewidth=0.5
)

cbar = fig.colorbar(scatter, ax=ax2)
cbar.set_label('Attendance (%)')

ax2.set_title("Bubble Chart (Size & Color = Attendance %)")
ax2.set_xlabel("Hours Studied")
ax2.set_ylabel("Exam Score")
ax2.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()