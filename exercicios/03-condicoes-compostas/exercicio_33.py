"""Escreva um programa para aprovar ou não o empréstimo bancário para a compra 
de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e 
em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que 
ela não pode exceder 30% do salário ou então o empréstimo será negado."""

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

def calcular_prestacao(salario):
    return salario * 0.3

def prestacao_emprestimo(valor_casa, anos_pagando):
    return valor_casa / (anos_pagando * 12)

def condicao_emprestimo(prestacao_maxima, prestacao_mensal):
    if prestacao_mensal <= prestacao_maxima:
        return "aprovado"
    else:
       return "negado"
   
def main():
    nome = input_letras("\nInforme o seu nome: ")
    valor_casa = input_float(f"Olá {nome}! Informe o valor desajado para o empréstimo: ")
    salario = input_float("Agora informe o seu salário: ")
    anos_pagando = input_float("Digitem em quantos anos deseja pagar: ")

    prestacao_maxima = calcular_prestacao(salario)
    prestacao_mensal = prestacao_emprestimo(valor_casa, anos_pagando)

    resultado = condicao_emprestimo(prestacao_maxima, prestacao_mensal)

    print(f"\nCom os dados informados seu emprestimo foi {resultado}!\n")

main()