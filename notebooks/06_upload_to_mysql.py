import pandas as pd
import mysql.connector
import numpy as np

# Load your final CSV
df = pd.read_csv("../data/final_pit_strategy_data.csv")

# Drop rows that have any missing values in the required columns
df = df.dropna(subset=['driverId', 'avg_pit_duration', 'positionOrder', 'pit_stops'])

# Convert types safely
df['avg_pit_duration'] = df['avg_pit_duration'].astype(float)
df['positionOrder'] = df['positionOrder'].astype(int)
df['pit_stops'] = df['pit_stops'].astype(int)

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="f1_pit_strategy"
)
cursor = conn.cursor()

# Insert data row by row
for _, row in df.iterrows():
    sql = """
    INSERT INTO pit_strategy (driverId, avg_pit_duration, positionOrder, pit_stops)
    VALUES (%s, %s, %s, %s)
    """
    values = (
        str(row['driverId']),
        float(row['avg_pit_duration']),
        int(row['positionOrder']),
        int(row['pit_stops'])
    )
    cursor.execute(sql, values)

# Commit and close connection
conn.commit()
cursor.close()
conn.close()

print("✅ Data uploaded successfully!")
