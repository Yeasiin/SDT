class Order:
    def __init__(self):
        self.items = {}

    def add_item(self,item):
        if item in self.items:
            self.items[item] += item.quantity # if already in cart
        else:
            self.items[item] = item.quantity

    def delete_item(self,item):
        if item in self.items:
            del self.items[item]


    @property
    def total_price(self):
        price = 0

        for item,quantity in self.items.items():
            price += (item.price * quantity)
        return price
    
    def clear(self):
        self.items={}


