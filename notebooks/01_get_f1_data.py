import requests
import pandas as pd

year = 2021
round_number = 10  # British GP

# Race results endpoint
url = f"http://ergast.com/api/f1/{year}/{round_number}/results.json"

res = requests.get(url)

if res.status_code == 200:
    data = res.json()
    race_results = data['MRData']['RaceTable']['Races'][0]['Results']
    
    df_results = pd.json_normalize(race_results)
    df_results.to_csv(f"../data/results_{year}_round{round_number}.csv", index=False)
    print("Results saved.")
else:
    print("Failed to fetch race results.")
