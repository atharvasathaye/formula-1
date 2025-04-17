import streamlit as st
import pandas as pd
import os
import altair as alt
import pickle

st.set_page_config(page_title="🏎️ F1 2025 Predictor", layout="wide")

st.title("🏁 F1 2025 Race Data Explorer & Winner Predictor")
st.markdown("Explore telemetry data and view winning probabilities for each driver.")

st.markdown("---")

# Load available race data
data_dir = "data"
csv_files = [f for f in os.listdir(data_dir) if f.endswith(".csv") and "fastf1" in f]

if not csv_files:
    st.warning("No FastF1 race data found. Run `main.py` to fetch race data.")
else:
    selected_file = st.selectbox("📂 Choose a race file:", csv_files)
    df = pd.read_csv(os.path.join(data_dir, selected_file))

    st.markdown("### 🧾 Data Preview")
    st.dataframe(df.head())

    st.markdown("### 📊 Metric Visualization by Driver")

    if 'Driver' in df.columns:
        numeric_cols = df.select_dtypes(include='number').columns.tolist()
        if 'DriverNumber' in numeric_cols:
            numeric_cols.remove('DriverNumber')

        if not numeric_cols:
            st.warning("No numeric columns found.")
        else:
            summary = df.groupby("Driver")[numeric_cols].mean().reset_index()
            metric = st.selectbox("Select a metric to visualize:", numeric_cols)

            chart = alt.Chart(summary).mark_bar().encode(
                x=alt.X("Driver:N", sort="-y"),
                y=alt.Y(f"{metric}:Q", title=metric),
                tooltip=["Driver", metric]
            ).properties(height=400)

            st.altair_chart(chart, use_container_width=True)

    st.markdown("### 🤖 Predicted Winning Probabilities")

    if os.path.exists("model.pkl"):
        with open("model.pkl", "rb") as f:
            model = pickle.load(f)

        X = df.select_dtypes(include='number').drop(columns=['Position'], errors='ignore')
        probs = model.predict_proba(X)[:, 1]

        df['WinProbability'] = probs
        win_avg = df.groupby("Driver")['WinProbability'].mean().reset_index()
        st.dataframe(win_avg.sort_values("WinProbability", ascending=False).reset_index(drop=True))
    else:
        st.warning("⚠ No model found. Train one using `train_model.py`.")