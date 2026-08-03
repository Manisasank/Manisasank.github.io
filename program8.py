import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. Generate Synthetic Daily Time-Series
# ==========================================
np.random.seed(42)  # For reproducible random data

# Create a full year of daily dates for 2025
dates = pd.date_range(start="2025-01-01", end="2025-12-31", freq="D")

# Generate a random walk to simulate daily closing stock prices
random_walk = np.random.normal(loc=0.1, scale=1.5, size=len(dates)).cumsum()
initial_price = 100.0
closing_prices = initial_price + random_walk

# Create DataFrame with a DatetimeIndex
df = pd.DataFrame({"Close": closing_prices}, index=dates)

# ==========================================
# 2. Moving Averages & Resampling
# ==========================================
# Compute 7-day and 30-day rolling (moving) averages
df["MA7"] = df["Close"].rolling(window=7).mean()
df["MA30"] = df["Close"].rolling(window=30).mean()

# Resample daily data to compute monthly average closing prices ('ME' = Month End)
monthly_df = df["Close"].resample("ME").mean()
# Format month labels as abbreviated month names (Jan, Feb, Mar, ...)
month_labels = monthly_df.index.strftime("%b")

# ==========================================
# 3. Visualization (Two Panels)
# ==========================================
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(12, 8), sharex=False)
fig.suptitle("Time Series Analysis: Daily Prices vs. Monthly Trends", fontsize=14, fontweight="bold")

# --- Top Panel: Daily Prices and Moving Averages ---
ax1.plot(df.index, df["Close"], color="lightgray", label="Daily Price", alpha=0.8, linewidth=1)
ax1.plot(df.index, df["MA7"], color="#1f77b4", label="7-Day Moving Avg", linewidth=1.5)
ax1.plot(df.index, df["MA30"], color="#d62728", label="30-Day Moving Avg", linewidth=2)

ax1.set_title("Daily Closing Price & Rolling Averages")
ax1.set_ylabel("Price ($)")
ax1.legend(loc="upper left")
ax1.grid(True, linestyle="--", alpha=0.5)

# --- Bottom Panel: Monthly Resampled Averages ---
bars = ax2.bar(month_labels, monthly_df.values, color="#4c72b0", edgecolor="black", alpha=0.85, width=0.6)

ax2.set_title("Monthly Average Closing Price")
ax2.set_xlabel("Month")
ax2.set_ylabel("Average Price ($)")
ax2.grid(True, linestyle="--", alpha=0.5, axis="y")

# Optional: Add data labels above each bar for clarity
for bar in bars:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f"{yval:.1f}", ha="center", va="bottom", fontsize=9)

plt.tight_layout()
plt.show()