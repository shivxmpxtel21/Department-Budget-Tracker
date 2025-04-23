'''
Testing Admin Tools
'''

import unittest
from department_budget_tracker.database import session, Department, initialize_database
from department_budget_tracker.department import DepartmentManager
from department_budget_tracker import admin_tools

class TestAdminTools(unittest.TestCase):

    def setUp(self):
        initialize_database()
        session.query(Department).delete()
        session.commit()
        self.manager = DepartmentManager("TestDept", 5000)

    def test_rename_department(self):
        admin_tools.rename_department("TestDept", "NewDept")
        dept = session.query(Department).filter_by(name="NewDept").first()
        self.assertIsNotNone(dept)

    def test_update_budget(self):
        admin_tools.update_department_budget("TestDept", 9000)
        dept = session.query(Department).filter_by(name="TestDept").first()
        self.assertEqual(dept.allocated_budget, 9000)

    def test_delete_department(self):
        admin_tools.delete_department("TestDept")
        dept = session.query(Department).filter_by(name="TestDept").first()
        self.assertIsNone(dept)

if __name__ == '__main__':
    unittest.main()

