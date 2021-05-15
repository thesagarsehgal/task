from Cart import Cart
from User import User
from typing import MutableMapping
from Inventory import Inventory
from Item import Item
from Brand import Brand
from Category import Category


milkCategory = Category("Milk", "MilkDesc")
chocolateCategory = Category("Chocolate", "ChocolateDesc")
butterCategory = Category("Butter", "ButterDesc")

amulBrand = Brand("Amul", "AmulDesc")
cadburyBrand = Brand("Cadbury", "CadburyDesc")
parlebrand = Brand("Parle", "ParleDesc")

amulMilk = Item(milkCategory, amulBrand, 25)
cadburyChocolate = Item(chocolateCategory, cadburyBrand, 25)
parleChocolate = Item(chocolateCategory, parlebrand, 25)
amulButter = Item(butterCategory, amulBrand, 10)

myInventory = Inventory()
myInventory.addItemQuantity(amulMilk, 10)
myInventory.addItemQuantity(amulButter, 20)
myInventory.addItemQuantity(cadburyChocolate, 20)
myInventory.addItemQuantity(parleChocolate, 15)

# amitUser = User("Amit",500)
# cart1 = Cart(amitUser)
# cart1.addProductToCart(amulMilk,5)
# cart1.addProductToCart(cadburyChocolate,10)
# cart1.updateCart(amulMilk,4)
# cart1.removeFromCart(amulMilk)
# cart1.getCart()
# myInventory.cartCheckout(cart1)

# gokuUser = User("Goku",-10)
# cart2 = Cart(gokuUser)
# cart2.addProductToCart(amulMilk,50)
# cart2.addProductToCart(cadburyChocolate,100)
# cart2.updateCart(amulMilk,40)
# cart2.removeFromCart(amulMilk)
# cart2.getCart()
# myInventory.cartCheckout(cart2)

# myuser1 = User("myuser1",10000)
# cart3 = Cart(myuser1)
# cart3.addProductToCart(amulMilk,50)
# cart3.addProductToCart(cadburyChocolate,100)
# cart3.updateCart(amulMilk,40)
# cart3.removeFromCart(amulMilk)
# cart3.getCart()
# myInventory.cartCheckout(cart3)

# myuser2 = User("myuser3",1000)
# cart4 = Cart(myuser2)
# cart4.addProductToCart(amulMilk,50)
# cart4.addProductToCart(cadburyChocolate,5)
# cart4.getCart()
# myInventory.cartCheckout(cart4)

# myuser3 = User("myuser3",1000)
# cart5 = Cart(myuser3)
# cart5.addProductToCart(amulMilk,50)
# cart5.addProductToCart(cadburyChocolate,5)
# cart5.getCart()
# myInventory.cartCheckout(cart5)

myuser4 = User("myuser4",1125)
cart6 = Cart(myuser4)
cart6.addProductToCart(amulMilk,50)
cart6.getCart()
cart6.addProductToCart(cadburyChocolate,5)
cart6.getCart()
amulMilk.price = 20
cart6.getCart()
myInventory.cartCheckout(cart6)
