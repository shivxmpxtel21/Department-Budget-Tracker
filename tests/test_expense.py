
import unittest
from department_budget_tracker.expense import create_expense

class TestExpenseCreation(unittest.TestCase):

    def test_create_expense(self):
        expense = create_expense(99.99, "Office Supplies", "Pens and paper", "2025-04-20")
        self.assertEqual(expense.amount, 99.99)
        self.assertEqual(expense.category, "Office Supplies")
        self.assertEqual(expense.description, "Pens and paper")
        self.assertEqual(str(expense.date), "2025-04-20")

if __name__ == '__main__':
    unittest.main()
