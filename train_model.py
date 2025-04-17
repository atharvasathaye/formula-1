import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_model(data_path, save_path="model.pkl"):
    df = pd.read_csv(data_path)

    # Ensure required columns are present
    if 'Position' not in df.columns or 'Driver' not in df.columns:
        print("Missing required columns in data.")
        return

    df['Winner'] = (df['Position'] == 1).astype(int)
    X = df.select_dtypes(include='number').drop(columns=['Position', 'Winner'], errors='ignore')
    y = df['Winner']

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    with open(save_path, "wb") as f:
        pickle.dump(model, f)
    print(f"✅ Model trained and saved to {save_path}")

if __name__ == "__main__":
    train_model("data/2025_Australia_fastf1.csv")
