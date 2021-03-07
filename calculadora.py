class Calculadora():
    def __init__(self):
        """Inicializa la calculadora"""
        self.valor = 0
    def suma (self, n):
        """suma un numero n al valor"""
        self.valor += n 
    def resta (self, n):
        """resta un numero n al valor"""
        self.valor -= n
    def mult (self, n):
        """multiplica un numero n al valor"""
        self.valor = self.valor * n
    def getValor(self):
        """Obtiene el valor"""
        return self.valor

calc = Calculadora()
calc.suma(2)
print(calc.getValor())
calc.mult(2)
print(calc.getValor())
