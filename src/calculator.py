def calculate_budget_risk(city, rent, income, transport,
                          groceries, tuition):
    total_expenses = rent + transport + groceries + tuition
    savings_weekly = income - total_expenses
    savings_monthly = savings_weekly * 4.33

    city_benchmarks = {
        'Melbourne': {'avg_rent': 380, 'min_wage_weekly': 660},
        'Sydney':    {'avg_rent': 450, 'min_wage_weekly': 660},
        'Brisbane':  {'avg_rent': 320, 'min_wage_weekly': 660},
    }
    bench = city_benchmarks.get(city, city_benchmarks['Melbourne'])
    rent_ratio = rent / income if income > 0 else 1
    expense_ratio = total_expenses / income if income > 0 else 1

    if expense_ratio > 0.85 or savings_weekly < 0:
        risk = 'High'
        color = 'red'
    elif expense_ratio > 0.65 or savings_weekly < 50:
        risk = 'Medium'
        color = 'orange'
    else:
        risk = 'Low'
        color = 'green'

    suggestions = []
    if rent > bench['avg_rent']:
        suggestions.append(
            f"Your rent is ${rent - bench['avg_rent']:.0f}/wk above "
            f"{city} average. Consider a share house."
        )
    if rent_ratio > 0.4:
        suggestions.append(
            "Rent is over 40% of income — the recommended max is 30%."
        )
    if savings_weekly < 50:
        suggestions.append(
            "Savings are critically low. Review grocery and transport spend."
        )

    return {
        'total_expenses_weekly': round(total_expenses, 2),
        'savings_weekly': round(savings_weekly, 2),
        'savings_monthly': round(savings_monthly, 2),
        'risk_level': risk,
        'risk_color': color,
        'suggestions': suggestions,
        'expense_ratio': round(expense_ratio * 100, 1),
    }