import pandas as pd
import os

def merge_datasets(fastf1_file, ergast_file):
    df_fastf1 = pd.read_csv(fastf1_file)
    df_ergast = pd.read_csv(ergast_file)

    last_laps = df_fastf1.groupby('Driver')['LapNumber'].max().reset_index()
    df_fastf1 = df_fastf1.merge(last_laps, on=['Driver', 'LapNumber'])

    features = df_fastf1.groupby('Driver').agg({
        'LapTime': 'mean',
        'SpeedST': 'mean',
        'PitOutTime': 'count'
    }).rename(columns={'LapTime': 'AvgLapTime', 'SpeedST': 'AvgSpeed', 'PitOutTime': 'PitStops'}).reset_index()

    df = features.merge(df_ergast, on='Driver', how='inner')
    df['Winner'] = (df['Position'] == 1).astype(int)

    output_file = f"data/merged_{os.path.basename(fastf1_file)}"
    df.to_csv(output_file, index=False)
    print(f"✅ Merged dataset saved as {output_file}")
    return df