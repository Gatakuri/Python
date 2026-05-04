class Cart:
    def __init__(self):
        self._products = []

    def insert_products(self, *products):
        for product in products:
            self._products.append(product)

    def list_products(self):
        print()
        for product in self._products:
            print(product.name, product.price)
        print()

    def total_price(self):
        return sum([p.price for p in self._products])
    
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

cart = Cart()
p1 = Product("Donut", 3.20)
p2 = Product("Tshirt", 20)
p3 = Product("Burguer", 1.80)
cart.insert_products(p1, p2, p3)
cart.list_products()
print(cart.total_price())