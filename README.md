# Formula 1 Race Winner Predictor

Machine learning pipeline that ingests real-time and historical Formula 1 data to predict race outcomes. The pipeline integrates the FastF1 and Ergast APIs to extract, clean, and merge driver telemetry and session data.

---

## Features

- Data pipeline for Formula 1 race data ingestion via FastF1
- Modular Python scripts for data extraction, preprocessing, and feature combination
- Pipeline automation via central entry point
- Streamlit web interface for model inference and results display

---

## Repository Structure

```
formula-1/
├── data/               # Processed race data
├── cache/              # FastF1 cache (git ignored)
├── src/
│   ├── fetch_fastf1.py
│   ├── fetch_ergast.py
│   └── combine_features.py
├── main.py             # Pipeline execution script
├── app.py              # Streamlit dashboard application
├── train_model.py      # Model training script
├── model.pkl           # Serialized model artifact
├── requirements.txt
└── README.md
```

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/atharvasathaye/formula-1.git
   cd formula-1
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

## License

This project is licensed under the MIT License.

## Author

Atharva Sathaye
