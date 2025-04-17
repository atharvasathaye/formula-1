import fastf1
import pandas as pd
import os

fastf1.Cache.enable_cache('cache')

def fetch_fastf1_race(year, race_name):
    try:
        session = fastf1.get_session(year, race_name, 'R')
        session.load()
        laps = session.laps
        laps = laps.reset_index(drop=True)
        filename = f"data/{year}_{race_name}_fastf1.csv"
        laps.to_csv(filename, index=False)
        print(f"✔ Saved FastF1 data for {race_name}")
        return filename
    except Exception as e:
        print(f"⚠ Error fetching FastF1 for {race_name}: {e}")
        return None