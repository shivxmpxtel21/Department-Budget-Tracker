
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
engine = create_engine('sqlite:///budget_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String)
    date = Column(Date, nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'))

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    allocated_budget = Column(Float, nullable=False)
    expenses = relationship('Expense', backref='department', cascade='all, delete-orphan')

def initialize_database():
    Base.metadata.create_all(engine)
