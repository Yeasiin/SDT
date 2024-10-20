from users import customer_menu, admin_menu
from restaurant import Restaurant

while True:
    restaurant = Restaurant("Daba")
    print("Welcome!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice  = int(input("Enter your choice: "))

    if choice ==1:
        customer_menu(restaurant)
    elif choice==2:
        admin_menu(restaurant)
    elif choice==3:
        break
    else:
        print("Invalid Choice")

    
