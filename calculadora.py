import numpy as np
import pandas as pd



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

def num(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def get_valid_value ():

    number = input("Insert the value: ")

    while not num(number):

        number = input('WRONG VALUE! \n Please, choose an enter value: ')

    number = int(number)

    return number

calc = Calculator()         

'''first_number = Datos.iloc[]
second_number = get_valid_value()
operator = input("Choose the operator: ")'''



Datos = pd.read_csv('DatosCalculadora.csv', delimiter='\t')
print(Datos)

for index, row in Datos.iterrows():
    first_number = row['num1']
    second_number = row['num2']
    operator = row['operador']
    resultado = 0

    if operator == '+':
        resultado = calc.add(first_number, second_number)
    elif operator =='-':
        resultado = calc.rest(first_number, second_number)
    elif operator =='*':
        resultado = calc.mult(first_number, second_number)
    elif operator =='/':
        resultado = calc.div(first_number, second_number)
        
    Datos.at[index, 'resultado'] = resultado

print(Datos)

Datos.to_csv('Datos_calculadora_resultado.csv')

        