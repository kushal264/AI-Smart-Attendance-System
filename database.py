import sqlite3

def create_db():
    conn = sqlite3.connect("attendance_records/attendance.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        date TEXT,
        time TEXT
    )
    """)

    conn.commit()
    conn.close()


def mark_attendance(name,date,time):

    conn = sqlite3.connect("attendance_records/attendance.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO attendance(name,date,time) VALUES(?,?,?)",
        (name,date,time)
    )

    conn.commit()
    conn.close()