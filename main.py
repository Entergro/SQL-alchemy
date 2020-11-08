from db import DBSession
from db.queries import employee, department
from db.models import Employee, Department
from sqlalchemy import func

DB = DBSession()


def create_data():
    department.push_new_depart(DB, d_title="Top")
    department.push_new_depart(DB, d_title="IT", d_parent="Top")
    department.push_new_depart(DB, d_title="Marketing", d_parent="Top")

    employee.push_new_employee(DB, e_name="Vlad", e_depart="Top")
    employee.push_new_employee(DB, e_name="Nastya", e_depart="Top")

    employee.push_new_employee(DB, e_name="Nikita", e_depart="IT")
    employee.push_new_employee(DB, e_name="Lidaaaaaaasdsaa", e_depart="IT")
    employee.push_new_employee(DB, e_name="Alex", e_depart="IT")
    employee.push_new_employee(DB, e_name="David", e_depart="IT")

    employee.push_new_employee(DB, e_name="Kate", e_depart="Marketing")
    employee.push_new_employee(DB, e_name="Justin", e_depart="Marketing")
    employee.push_new_employee(DB, e_name="L", e_depart="Marketing")
    employee.push_new_employee(DB, e_name="Ann", e_depart="Marketing")
    employee.push_new_employee(DB, e_name="Alex-J", e_depart="Marketing")

def task1():
    print("Task1()")
    d_name = input("Enter the Department name: ")
    d_id = department.get_depart_id_by_name(DB, d_name)
    data = DB.session.query(Employee.name).filter(Employee.dep_id == d_id).all()
    for empl in data:
        print(empl[0])
    print("Task1() completed\n")


def task2():
    print("Task2()")
    d_id = DB.session.query(Employee.dep_id, func.max(func.length(Employee.name))).first()[0]
    d_title = DB.session.query(Department.title).filter(Department.id == d_id).one()[0]
    print(d_title)
    print("Task2() completed\n")


create_data()
task1()
task2()
