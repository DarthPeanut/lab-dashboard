# In app/database.py

import sqlite3
import json
from . import parser

DATABASE_NAME = "lab_data.db"

def init_db():
    """Initializes the database and creates the table if it doesn't exist."""
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS lab_reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id TEXT NOT NULL,
            report_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            results_json TEXT NOT NULL
        )
        """)
        conn.commit()

def save_lab_report(patient_id: str, results: list):
    """Saves a new lab report for a given patient."""
    results_json = json.dumps(results)
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO lab_reports (patient_id, results_json) VALUES (?, ?)",
            (patient_id, results_json)
        )
        conn.commit()

def get_latest_report(patient_id: str):
    """Gets the most recent previous lab report for a given patient."""
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT results_json FROM lab_reports WHERE patient_id = ? ORDER BY report_date DESC LIMIT 1",
            (patient_id,)
        )
        row = cursor.fetchone()
        if row:
            return json.loads(row[0])
        return None

def process_and_store_report(patient_id: str, file_text: str):
    """
    Orchestrates parsing, fetching previous results, and saving current results.
    """
    previous_results = get_latest_report(patient_id)
    current_results = parser.process_lab_text(file_text)

    if current_results:
        save_lab_report(patient_id, current_results)

    return {
        "current_results": current_results,
        "previous_results": previous_results
    }

# Call this once when the application starts to ensure the DB and table exist
init_db()