"""Faça um programa que leia um número inteiro e mostre o seu antecessor e seu 
sucessor. 
Ex:  
Digite um número: 9 
O antecessor de 9 é 8 
O sucessor de 9 é 10"""

valor = int(input("Digite um número: "))

antecessor = valor - 1
sucessor = valor + 1

print(f"O antecessor de {valor} é {antecessor}.\nO sucessor de {valor} é {sucessor}.")