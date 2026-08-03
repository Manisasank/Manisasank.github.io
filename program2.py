import matplotlib.pyplot as plt
import numpy as np

# Sample Data
subjects = ['Math', 'Science', 'English', 'History', 'Art']
marks_2024 = [85, 78, 92, 65, 88]
marks_2025 = [89, 84, 90, 72, 95]

x = np.arange(len(subjects))  # Label locations
width = 0.35  # Width of the bars

# Create a figure with two panels side-by-side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# ----------------------------------------------------
# PANEL 1: Grouped Bar Chart (2024 vs 2025 Marks)
# ----------------------------------------------------
rects1 = ax1.bar(x - width/2, marks_2024, width, label='2024', color="#100068")
rects2 = ax1.bar(x + width/2, marks_2025, width, label='2025', color="#ce0606b2")

# Labels, titles, and ticks
ax1.set_ylabel('Marks')
ax1.set_title('Subject-wise Performance Comparison (2024 vs 2025)')
ax1.set_xticks(x)
ax1.set_xticklabels(subjects)
ax1.legend()
ax1.set_ylim(0, 110)  # Extra space for data labels

# Add data labels above the bars
ax1.bar_label(rects1, padding=3)
ax1.bar_label(rects2, padding=3)

# ----------------------------------------------------
# PANEL 2: Pie Chart (2025 Marks Distribution)
# ----------------------------------------------------
colors = ["#0c9580", "#29004a", "#8348008B", '#8064a2', '#4bacc6']
# autopct='%1.1f%%' formats the labels to show one decimal place
wedges, texts, autotexts = ax2.pie(
    marks_2025, 
    labels=subjects, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors,
    textprops=dict(color="black")
)

# Stylizing the pie chart text labels for readability
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')

ax2.set_title("Subject's Percentage Share of Total 2025 Marks")

# Display the charts
plt.tight_layout()
plt.show()