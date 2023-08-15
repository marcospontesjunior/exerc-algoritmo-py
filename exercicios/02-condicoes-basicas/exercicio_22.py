"""Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua 
situação em relação ao alistamento militar. 
   - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o 
alistamento. 
   - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do 
alistamento. """

import datetime

def calcular_idade(ano, ano_nascimento):
        return ano - ano_nascimento

def calcular_anos(idade):
    if idade < 18:
        return 18 - idade
    else:
         return idade - 18

def main():
    ano = datetime.date.today().year

    ano_nascimento = int(input("\nDigite o ano de seu nascimento: "))

    idade = calcular_idade(ano, ano_nascimento)
    anos_faltantes = calcular_anos(idade)

    if idade < 18:
        print(f"\nPessoas com 18 anos de idade precisam alistar no exército.\n"
              f"Sua idade é de {idade} anos e você não está apto a se alistar ainda.\n"
              f"Aguarde mais {anos_faltantes} anos para completar 18 e se alistar no posto do exército mais próximo!\n")
    else:
        print(f"\nSua idade é de {idade} anos e já se passaram {anos_faltantes} anos do seu alistamento.\n")

main()