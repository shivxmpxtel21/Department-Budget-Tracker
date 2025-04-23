
from setuptools import setup, find_packages

setup(
    name='department_budget_tracker',
    version='0.1',
    packages=find_packages(),
    install_requires=['pandas', 'matplotlib', 'seaborn', 'sqlalchemy', 'fpdf'],
    author='Shivam Patel',
    description='A package to manage and monitor departmental budgets',
)
