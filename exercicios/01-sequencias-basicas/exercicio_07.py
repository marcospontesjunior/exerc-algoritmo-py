"""Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a 
sua terça parte. 
Ex:  
Digite um número: 3.5 
O dobro de 3.5 é 7.0 
A terça parte de 3.5 é 1.16666"""

numero = float(input("Digite um número: "))

dobro = numero * 2 
terca_parte = numero / 3

print(f"O dobro de {numero} é {dobro}.\nA terça parte de {numero} é {terca_parte:.5f}.")