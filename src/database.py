import sqlite3, pandas as pd, os

DB_PATH = 'data/students.db'

def init_db():
    df = pd.read_csv('data/synthetic/students.csv')
    conn = sqlite3.connect(DB_PATH)
    df.to_sql('students', conn, if_exists='replace', index=False)
    conn.close()
    print(f"DB created at {DB_PATH}")

def query_stress_by_city():
    conn = sqlite3.connect(DB_PATH)
    result = pd.read_sql("""
        SELECT city,
               COUNT(*) as total_students,
               SUM(financial_stress) as stressed,
               ROUND(AVG(financial_stress)*100, 1) as stress_pct,
               ROUND(AVG(savings_weekly), 2) as avg_savings
        FROM students
        GROUP BY city
        ORDER BY stress_pct DESC
    """, conn)
    conn.close()
    return result
