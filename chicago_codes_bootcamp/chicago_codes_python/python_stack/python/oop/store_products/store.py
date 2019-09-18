class Store:
    def __init__(self, name, products):
        self.name = name
        self.products = Product(name='PS4', price=100, category="electronics")

    def add_product(self, new_product):
        self.new_product = new_product
    def sell_product(self, id):
        self.id

    def inflation(self, percent_increase):
        self.price


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    
    def update_price(self, percent_change, is_increased):
        if self.is_increased:
            self.price += self.percent_change
        else:
            self.price -= self.percent_change
            
    def print_info(self):
        print(self.name)
        print(self.category)
        print(self.price)






