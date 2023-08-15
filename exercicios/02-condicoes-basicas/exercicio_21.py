"""Faça um algoritmo que leia um determinado ano e mostre se ele é ou não 
BISSEXTO."""

def ano_bissexto(num):
    return num % 4

def main():
    ano = int(input("\nDigite um ano para saber se ele é(foi) bissexto: "))

    resultado = (ano_bissexto(ano))

    if resultado == 0:
        print(f"\nO ano {ano} foi/é ano bissexto!\n")
    else:
        print(f"\nO ano {ano} não foi/é um ano bissexto!\n")

main()