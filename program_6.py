import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os

plt.style.use("seaborn-v0_8-whitegrid")
np.random.seed(3)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = np.array([120, 135, 128, 160, 175, 210])
expense = np.array([90, 95, 100, 110, 120, 130])

region_share = [35, 25, 20, 20]
regions = ["North", "South", "East", "West"]

fig = plt.figure(figsize=(12, 8))
gs = gridspec.GridSpec(2, 2, height_ratios=[1.2, 1], width_ratios=[1.4, 1])

ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(months, sales, marker="o", color="#0D4BAE", label="Sales (Rs. Lakh)")
ax1.plot(months, expense, marker="s", color="#551C8B", label="Expense (Rs. Lakh)")
peak_idx = int(np.argmax(sales))
ax1.annotate("Peak Sales", xy=(months[peak_idx], sales[peak_idx]),
	     xytext=(peak_idx - 1.5, sales[peak_idx] + 20),
	     arrowprops=dict(facecolor="black", arrowstyle="->"))
ax1.set_title("Monthly Sales vs Expense")
ax1.legend()

ax2 = fig.add_subplot(gs[0, 1])
ax2.pie(region_share, labels=regions, autopct="%1.0f%%", startangle=90,
	colors=plt.cm.Pastel1.colors)
ax2.set_title("Region-wise Sales Share")

ax3 = fig.add_subplot(gs[1, 0])
profit = sales - expense
ax3.bar(months, profit, color=np.where(profit > 40, "#286D0FD6", "#843E16F5"))
ax3.set_title("Monthly Profit (Sales - Expense)")
ax3.set_ylabel("Rs. Lakh")

ax4 = fig.add_subplot(gs[1, 1])
ax4.fill_between(months, np.cumsum(sales), color="#0B29A2BA", alpha=0.6)
ax4.set_title("Cumulative Sales")

fig.suptitle("Company Performance Dashboard (Static)", fontsize=16, fontweight="bold")
plt.tight_layout(rect=[0, 0, 1, 0.96])
out = "program6_gridspec_dashboard.png"
plt.savefig(out, dpi=150)
print("Saved image:", os.path.abspath(out))
plt.show()  # commented out for non-interactive runs