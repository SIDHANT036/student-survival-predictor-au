import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from src.calculator import calculate_budget_risk
from src.predictor import predict_stress
from src.balance import calculate_burnout_risk
from src.report_gen import generate_report

st.set_page_config(
    page_title="Student Survival Predictor",
    page_icon="🎓",
    layout="wide"
)
st.title("🎓 International Student Survival Predictor")
st.caption("Australia — Melbourne · Sydney · Brisbane")

tab1, tab2, tab3, tab4 = st.tabs([
    "💰 Budget Risk",
    "🧠 Stress Prediction",
    "⚖️ Work-Study Balance",
    "📄 My Report"
])

# ── TAB 1: Budget Risk ───────────────────────────────────
with tab1:
    st.subheader("Budget Risk Calculator")
    col1, col2 = st.columns(2)
    with col1:
        city    = st.selectbox("City", ["Melbourne", "Sydney", "Brisbane"])
        rent    = st.number_input("Weekly rent ($)", 100, 1000, 350)
        income  = st.number_input("Weekly income ($)", 0, 2000, 500)
    with col2:
        transport  = st.number_input("Weekly transport ($)", 0, 200, 40)
        groceries  = st.number_input("Weekly groceries ($)", 0, 300, 80)
        tuition    = st.number_input("Weekly tuition ($)", 0, 500, 150)

    if st.button("Calculate budget risk"):
        r = calculate_budget_risk(city, rent, income,
                                  transport, groceries, tuition)
        st.session_state['budget'] = r
        col_a, col_b, col_c = st.columns(3)
        col_a.metric("Weekly savings", f"${r['savings_weekly']}")
        col_b.metric("Monthly savings", f"${r['savings_monthly']}")
        col_c.metric("Risk level", r['risk_level'])
        if r['suggestions']:
            st.warning("Suggestions")
            for s in r['suggestions']:
                st.write(f"• {s}")

    st.divider()
    st.subheader("Scenario simulator")
    rent_change   = st.slider("Rent change per week ($)", -100, 200, 0, 10)
    hours_change  = st.slider("Extra work hours per week", -10, 10, 0)
    hourly_rate   = st.number_input("Your hourly rate ($)", 15, 50, 24)
    sim = calculate_budget_risk(
        city, rent + rent_change,
        income + hours_change * hourly_rate,
        transport, groceries, tuition
    )
    st.metric("Simulated weekly savings",
              f"${sim['savings_weekly']}",
              delta=round(sim['savings_weekly'] - (income - rent - transport - groceries - tuition), 2))
    st.metric("Simulated risk", sim['risk_level'])

# ── TAB 2: Stress Prediction ─────────────────────────────
with tab2:
    st.subheader("ML Financial Stress Prediction")
    st.caption("Powered by XGBoost trained on 2,000 student records")
    col1, col2 = st.columns(2)
    with col1:
        p_rent    = st.number_input("Rent/wk", 100, 1000, 350, key="p_rent")
        p_income  = st.number_input("Income/wk", 0, 2000, 500, key="p_inc")
        p_trans   = st.number_input("Transport/wk", 0, 200, 40, key="p_tr")
        p_groc    = st.number_input("Groceries/wk", 0, 300, 80, key="p_gr")
    with col2:
        p_tuition = st.number_input("Tuition/wk", 0, 500, 150, key="p_tu")
        p_study   = st.slider("Study hours/wk", 10, 60, 30)
        p_work    = st.slider("Work hours/wk", 0, 48, 20)
        p_commute = st.slider("Daily commute (hrs)", 0.5, 4.0, 1.5)

    if st.button("Predict stress level"):
        result = predict_stress(p_rent, p_income, p_trans, p_groc,
                                p_tuition, p_study, p_work, p_commute)
        st.session_state['stress'] = result
        if result['stressed']:
            st.error(f"⚠️ {result['label']} — {result['probability']}% probability of financial stress")
        else:
            st.success(f"✅ {result['label']} — {result['probability']}% probability of financial stress")

# ── TAB 3: Burnout Balance ───────────────────────────────
with tab3:
    st.subheader("Work-Study Balance Analyser")
    b_study   = st.slider("Study hours per week", 10, 60, 30, key="b_s")
    b_work    = st.slider("Work hours per week",  0, 48, 20, key="b_w")
    b_commute = st.slider("Total commute hours per week", 0.0, 20.0, 7.0, key="b_c")

    if st.button("Analyse balance"):
        b = calculate_burnout_risk(b_study, b_work, b_commute)
        st.session_state['burnout'] = b
        col_a, col_b, col_c = st.columns(3)
        col_a.metric("Total hrs committed", b['total_committed_hours'])
        col_b.metric("Free time/day (hrs)", b['daily_free_time'])
        col_c.metric("Burnout risk", b['burnout_risk'])
        for s in b['suggestions']:
            st.warning(s)

# ── TAB 4: Report ────────────────────────────────────────
with tab4:
    st.subheader("📊 City Comparison Dashboard")

    import plotly.express as px
    import pandas as pd
    import sqlite3

    try:
        conn = sqlite3.connect('data/students.db')
        df = pd.read_sql("SELECT * FROM students", conn)
        conn.close()
    except Exception as e:
        st.error("Database not found. Using fallback CSV.")
        df = pd.read_csv('data/synthetic/students.csv')

    # ---- Filter (PRO FEATURE) ----
    cities = st.multiselect(
        "Select cities",
        df['city'].unique(),
        default=df['city'].unique()
    )
    df = df[df['city'].isin(cities)]

    # ---- Chart 1 ----
    fig1 = px.box(
        df,
        x='city',
        y='savings_weekly',
        color='city',
        title='Weekly savings by city',
        labels={'savings_weekly': 'Savings/week ($)'}
    )
    st.plotly_chart(fig1, use_container_width=True)

    # ---- Chart 2 ----
    fig2 = px.histogram(
        df,
        x='savings_weekly',
        color='financial_stress',
        barmode='overlay',
        nbins=50,
        title='Savings distribution: stressed vs stable'
    )
    st.plotly_chart(fig2, use_container_width=True)