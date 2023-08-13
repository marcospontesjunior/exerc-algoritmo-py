"""Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o 
seu novo salário, com 15% de aumento."""

entrada_salario = float(input("Digite o atual salário do funcionário: "))

calco_aumento = entrada_salario * 0.15
salario_final = entrada_salario + calco_aumento

print(f"O valor final do salário do funcionário com o aumento de 15% é de R${salario_final:.2f}")