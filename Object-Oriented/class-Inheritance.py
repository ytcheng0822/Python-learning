class Employee:
    raise_amount = 1.04   # salary raise 4%

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
    
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):  # this is Subclasses
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)    #  = Employee.__init__(self, first, last, pay) 
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())
    

emp_1 = Developer("Corey", "Schafer", 50000, "Python")

emp_2 = Developer("Test", "User", 60000, "C")

mgr_1 = Manager("Sue", "Smith", 90000, [emp_1])

# print(mgr_1.email)

# mgr_1.add_emp(emp_2)

# mgr_1.print_emps()

print(issubclass(Manager, Employee))   # Manger is subclass in Employee

# print(emp_1.email)
# print(emp_1.prog_lang)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)