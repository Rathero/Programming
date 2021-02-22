import pickle

class Inventory:
    #Atributos
    products = []
    filename = 'outfile'

    #Constructor
    def __init__(self, products):
        self.products = products

    #Funcion
    def print(self):
        for product in self.products:
            product.print()

    def load(self):
        with open (self.filename, 'rb') as fp:
            self.products = pickle.load(fp)

    def save(self):
        with open(self.filename, 'wb') as fp:
            pickle.dump(self.products, fp)
#guardar
    def addProduct(self, product):
        self.products.append(product)