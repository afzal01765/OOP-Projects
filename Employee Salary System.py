

'''

Problem :-

Employee Salary System (Polymorphism)
Create an abstract class Employee with methods to:

Calculate the salary.
Display the details of the employee. Then, create two subclasses:
FullTimeEmployee (salary is calculated based on fixed monthly salary).
PartTimeEmployee (salary is calculated based on hourly rate). Demonstrate polymorphism by calculating salaries for both types of employees.

'''

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_details(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}")


class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

# Part-time Employee class
class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hourly_rate, hours_worked):
        super().__init__(name, emp_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


if __name__ =="__main__":

    full_time_emp = FullTimeEmployee("Alice", 101, 50000)
    part_time_emp = PartTimeEmployee("Bob", 102, 500, 20)

    employees = [full_time_emp, part_time_emp]

    for emp in employees:
        emp.display_details()
        print(f"Salary: {emp.calculate_salary()}\n")
