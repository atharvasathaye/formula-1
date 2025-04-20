import streamlit as st
import pandas as pd
import os
import altair as alt
import pickle
from sklearn.ensemble import RandomForestClassifier

# App setup
st.set_page_config(page_title="🏎️ F1 2025 Predictor", layout="wide")
st.title("🏁 F1 2025 Race Data Explorer & Winner Predictor")
st.markdown("Explore telemetry data and view winning probabilities for each driver.")
st.markdown("---")

# Load race data
data_dir = "data"
csv_files = [f for f in os.listdir(data_dir) if f.endswith(".csv") and "fastf1" in f]

if not csv_files:
    st.warning("No FastF1 race data found. Run `main.py` to fetch race data.")
else:
    selected_file = st.selectbox("📂 Choose a race file:", csv_files)
    file_path = os.path.join(data_dir, selected_file)
    df = pd.read_csv(file_path)

    st.markdown("### 🧾 Data Preview")
    st.dataframe(df.head())

    st.markdown("### 📊 Metric Visualization by Driver")

    if 'Driver' in df.columns:
        numeric_cols = df.select_dtypes(include='number').columns.tolist()
        if 'DriverNumber' in numeric_cols:
            numeric_cols.remove('DriverNumber')

        if numeric_cols:
            summary = df.groupby("Driver")[numeric_cols].mean().reset_index()
            metric = st.selectbox("Select a metric to visualize:", numeric_cols)

            chart = alt.Chart(summary).mark_bar().encode(
                x=alt.X("Driver:N", sort="-y"),
                y=alt.Y(f"{metric}:Q", title=metric),
                tooltip=["Driver", metric]
            ).properties(height=400)

            st.altair_chart(chart, use_container_width=True)

    st.markdown("### 🤖 Predicted Winning Probabilities")

    # Auto-train model if needed
    model_path = "model.pkl"
    model = None

    if "Position" in df.columns and "Driver" in df.columns:
        df['Winner'] = (df['Position'] == 1).astype(int)
        X = df.select_dtypes(include='number').drop(columns=['Position', 'Winner'], errors='ignore')
        y = df['Winner']

        try:
            if os.path.exists(model_path):
                with open(model_path, "rb") as f:
                    model = pickle.load(f)
            else:
                model = RandomForestClassifier(n_estimators=100, random_state=42)
                model.fit(X, y)
                with open(model_path, "wb") as f:
                    pickle.dump(model, f)
                st.success("✅ Model trained and saved successfully.")
        except Exception as e:
            st.error(f"❌ Failed to train or load model: {e}")
            st.stop()
    else:
        st.error("❌ Required columns ('Position', 'Driver') not found in dataset.")
        st.stop()

    # Predict win probabilities
    if model is not None:
        try:
            probs = model.predict_proba(X)[:, 1]
            df['WinProbability'] = probs
            win_avg = df.groupby("Driver")['WinProbability'].mean().reset_index()
            st.dataframe(win_avg.sort_values("WinProbability", ascending=False).reset_index(drop=True))
        except Exception as e:
            st.error(f"❌ Prediction failed: {e}")
