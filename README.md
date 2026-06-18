# 🎓 International Student Survival Predictor (Australia)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://YOUR-APP.streamlit.app)
[![Tests](https://github.com/SIDHANT036/student-survival-predictor-au/actions/workflows/test.yml/badge.svg)](https://github.com/SIDHANT036/student-survival-predictor-au/actions)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://python.org)

> An end-to-end machine learning platform that predicts financial stress
> and work-study burnout risk for international students across
> Melbourne, Sydney, and Brisbane.


## Problem
International students in Australia face rent increases, 48h/fortnight
work limits, and rising cost of living. This tool helps them predict and
manage financial risk before it becomes a crisis.

## Features
| Feature | Description |
|---|---|
| Budget risk calculator | Risk score + suggested adjustments |
| Scenario simulator | "What if rent goes up $50/week?" |
| ML stress predictor | XGBoost, F1=0.91 on test set |
| Burnout analyser | Visa-compliant work-hour checks |
| PDF report export | Personalised downloadable report |

## Tech stack
Python · Pandas · Scikit-learn · XGBoost · Streamlit · Plotly · SQLite · fpdf2 · Docker

## Model performance
| Model | Accuracy | F1 Score | ROC AUC |
|---|---|---|---|
| Logistic Regression | 84.2% | 0.83 | 0.84 |
| Random Forest | 90.1% | 0.90 | 0.91 |
| **XGBoost** | **91.4%** | **0.91** | **0.93** |

## How to run locally
```bash
git clone https://github.com/SIDHANT036/student-survival-predictor-au
cd student-survival-predictor-au
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Project structure
```
├── notebooks/      # EDA, model training, evaluation
├── src/            # Calculator, predictor, balance, PDF logic
├── data/synthetic/ # Generated student dataset (2,000 rows)
├── models/         # Saved XGBoost model (.pkl)
├── tests/          # Unit tests (pytest)
├── docs/           # Full project write-up
└── app.py          # Streamlit app entry point
```

## Dataset
Synthetic dataset of 2,000 student records generated using Australian
Bureau of Statistics cost-of-living benchmarks for Melbourne, Sydney,
and Brisbane (2024–25).

## Author
Sidhant Narang 