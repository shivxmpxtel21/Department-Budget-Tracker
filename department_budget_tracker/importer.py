
import csv
from department_budget_tracker.database import initialize_database, session, Department
from department_budget_tracker.department import DepartmentManager

def import_transactions_from_csv(filepath, default_budget=10000):
    initialize_database()

    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                department_name = row['department']
                amount = float(row['amount'])
                category = row['category']
                description = row['description']
                date = row['date']

                dept_manager = DepartmentManager(department_name, default_budget)
                dept_manager.add_expense(amount, category, description, date)
            except KeyError as e:
                print(f"Missing column in CSV: {e}")
            except Exception as e:
                print(f"Error processing row {row}: {e}")
