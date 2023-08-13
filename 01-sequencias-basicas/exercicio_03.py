"""Crie um programa que leia o nome e o salário de um funcionário, mostrando no 
final uma mensagem. 
Ex: 
Nome do Funcionário: Maria do Carmo 
Salário: 1850,45 
O funcionário Maria do Carmo tem um salário de R$1850,45 em Junho."""

entrada_nome = input("Nome do Funcionário: ")

salario = float(input("Digite o salário do funcionário: "))

print(f"O(A) funcionário(a) {entrada_nome} tem um salário de R${salario:.2f} em Junho.")