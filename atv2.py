# Faça um programa que calcule a divisão de dois números m e n e trate os casos em
# que n = 0.
from decimal import Decimal

def validate_denominator(denominador):
    if denominador == 0:
        raise TypeError("Não existe divisão por zero!")

def divisao():
    try:
        numerator = int(input("Digite o numerador: "))
        denominator = int(input("Digite o denominador: "))
        validate_denominator(denominator)
        print(f"O resultado é: {Decimal(numerator/denominator)}")
    except ZeroDivisionError:
        print("Não é possível dividir um número por zero")
        return
    
divisao()