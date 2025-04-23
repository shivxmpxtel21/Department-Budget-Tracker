
import matplotlib.pyplot as plt
from collections import defaultdict

def plot_budget_vs_spent(department_name, allocated_budget, total_spent):
    labels = ['Allocated Budget', 'Total Spent']
    values = [allocated_budget, total_spent]

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color=['green', 'red'])
    plt.title(f'Budget vs Spent for {department_name}')
    plt.ylabel('Amount')
    plt.tight_layout()
    plt.show()

def plot_expense_categories(expenses, department_name=""):
    category_totals = defaultdict(float)
    for exp in expenses:
        category_totals[exp.category] += exp.amount

    labels = list(category_totals.keys())
    sizes = list(category_totals.values())

    plt.figure(figsize=(7, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(f'Spending by Category for {department_name}' if department_name else 'Spending by Category')
    plt.tight_layout()
    plt.show()

def plot_multiple_departments_by_category(departments):
    from collections import defaultdict
    data = defaultdict(lambda: defaultdict(float))  # {department: {category: amount}}

    for dept in departments:
        for exp in dept.expenses:
            data[dept.name][exp.category] += exp.amount

    for dept_name, categories in data.items():
        labels = list(categories.keys())
        amounts = list(categories.values())

        plt.figure(figsize=(8, 4))
        plt.bar(labels, amounts)
        plt.title(f'{dept_name} Department - Spending by Category')
        plt.ylabel('Amount')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
