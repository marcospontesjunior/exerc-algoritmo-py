"""Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando 
na tela uma das mensagens abaixo: 
   - O primeiro valor é o maior 
   - O segundo valor é o maior 
   - Não existe valor maior, os dois são iguais"""

def input_int(mensagem):
    while True:
        try:
            entrada = int(input(mensagem))
            return entrada
        except ValueError:
            print("Digite apenas valor numérico inteiro válido.")
        
def input_numeros():
    numero_1 = input_int("\nDigite digite o valor do primeiro número inteiro: ")
    numero_2 = input_int("Digite digite o valor do segundo número inteiro: ")
    return numero_1, numero_2

def comparar_numeros(numeros):
    numero_1, numero_2 = numeros
    if numero_1 > numero_2:
        return "o primeriro valor é o maior!"
    elif numero_1 < numero_2:
        return "o segundo valor é o maior"
    else:
        return "não existe valor maior, os dois são iguais!"

def main():
    numeros = input_numeros()
    resultado = comparar_numeros(numeros)

    print(f"\nNos valores {numeros} {resultado}\n")

main()