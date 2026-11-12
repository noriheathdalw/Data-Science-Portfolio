"""
Departure delays by time of day — American Airlines, JFK, January 2025
Data: U.S. Bureau of Transportation Statistics, "Detailed Statistics Departures"
      https://www.transtats.bts.gov/ONTIME/Departures.aspx
Usage: python3 analysis.py [path_to_csv]
"""
import sys
import pandas as pd
import numpy as np

SRC = sys.argv[1] if len(sys.argv) > 1 else "Detailed_Statistics_Departures.csv"

# ---------------------------------------------------------------- load & clean
# BTS report has a 6-line header block before the CSV header row
df = pd.read_csv(SRC, skiprows=6).dropna()

df["date"] = pd.to_datetime(df["Date (MM/DD/YYYY)"], format="%m/%d/%Y")
df["sched"] = pd.to_datetime(df["Scheduled departure time"], format="%H:%M")
df["hour"] = df["sched"].dt.hour
df["delay"] = df["Departure delay (Minutes)"]
df = df[df["hour"].notna()].copy()
df["dow"] = df["date"].dt.day_of_week  # 0 = Monday

# ------------------------------------------------------------------ summaries
hourly = df.groupby("hour")["delay"].agg(
    flights="size", mean="mean", median="median", p90=lambda x: x.quantile(0.9),
    pct_delayed_15=lambda x: (x >= 15).mean() * 100,
    pct_delayed_60=lambda x: (x >= 60).mean() * 100,
).round(1)
print("=== Delay by scheduled departure hour ===")
print(hourly.to_string())

dnames = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
dow = df.groupby("dow")["delay"].agg(
    flights="size", mean="mean", median="median",
    pct_delayed_15=lambda x: (x >= 15).mean() * 100,
).round(1).rename(index=dict(enumerate(dnames)))
print("\n=== Delay by day of week ===")
print(dow.to_string())

# Aircraft sequence within a day (delay propagation check)
df = df.sort_values(["Tail Number", "date", "sched"])
df["leg"] = df.groupby(["Tail Number", "date"]).cumcount() + 1
leg = df.groupby("leg")["delay"].agg(
    flights="size", mean="mean", median="median",
    pct_delayed_15=lambda x: (x >= 15).mean() * 100,
).round(1)
print("\n=== Delay by flight leg of the day (same aircraft) ===")
print(leg.head(5).to_string())

print("\n=== Overall ===")
print(f"n={len(df)}, mean={df['delay'].mean():.1f} min, median={df['delay'].median():.0f} min, "
      f">=15 min late: {(df['delay'] >= 15).mean()*100:.1f}%, "
      f">=60 min late: {(df['delay'] >= 60).mean()*100:.1f}%")
