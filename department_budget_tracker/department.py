
from .database import Department, session
from .expense import create_expense
from .visualization import plot_budget_vs_spent, plot_expense_categories
from .reporting import export_report_csv, export_report_pdf

class DepartmentManager:
    def __init__(self, name, allocated_budget):
        existing = session.query(Department).filter_by(name=name).first()
        if existing:
            self.department = existing
        else:
            self.department = Department(name=name, allocated_budget=allocated_budget)
            session.add(self.department)
            session.commit()

    def add_expense(self, amount, category, description, date_str):
        expense = create_expense(amount, category, description, date_str)
        expense.department = self.department
        session.add(expense)
        session.commit()

    def get_total_spent(self):
        return sum(exp.amount for exp in self.department.expenses)

    def get_remaining_budget(self):
        return self.department.allocated_budget - self.get_total_spent()

    def list_expenses(self):
        return [(exp.amount, exp.category, exp.description, exp.date) for exp in self.department.expenses]

    def visualize_budget(self):
        plot_budget_vs_spent(self.department.name, self.department.allocated_budget, self.get_total_spent())

    def visualize_categories(self):
        plot_expense_categories(self.department.expenses, department_name=self.department.name)

    def export_report(self, format='csv', filename=None):
        if not filename:
            filename = f"{self.department.name}_report.{format}"
        if format == 'csv':
            export_report_csv(self.department, self.department.expenses, filename)
        elif format == 'pdf':
            export_report_pdf(self.department, self.department.expenses, filename)
        else:
            raise ValueError("Format must be 'csv' or 'pdf'")
