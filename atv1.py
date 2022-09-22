# Faça um programa que calcule a raiz quadrada de um número n e trate os casos 
# em que n < 0.
# OBS: Utilize o módulo math para calcular a raiz quadrada.
from typing import Type
import math

def number_validate(number):
    if number < 0:
        raise TypeError("Número inválido. Não calculamos raiz negativa! Trabalhamos com números reais mas não com os imaginários!")

def calcula_raiz():
    try:
        numero = int(input("Digite um número para calcular a raiz: "))
        number_validate(numero)
        print(f'O resultado é: {math.sqrt(numero)}')
    except ValueError:
        print("Erro nos tipos de dados digitados")
        return

calcula_raiz()
