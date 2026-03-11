from datetime import datetime
from database import mark_attendance

def register_attendance(name):

    now = datetime.now()

    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    mark_attendance(name,date,time)