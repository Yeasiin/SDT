

class Shop:
    cart = []

    def __init__(self,val):
        self.buyer = val

    def chang(self,val):
        self.cart.append(val)


af  = Shop("Afa")

af.chang("shoe")
af.chang("phone")

meh = Shop("Niso")

meh.chang("Helo")
meh.chang("Charger")

print(meh.cart)






