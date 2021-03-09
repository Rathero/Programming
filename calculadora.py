class Calculadora():

    def add (self, first_number, second_number):
        return first_number + second_number 
    def rest (self, first_number, second_number):
        return first_number - second_number 
    def mult (self, first_number, second_number):
        return first_number * second_number 
    def is_valid_operator (self, operator):
        return operator == '+' or operator =='-' or operator =='*'
         
first_number = int(input("Insert the first value: "))
second_number = int(input("Insert the second value: "))
operator = input("Choose the operator: ")
calc = Calculadora()

while not calc.is_valid_operator(operator):

    operator = input("Choose a valid operator (+,-,*): ")


if operator == '+':
    resultado = calc.add(first_number, second_number)
elif operator =='-':
    resultado = calc.rest(first_number, second_number)
elif operator =='*':
    resultado = calc.mult(first_number, second_number)

print(resultado)
