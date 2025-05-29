import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the pit stop data
df = pd.read_csv('../data/pitstops_2021_round14.csv')

# Helper: Convert MM:SS.sss to total seconds
def convert_to_seconds(time_str):
    if ':' in str(time_str):
        minutes, seconds = time_str.split(':')
        return int(minutes) * 60 + float(seconds)
    try:
        return float(time_str)
    except:
        return None

# Apply conversion
df['duration_seconds'] = df['duration'].apply(convert_to_seconds)


# Plot pit stop durations
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='driverId', y='duration_seconds')
plt.xticks(rotation=90)
plt.title("Pit Stop Duration by Driver - 2021 Italian GP")
plt.xlabel("Driver")
plt.ylabel("Pit Stop Duration (s)")
plt.tight_layout()
plt.show()\

 