from menu import Menu

class Restaurant:
    def __init__(self,name):
        self.name= name
        self.employee = []
        self.menu = Menu()

    def add_employee(self, employee):
        self.employee.append(employee)
        print("Employee Added !!!")

    def view_employee(self):
        for emp in self.employee:
            print(emp.name, emp.email, emp.phone, emp.address )

