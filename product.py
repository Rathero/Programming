class Product:
    #Atributos
    name = ""
    description = ""
    quantity = 0

    #Constructor
    def __init__(self, name, description, quantity):
        self.name = name
        self.description = description
        self.quantity = quantity

    #Funcion
    def print(self):
        print("-----------------------------------------")
        print("Product name: " + self.name)
        print("Description: " + self.description)
        print("Quantity: " + str(self.quantity))
        print("-----------------------------------------")