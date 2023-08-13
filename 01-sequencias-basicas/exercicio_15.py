"""Crie um programa que leia o número de dias trabalhados em um mês e mostre o 
salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25 
por hora trabalhada."""

def calco_salario(dias_trabalhados, horas_diaria, valor_hora):
    return dias_trabalhados * (horas_diaria * valor_hora)

dias_trabalhados = int(input("Digite a quantidade de dias trabalhados: "))

horas_diaria = 8
valor_hora = 25

salario = calco_salario(dias_trabalhados, horas_diaria, valor_hora)

print(f"O salário total do funcionário é R${salario:.2f}")