# Student Survival Predictor — Project Writeup

## Problem Statement
International students in Australia face financial pressure due to high living costs, tuition fees, and limited work hours. This project aims to predict financial stress and provide actionable insights using data-driven models.

## Dataset Description
The dataset consists of synthetic student records including:
- City (Melbourne, Sydney, Brisbane)
- Weekly rent, income, groceries, transport, tuition
- Study hours, work hours, commute time
- Derived features like weekly savings and financial stress labels

Total records: ~2000 students

## Methodology
### 1. Exploratory Data Analysis (EDA)
- Analysed cost distributions across cities
- Identified correlation between rent, income, and stress
- Visualised savings patterns

### 2. Feature Engineering
- Created savings_weekly = income - expenses
- Derived financial_stress (binary classification)
- Normalised numerical features

### 3. Model Selection
- Tested multiple models:
  - Logistic Regression
  - Random Forest
  - XGBoost (final choice)

### 4. Evaluation
- Train-test split (80/20)
- Metrics used:
  - Accuracy
  - Precision
  - Recall
  - F1-score

## Key Findings
- XGBoost achieved F1-score ≈ 0.91
- Rent and income are the strongest predictors
- Students with negative weekly savings are highly likely to be stressed
- Sydney shows highest financial pressure among cities

## Limitations & Next Steps
### Limitations
- Synthetic dataset (not real-world data)
- Limited feature diversity (no visa/work restrictions included)
- Static model (no real-time updates)

### Next Steps
- Use real-world datasets
- Add more behavioural and demographic features
- Deploy model with real-time API
- Improve explainability using SHAP

## How to Run
1. Clone the repository:
   git clone <your-repo-url>

2. Navigate to project:
   cd student-survival-predictor-au

3. Create virtual environment:
   python3.11 -m venv venv
   source venv/bin/activate

4. Install dependencies:
   pip install -r requirements.txt

5. Run Streamlit app:
   streamlit run app.py

6. Open in browser:
   http://localhost:8501
