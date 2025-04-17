# 🏎️ F1 2025 Race Winner Predictor

This project uses real-time and historical data from the 2025 Formula 1 season to build a machine learning pipeline that predicts race winners. It leverages the FastF1 and Ergast APIs to extract, clean, and merge detailed driver and telemetry data.

---

## 🚀 Features

- ✅ Automated data pipeline for 2025 race data (FastF1)
- ✅ Modular Python scripts to extract, clean, and preprocess data
- ✅ Ready for integration with machine learning models
- ✅ GitHub-ready project layout for sharing and collaboration

---

## 📁 Folder Structure

```
f1-2025-predictor/
├── data/               # Processed race data
├── cache/              # FastF1 cache (ignored in Git)
├── src/
│   ├── fetch_fastf1.py
│   ├── fetch_ergast.py
│   └── combine_features.py
├── main.py             # Master script for running the pipeline
├── requirements.txt
└── README.md
```

---

## 📦 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/f1-2025-predictor.git
   cd f1-2025-predictor
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the data pipeline:
   ```bash
   python main.py
   ```

---

## 📊 Next Steps

- Add feature engineering logic and model training
- Integrate Streamlit for live visualization
- Deploy model predictions and leaderboards

---

## 🤝 Contributing

Feel free to fork the repo and open a pull request with improvements or fixes!

---

## 📜 License

This project is licensed under the MIT License.
