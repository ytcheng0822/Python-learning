class Employee:
    nums_of_emps = 0     # count employee numbers
    raise_amount = 1.04  # salary raise 4%

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.nums_of_emps += 1
    
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print(Employee.nums_of_emps)   # 0 employees

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

print(Employee.nums_of_emps)   # 2 employees

# emp_1.raise_amount = 1.05

# print(emp_1.__dict__)  # dictionary

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)