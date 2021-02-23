# Python Object-Oriented Programming

class Employee:
    def __init__(self, first, last, pay):    # definition initialize function
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
    
    def fullname(self):
        return "{} {}".format(self.first, self.last)


emp_1 = Employee("Corey", "Schafer", 50000)  # instance object1
emp_2 = Employee("Test", "User", 60000)      # instance object2

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(Employee.fullname(emp_1))