def calculate_burnout_risk(study_hours, work_hours, commute_hours):
    total_hours = study_hours + work_hours + commute_hours
    sleep_available = 168 - total_hours
    daily_free_time = (168 - total_hours - (sleep_available * 0.9)) / 7

    if total_hours > 65 or daily_free_time < 1:
        risk = 'High'
    elif total_hours > 55 or daily_free_time < 2:
        risk = 'Medium'
    else:
        risk = 'Low'

    suggestions = []
    if work_hours > 20:
        suggestions.append(
            f"You work {work_hours}h/wk. Australian student visa "
            "limits are 48h per fortnight — check you are compliant."
        )
    if study_hours > 40:
        suggestions.append(
            "Study load is very high. Talk to your university "
            "about reducing units if possible."
        )
    if commute_hours > 10:
        suggestions.append(
            "Long commute detected. Moving closer to uni or work "
            f"could save ~{commute_hours - 5:.0f}h/week."
        )
    if daily_free_time < 1.5:
        suggestions.append(
            "Almost no free time. Schedule at least 2h daily for "
            "rest — burnout affects academic performance."
        )

    return {
        'total_committed_hours': round(total_hours, 1),
        'daily_free_time': round(daily_free_time, 1),
        'estimated_sleep_hours': round(sleep_available / 7, 1),
        'burnout_risk': risk,
        'suggestions': suggestions,
    }