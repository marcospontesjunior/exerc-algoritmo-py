"""Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade 
dela e depois mostre se ela pode ou não votar."""

import datetime

def calcular_idade(ano, ano_nascimento):
    return ano - ano_nascimento 

def main():
    ano = datetime.date.today().year
    ano_nascimento = int(input("\nDigite o ano de seu nascimento: "))

    idade = calcular_idade(ano, ano_nascimento)

    if idade > 18:
        print(f"\nPessoas com idade acima de 18 anos estão aptas a votar.\n"
              f"Sua idade é de {idade} anos e você está apto a participar da festa da democracia!\n"
              "Exerça seu direito\n")
    else:
        print(f"\nSua idade é de {idade} anos e você está apto a votar. Aguarde mais um pouco para participar da festa da democracia!\n")

main()