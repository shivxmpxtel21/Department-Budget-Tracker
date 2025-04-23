# Department Budget Tracker

# Overview
The Department Budget Tracker is a Python package that helps organizations manage and monitor departmental budgets. It supports creating departments, recording categorized expenses, importing transactions from CSV files, visualizing spending data, and exporting reports in CSV or PDF format.

This package uses a persistent SQLite database via SQLAlchemy to store departments and their expenses, ensuring data is retained across sessions. It is ideal for finance teams seeking transparency, automation, and analytics without the overhead of a large-scale ERP system.


# Package Structure


department_budget_tracker/
├── __init__.py
├── database.py          - SQLAlchemy models and session setup
├── department.py        - DepartmentManager class (core interface)
├── expense.py           - Expense factory method
├── importer.py          - CSV import tool for bulk transactions
├── reporting.py         - CSV and PDF export logic
├── visualization.py     - Graphs for budget and category analysis
├── admin_tools.py       - Department update/delete/rename
tests/
├── test_department.py
├── test_expense.py


# Setup

# Requirements
Install requirements with:

```bash
pip install -r requirements.txt
```


# Usage

The Department Budget Tracker is used to track budgets and expenses for multiple departments. Users start by initializing the database and creating departments with allocated budgets. Expenses can be added individually or imported in bulk via a CSV file.

Each department tracks categorized spending such as Travel, Software, Supplies, etc. Expenses are stored in a persistent SQLite database, making it possible to analyze trends, visualize budget usage, and export reports.

Typical workflow:
1. Initialize the database
2. Create departments
3. Add expenses manually or import from CSV
4. Visualize spending per department or across all departments
5. Export reports in PDF or CSV format
6. Use admin tools to manage departments

Example:

```python
from department_budget_tracker.database import initialize_database
from department_budget_tracker.department import DepartmentManager
from department_budget_tracker.importer import import_transactions_from_csv

initialize_database()

# Add a department and an expense
dept = DepartmentManager("Finance", 10000)
dept.add_expense(500, "Travel", "Conference trip", "2025-03-21")

# Import multiple transactions
import_transactions_from_csv("transactions.csv", default_budget=8000)

# Visualize and export
dept.visualize_budget()
dept.visualize_categories()
dept.export_report(format="pdf")
```

# Importing Transactions from CSV

CSV Format:

| date       | amount | category       | description         | department |
|------------|--------|----------------|----------------------|------------|
| 2025-04-20 | 500.00 | Travel         | Conference Flight     | Finance    |

Use the importer like this:

```python
from department_budget_tracker.importer import import_transactions_from_csv
import_transactions_from_csv("transactions.csv", default_budget=8000)
```

---

# Admin Tools

Update or remove departments:

```python
from department_budget_tracker import admin_tools

admin_tools.rename_department("HR", "People Ops")
admin_tools.update_department_budget("IT", 12000)
admin_tools.delete_department("Finance")
```

---

# Testing

Run all unit tests:

```bash
python -m unittest discover tests
```

---

# Notes

- All data is stored persistently using SQLite in `budget_tracker.db`.
- Visualizations use `matplotlib`.
- Reports are exported using the `fpdf` library.

