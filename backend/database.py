import sqlite3
from datetime import datetime

DATABASE_FILE = "../resume_screening.db"

def init_db():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resume_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            resume_name TEXT NOT NULL,
            role TEXT NOT NULL,
            score INTEGER NOT NULL,
            reasoning TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_evaluation(resume_name, role, score, reasoning):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    created_at = datetime.now().isoformat()
    cursor.execute('''
        INSERT INTO resume_results (resume_name, role, score, reasoning, created_at)
        VALUES (?, ?, ?, ?, ?)
    ''', (resume_name, role, score, reasoning, created_at))
    conn.commit()
    conn.close()

def get_all_results():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT resume_name, role, score, reasoning FROM resume_results ORDER BY created_at DESC')
    results = cursor.fetchall()
    conn.close()
    return [{"resume_name": r[0], "role": r[1], "score": r[2], "reasoning": r[3]} for r in results]