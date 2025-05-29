import pandas as pd

# Load data
pit_df = pd.read_csv('../data/pitstops_2021_round10.csv')
result_df = pd.read_csv('../data/results_2021_round10.csv')

# Convert duration to seconds again
def convert_to_seconds(time_str):
    if ':' in str(time_str):
        minutes, seconds = time_str.split(':')
        return int(minutes) * 60 + float(seconds)
    try:
        return float(time_str)
    except:
        return None

pit_df['duration_seconds'] = pit_df['duration'].apply(convert_to_seconds)

# Group pit data: total stops and avg duration per driver
pit_summary = pit_df.groupby('driverId').agg(
    pit_stops=('stop', 'count'),
    avg_pit_duration=('duration_seconds', 'mean')
).reset_index()

# Get driverId and position from result data
# Print available columns to inspect
print(result_df.columns)

# Adjust column selection based on actual column names
result_df_summary = result_df[['Driver.driverId', 'position']].copy()
result_df_summary.rename(columns={
    'Driver.driverId': 'driverId',
    'position': 'positionOrder'
}, inplace=True)
result_df_summary['positionOrder'] = result_df_summary['positionOrder'].astype(int)

result_df_summary['positionOrder'] = result_df_summary['positionOrder'].astype(int)

# Merge datasets
combined_df = pd.merge(result_df_summary, pit_summary, on='driverId', how='left')

combined_df.sort_values('positionOrder', inplace=True)

print(combined_df)


# Add this
import seaborn as sns
import matplotlib.pyplot as plt

# Bar plot: Pit Stops vs Final Position
plt.figure(figsize=(10, 6))
sns.barplot(data=combined_df, x='driverId', y='pit_stops', order=combined_df['driverId'])
plt.title('Number of Pit Stops by Driver (sorted by Finish Position)')
plt.xticks(rotation=90)
plt.ylabel('Number of Pit Stops')
plt.show()

# Scatter plot: Avg Pit Duration vs Final Position
plt.figure(figsize=(10, 6))
sns.scatterplot(data=combined_df, x='avg_pit_duration', y='positionOrder', hue='driverId')
plt.title('Avg Pit Duration vs Final Position')
plt.xlabel('Avg Pit Duration (s)')
plt.ylabel('Finishing Position (1 = best)')
plt.gca().invert_yaxis()
plt.show()