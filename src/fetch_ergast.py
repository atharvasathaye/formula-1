import requests
import pandas as pd

def fetch_ergast_results(year, round_num):
    url = f"https://ergast.com/api/f1/{year}/{round_num}/results.json"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"❌ No Ergast data for Round {round_num}")
        return None

    race_data = response.json()
    try:
        results = race_data['MRData']['RaceTable']['Races'][0]['Results']
        data = []
        for r in results:
            entry = {
                'Driver': r['Driver']['driverId'],
                'Constructor': r['Constructor']['name'],
                'Position': int(r['position']),
                'Grid': int(r['grid']),
                'Status': r['status'],
                'FastestLapRank': int(r['FastestLap']['rank']) if 'FastestLap' in r else None
            }
            data.append(entry)

        df = pd.DataFrame(data)
        filename = f"data/{year}_round{round_num}_ergast.csv"
        df.to_csv(filename, index=False)
        print(f"✔ Saved Ergast data for Round {round_num}")
        return filename
    except Exception as e:
        print(f"⚠ Failed parsing Ergast: {e}")
        return None