from Item import Item


class Inventory:
    def __init__(self):
        self.inventory = {}
    
    def getInventory(self):
        for item in self.inventory:
            print(item.name,self.inventory[item])

    def addItemQuantity(self, item, quantity):
        if(item not in self.inventory):
            self.inventory[item]=quantity
        else:
            self.inventory[item]+=quantity
    
    def checkAvailablity(self, itemList):
        for i in itemList:
            if(i not in self.inventory or self.inventory[i]<itemList[i]):
                return False
        return True
    
    def buyItems(self, itemList):
        for i in itemList:
            if(i in self.inventory and self.inventory[i]>=itemList[i]):
                self.inventory[i]-=itemList[i]

    def cartCheckout(self, cart):
        if(cart.checkout==True):
            print("Cart already checked out")
            return 
        cartPrice = 0
        for i in cart.cart:
            cartPrice+=cart.cart[i]*i.price
        
        if(cart.user.walletAmount >= cartPrice):
            if(self.checkAvailablity(cart.cart)):
                self.buyItems(cart.cart)
                cart.user.walletAmount-=cartPrice
                cart.checkout = True
                print("Sucessfully buyed items in the cart ... ")
            else:
                print("not enough items in the cart")
        else:
            print("Not enough balance with the user")
    
                