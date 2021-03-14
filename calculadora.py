class Calculator():

    def add (self, first_number, second_number):
        return first_number + second_number 
    def rest (self, first_number, second_number):
        return first_number - second_number 
    def mult (self, first_number, second_number):
        return first_number * second_number 
    def div (self, first_number, second_number):
        return first_number / second_number 
    def is_valid_operator (self, operator):
        return operator == '+' or operator =='-' or operator =='*' or operator == '/'
    def valid_first_number (self, first_number):
        return isinstance(first_number, int) 
    def valid_second_number (self, second_number):
        return isinstance(second_number, int)

calc = Calculator()         

first_number = input("Insert the first value: ")

while not calc.valid_first_number(first_number):

    first_number = int(input('WRONG VALUE! n\ Please, choose an enter value: '))

second_number = int(input("Insert the second value: "))

while not calc.valid_second_number(second_number):

   second_number = input('WRONG!! n\ Please select an enter value')

operator = input("Choose the operator: ")

while not calc.is_valid_operator(operator):

    operator = input("Choose a valid operator (+,-,*,/): ")


if operator == '+':
    resultado = calc.add(first_number, second_number)
elif operator =='-':
    resultado = calc.rest(first_number, second_number)
elif operator =='*':
    resultado = calc.mult(first_number, second_number)
elif operator =='/':
    resultado = calc.div(first_number, second_number)

print(resultado)
