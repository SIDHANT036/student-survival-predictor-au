import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.calculator import calculate_budget_risk

def test_high_risk():
    r = calculate_budget_risk('Melbourne', 600, 300, 60, 150, 350)
    assert r['risk_level'] == 'High'

def test_low_risk():
    r = calculate_budget_risk('Brisbane', 250, 800, 30, 60, 100)
    assert r['risk_level'] == 'Low'

def test_savings_calculation():
    r = calculate_budget_risk('Sydney', 300, 600, 40, 80, 100)
    assert r['savings_weekly'] == 80.0

def test_monthly_savings():
    r = calculate_budget_risk('Melbourne', 300, 600, 40, 80, 100)
    assert r['savings_monthly'] == round(80 * 4.33, 2)

def test_suggestions_for_high_rent():
    r = calculate_budget_risk('Melbourne', 550, 600, 40, 80, 100)
    assert len(r['suggestions']) > 0