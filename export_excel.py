import pandas as pd
import sqlite3

def export_excel():

    conn = sqlite3.connect("attendance_records/attendance.db")

    df = pd.read_sql_query("SELECT * FROM attendance", conn)

    df.to_excel("attendance_records/attendance_report.xlsx", index=False)

    conn.close()

    return "Excel report generated"