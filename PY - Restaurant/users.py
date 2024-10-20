from abc import ABC
from restaurant import Restaurant
from orders import Order
from foodItem import FoodItem

class User(ABC):
    def __init__(self,name,email,phone,address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address


class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart = Order()

    def view_menu(self,restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self,restaurant,item_name,quantity):
        item = restaurant.menu.find_item(item_name)

        if item:
            if(quantity > item.quantity):
                print("Item Quantity Exceeded!!")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("item added")
        else:
            print("item not found")

    def view_cart(self):
        print("****View Cart****")
        print("Name\tPrice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")

        print(f"Total Price: {self.cart.total_price}")

    def pay_bill(self):
        print(f"Total {self.cart.total_price} paid successfully")
        self.cart.clear()



class Employee(User):
    def __init__(self, name, email, phone, address,age,designation,salary):
        super().__init__(name, email, phone, address)
        self.age = age
        self.designation = designation
        self.salary = salary


class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)


    def add_employee(self,restaurant,employee):
        restaurant.add_employee(employee)

    def view_employee(self,restaurant):
        restaurant.view_employee()

    def view_item(self,restaurant):
        restaurant.menu.show_menu()

    def add_new_item(self,restaurant,item):
        restaurant.menu.add_menu_item(item)

    def delete_item(self,restaurant,item_name):
        restaurant.menu.remove_item(item_name)




def customer_menu(restaurant):
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Input your phone: ")
    address = input("Input your address: ")

    customer = Customer(name,email,phone,address)

    while True:
        print(f"Welcome {name}!!")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View Cart")
        print("4. PayBill")
        print("5. Exit")


        choice = int(input("Enter your choice: "))
        
        if(choice ==1):
            customer.view_menu(restaurant)
        elif(choice==2):
            item_name = input("Enter Item Name: ")
            item_quantity = int(input("Enter Item Quantity: "))
            customer.add_to_cart(restaurant,item_name, item_quantity)
        elif choice ==3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()

        elif choice ==5:
            break
        else:
            print("Invalid Input")


def admin_menu(restaurant):
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Input your phone: ")
    address = input("Input your address: ")

    admin = Admin(name,email,phone,address)

    while True:
        print(f"Welcome {name}!!")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Delete Item")
        print("6. Exit")


        choice = int(input("Enter your choice: "))
        
        if(choice ==1):
            f_name =input("Enter Item Name: ")
            f_price = input("Enter Item Price: ")
            f_quantity = input("Enter Item Quantity: ")
            item = FoodItem(f_name,f_price,f_quantity)
            admin.add_new_item(restaurant,item)
        elif(choice==2):
            e_name= input("Enter Employee Name: ")
            e_email= input("Enter Employee Email: ")
            e_phone= input("Enter Employee Phone: ")
            e_address= input("Enter Employee Address: ")
            e_age= input("Enter Employee Age: ")
            e_designation= input("Enter Employee Designation: ")
            e_salary= input("Enter Employee Salary: ")

            employee = Employee(e_name,e_email,e_phone,e_address,e_age,e_designation,
            e_salary)
            admin.add_employee(restaurant, employee)
        elif choice ==3:
            admin.view_employee(restaurant)
        elif choice == 4:
            admin.view_item(restaurant)
        elif choice ==5:
            item_name = input("Enter Item Name: ")
            admin.delete_item(restaurant,item_name)
            
        elif choice ==6:
            break
        else:
            print("Invalid Input")


 