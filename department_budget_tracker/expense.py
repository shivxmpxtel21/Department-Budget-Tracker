
from datetime import datetime
from .database import Expense

def create_expense(amount, category, description, date_str):
    date = datetime.strptime(date_str, "%Y-%m-%d").date()
    return Expense(amount=amount, category=category, description=description, date=date)
