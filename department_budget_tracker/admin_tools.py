
from department_budget_tracker.database import session, Department

def delete_department(name):
    dept = session.query(Department).filter_by(name=name).first()
    if dept:
        session.delete(dept)
        session.commit()
        print(f"Department '{name}' deleted successfully.")
    else:
        print(f"Department '{name}' not found.")

def rename_department(old_name, new_name):
    dept = session.query(Department).filter_by(name=old_name).first()
    if dept:
        dept.name = new_name
        session.commit()
        print(f"Department '{old_name}' renamed to '{new_name}'.")
    else:
        print(f"Department '{old_name}' not found.")

def update_department_budget(name, new_budget):
    dept = session.query(Department).filter_by(name=name).first()
    if dept:
        dept.allocated_budget = new_budget
        session.commit()
        print(f"Budget for department '{name}' updated to {new_budget}.")
    else:
        print(f"Department '{name}' not found.")
