class Item:
    def __init__(self, category, brand, price):
        self.category = category 
        self.brand = brand 
        self.price = price
        self.name = category.name+"-"+brand.name
    