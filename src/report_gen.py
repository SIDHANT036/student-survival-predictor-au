from fpdf import FPDF
import datetime, os

def generate_report(student_name, budget_results,
                    stress_results, burnout_results):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(24, 95, 165)
    pdf.cell(0, 12, "Student Survival Report", ln=True)

    pdf.set_font("Helvetica", size=10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 6, f"Student: {student_name}", ln=True)
    pdf.cell(0, 6, f"Generated: {datetime.date.today()}", ln=True)
    pdf.ln(6)

    def section(title):
        pdf.set_font("Helvetica", "B", 13)
        pdf.set_text_color(30, 30, 30)
        pdf.cell(0, 10, title, ln=True)
        pdf.set_font("Helvetica", size=11)
        pdf.set_text_color(60, 60, 60)

    section("Financial Summary")
    pdf.cell(0, 7, f"Weekly savings: ${budget_results['savings_weekly']}", ln=True)
    pdf.cell(0, 7, f"Monthly savings: ${budget_results['savings_monthly']}", ln=True)
    pdf.cell(0, 7, f"Budget risk: {budget_results['risk_level']}", ln=True)
    pdf.ln(4)

    section("Financial Stress Prediction")
    pdf.cell(0, 7, f"Status: {stress_results['label']}", ln=True)
    pdf.cell(0, 7, f"Probability: {stress_results['probability']}%", ln=True)
    pdf.ln(4)

    section("Work-Study Balance")
    pdf.cell(0, 7, f"Total committed hours/week: {burnout_results['total_committed_hours']}", ln=True)
    pdf.cell(0, 7, f"Burnout risk: {burnout_results['burnout_risk']}", ln=True)
    pdf.ln(4)

    section("Recommendations")
    all_tips = (budget_results.get('suggestions', []) +
                burnout_results.get('suggestions', []))
    if all_tips:
        for tip in all_tips:
            pdf.multi_cell(0, 7, f"- {tip}")
    else:
        pdf.cell(0, 7, "No major issues detected. Keep it up!", ln=True)

    os.makedirs('reports', exist_ok=True)
    path = f"reports/report_{student_name.replace(' ','_')}_{datetime.date.today()}.pdf"
    pdf.output(path)
    return path