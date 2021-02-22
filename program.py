import pickle
from product import Product
from inventory import Inventory

def askForProduct():
    print("Please, write the name")
    name = input()
    print("Please, write the description")
    description = input()
    print("Please, write the quantity")
    quantity = input()
    product = Product(name, description, quantity)
    return product

inventory = Inventory([])
inventory.load()
inventory.print()

while(1 != 2):
    newproduct = askForProduct()
    inventory.addProduct(newproduct)
    inventory.print()
    inventory.save()