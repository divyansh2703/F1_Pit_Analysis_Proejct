import requests
import pandas as pd

year = 2021
round_number = 14

url = f"http://ergast.com/api/f1/{year}/{round_number}/pitstops.json?limit=100"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    pit_stops = data['MRData']['RaceTable']['Races'][0]['PitStops']
    df = pd.DataFrame(pit_stops)
    print(df.head())

    df.to_csv(f"../data/pitstops_{year}_round{round_number}.csv", index=False)
    print("Data saved.")
else:
    print("Failed to fetch data:", response.status_code)
