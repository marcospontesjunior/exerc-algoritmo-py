"""[DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o 
jogador vai tentar descobrir qual foi o valor sorteado."""

import random

escolhas = [1, 2, 3, 4, 5]

def input_int(mensagem):
    while True:
            entrada = int(input(mensagem))
            if entrada >= 1 and entrada <= 5:
                return entrada
            else:
                print("Entrada inválida. Escolha um número entre 1 e 5.")

def resultado(escolha_usuario, escolha_ia):
     if escolha_usuario == escolha_ia:
          return "Você adivinhou o número"
     else:
          return "Você errou. Tente mais uma vez!"

def main():
    escolha_ia = random.randint(1, 5)

    print("\nBem-vindo ao jogo de Adivinhação!\n"
          "Tente adivinhar o número escolhido pela IA.")

    escolha_usuario = input_int("\nDigite o número entre 1 e 5 para tentar adiivinhar o número: ") 

    resultado_jogo = resultado(escolha_usuario, escolha_ia)

    print(f"\nVocê escolheu o número: {escolha_usuario}\n"
          f"O número escolhido pela IA foi: {escolha_ia}\n" 
          f"\n{resultado_jogo}\n")

main()