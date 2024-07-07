from datetime import datetime

def is_today(date):
    return date.date() == datetime.today().date()