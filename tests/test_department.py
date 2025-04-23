
import unittest
from department_budget_tracker.database import initialize_database, session, Department
from department_budget_tracker.department import DepartmentManager

class TestDepartmentManager(unittest.TestCase):

    def setUp(self):
        initialize_database()
        session.query(Department).delete()
        session.commit()

    def test_create_department_and_budget(self):
        dept = DepartmentManager("HR", 3000)
        self.assertEqual(dept.department.name, "HR")
        self.assertEqual(dept.department.allocated_budget, 3000)

    def test_add_expense_and_check_total(self):
        dept = DepartmentManager("Finance", 5000)
        dept.add_expense(200, "Training", "Workshop", "2025-04-20")
        self.assertEqual(dept.get_total_spent(), 200)
        self.assertEqual(dept.get_remaining_budget(), 4800)

    def test_list_expenses(self):
        dept = DepartmentManager("IT", 6000)
        dept.add_expense(100, "Hardware", "Mouse", "2025-04-21")
        dept.add_expense(150, "Software", "License", "2025-04-22")
        expenses = dept.list_expenses()
        self.assertEqual(len(expenses), 2)

if __name__ == '__main__':
    unittest.main()
