from random import random

class Product:
    def __init__(self,id,name,price,qty):
        self.id = id
        self.name = name
        self.price = price
        self.qty = qty

    def __repr__(self) -> str:
        return f"{self.id}: {self.name} : {self.price} : {self.qty} \n"


def fun(x):
    print(x,'x-xx')


class Shop:
    def __init__(self,name) :
        self.name  = name
        self.cart = dict()


    def add_product(self,id,name, price,qty):
        self.cart[id] = Product(id,name,price,qty)

    def buy_product(self,id):
        
        if(id in self.cart):
            
            if(self.cart[id].qty>0):
                print("Congratulation, Purchase Successful")
            else:
                print("Product is Not available")
            
        else:
            print("Product is Not available")





yeasin = Shop("Yeasin LTD")

yeasin.add_product(1,"Mobile",12_000,5)
yeasin.add_product(2,"Watch",500,8)


yeasin.buy_product(1)
yeasin.buy_product(3)













