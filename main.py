from src.fetch_fastf1 import fetch_fastf1_race
# from src.fetch_ergast import fetch_ergast_results  # Not used
# from src.combine_features import merge_datasets    # Not used

races_2025 = [
    {'name': 'Australia', 'round': 1},
    {'name': 'China', 'round': 2},
    {'name': 'Japan', 'round': 3},
    {'name': 'Bahrain', 'round': 4},
]

for race in races_2025:
    fastf1_file = fetch_fastf1_race(2025, race['name'])

    if fastf1_file:
        print(f"✔ Fetched FastF1 data for {race['name']} and saved as {fastf1_file}")
        # You can process or analyze this data here manually or via notebook
    else:
        print(f"❌ Failed to fetch FastF1 data for {race['name']}")
