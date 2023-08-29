"""Um programa de vida saudável quer dar pontos atividades físicas que podem 
ser trocados por dinheiro. O sistema funciona assim: 
 
   - Cada hora de atividade física no mês vale pontos 
      - até 10h de atividade no mês: ganha 2 pontos por hora 
      - de 10h até 20h de atividade no mês: ganha 5 pontos por hora 
      - acima de 20h de atividade no mês: ganha 10 pontos por hora 
   - A cada ponto ganho, o cliente fatura R$0,05 (5 centavos)   
 
Faça um programa que leia quantas horas de atividade uma pessoa teve por mês, 
calcule e mostre quantos pontos ela teve e quanto dinheiro ela conseguiu ganhar."""

import time


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
            print("Digite apenas valor numérico válido e/ou use (.) em vez de (,).")


def calcular_pontos(horas_exercicio):
    pontos_por_hora = 0

    if horas_exercicio <= 10:
        pontos_por_hora = 2
    elif 10 < horas_exercicio <= 20:
        pontos_por_hora = 5
    else:
        pontos_por_hora = 10

    horas_exercicio = int(horas_exercicio) + \
        (horas_exercicio - int(horas_exercicio)) * 100 / 60

    pontos_total = horas_exercicio * pontos_por_hora
    return pontos_total


def main():

    print("\nBem-Vindo ao aplicativo Ponto de Vida!\n")

    nome = input_letras("\nDigite seu nome: ")
    horas_exercicio = input_float(
        f"{nome}, digite quantas horas executou de exercício no mês (ex.: horas.minutos): ")

    pontos = calcular_pontos(horas_exercicio)

    valor = pontos * 0.05

    print("\n------------------------------TABELA------------------------------")
    print(f"\nCada hora de atividade física no mês vale pontosn"
          f"\n  - até 10h de atividade no mês: ganha 2 pontos por hora "
          f"\n  - de 10h até 20h de atividade no mês: ganha 5 pontos por hora"
          f"\n  - acima de 20h de atividade no mês: ganha 10 pontos por hora"
          f"\n  - A cada ponto ganho, fatura R$0,05 (5 centavos)")
    print("\n-------------------------------------------------------------------")

    time.sleep(2)

    print(f"\n{nome}, você conquistou {pontos:.1f} com seus exercícios."
          f"\nSendo assim, resgatando seus pontos, você leva um total de R${valor:.2f}\n")


main()