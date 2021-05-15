class Cart:
    def __init__(self,user):
        self.user = user 
        self.cart = {}
        self.checkout = False
    
    def addProductToCart(self, item, quantity):
        if(item not in self.cart):
            self.cart[item] = 0
        self.cart[item] = quantity
        
    
    def updateCart(self, item, quantity):
        if(item in self.cart):
            self.cart[item] = quantity
        else:
            print(item.category.name,item.brand.name,"is not present in the cart ... so cannot update")

    
    def removeFromCart(self, item):
        if(item in self.cart):
            del self.cart[item]
        else:
            print(item.category.name,item.brand.name,"is not present in the cart ... so cannot remove")

    
    def getCart(self):
        cartPrice = 0
        for i in self.cart:
            print(i.category.name,i.brand.name,self.cart[i])
            cartPrice+=self.cart[i]*i.price
        print("Total Amount=>",cartPrice)