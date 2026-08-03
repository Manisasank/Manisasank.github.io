import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
np.random.seed(7)
n = 80
study_hours = np.random.uniform(1, 10, n)
attendance  = np.random.uniform(50, 100, n)
marks = 5*study_hours + 0.4*attendance + np.random.normal(0, 8, n)
df = pd.DataFrame({"StudyHours": study_hours,
    "Attendance": attendance, "Marks": marks})
 
corr = df["StudyHours"].corr(df["Marks"])
print(f"Pearson correlation: {corr:.3f}")
 
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
 
axes[0].scatter(df["StudyHours"], df["Marks"],
    color="#4C72B0", alpha=0.7, edgecolor="white")
m, b = np.polyfit(df["StudyHours"], df["Marks"], 1)
x_line = np.linspace(study_hours.min(), study_hours.max(), 100)
axes[0].plot(x_line, m*x_line + b, color="crimson",
    linewidth=2, label=f"y = {m:.2f}x + {b:.2f}")
axes[0].set_title(f"Study Hours vs Marks (r = {corr:.2f})")
axes[0].legend()
 
bubble = axes[1].scatter(df["StudyHours"], df["Marks"],
    s=df["Attendance"], c=df["Attendance"],
    cmap="viridis", alpha=0.75, edgecolor="white")
axes[1].set_title("Bubble Chart (size/color = Attendance %)")
plt.colorbar(bubble, ax=axes[1], label="Attendance %")
 
plt.tight_layout()
plt.savefig("program5_scatter.png", dpi=150)
plt.show()