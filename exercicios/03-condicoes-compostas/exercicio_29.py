"""Desenvolva um programa que leia o nome de um funcionário, seu salário, 
quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de 
acordo com a tabela a seguir: 
   - Até 3 anos de empresa: aumento de 3% 
   - entre 3 e 10 anos: aumento de 12.5% 
   - 10 anos ou mais: aumento de 20%"""

def input_letras(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.isalpha():
            return entrada
        else:
            print("Digite apenas letras.")

def input_float(mensagem):
    while True:
        try:
            entrada = float(input(mensagem))
            return entrada
        except ValueError:
            print("Digite apenas valor numérico válido.")

def input_int(mensagem):
    while True:
        try:
            entrada = int(input(mensagem))
            return entrada
        except ValueError:
            print("Digite apenas valor numérico válido.")

def calcular_aumento(salario_funcionario, anos_trabalhando):
    if anos_trabalhando <= 3:
        return salario_funcionario + (salario_funcionario * 0.03)
    elif 3 < salario_funcionario <= 10:
        return salario_funcionario + (salario_funcionario * 0.125)
    else:
        return salario_funcionario + (salario_funcionario * 0.2)
    
def aumento(anos_trabalhando):
    if anos_trabalhando <= 3:
        return "3%"
    elif 3 < anos_trabalhando <= 10:
        return "12.5%"
    else:
        return "2%"

def main():
    nome_funcionario = input_letras("\nInforme o nome do funcionário: ")
    salario_funcionario = input_float("Informe o salário deste funcionário: ")
    anos_trabalhando = input_int("Informe quantos anos trabalhados na empresa: ")
    calculo = calcular_aumento(salario_funcionario, anos_trabalhando)
    valor_aumento = aumento(anos_trabalhando)

    print(f"\nOlá colaborador {nome_funcionario}, seu atual salário é de R${salario_funcionario}.\n"
          f"Por trabalhar na nossa empresa pelo tempo de {anos_trabalhando} ano(s), você terá uma aumento de {valor_aumento}!\n"
          f"A partir do próximo mês seu salários será de R${calculo}\n")

main()