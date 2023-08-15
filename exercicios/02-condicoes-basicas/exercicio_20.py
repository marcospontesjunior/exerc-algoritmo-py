"""Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou 
ÍMPAR."""

def num_par(num):
    return num % 2

def main():
    num = int(input("\nDigite um número inteiro: "))

    resultado = (num_par(num))

    if resultado == 0:
        print(f"\nO número {num} é PAR!\n")
    else:
        print(f"\nO número {num} é IMPAR!\n")

main()