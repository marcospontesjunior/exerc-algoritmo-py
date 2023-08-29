# [DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)

import random

escolhas = ["Pedra", "Papel", "Tesoura"]

def input_int(mensagem):
    while True:
            entrada = int(input(mensagem))
            if entrada >= 1 and entrada <= len(escolhas):
                return entrada
            else:
                print("Escolha inválida. Tente novamente.")

def jokenpo(escolha_usuario, escolha_ia):
    if escolha_usuario == escolha_ia:
        return "Empate!"
    elif (escolha_usuario == "Pedra" and escolha_ia == "Tesoura") or \
         (escolha_usuario == "Tesoura" and escolha_ia == "Papel") or \
         (escolha_usuario == "Papel" and escolha_ia == "Pedra"):
        return "Você ganhou!"
    else:
        return "Você perdeu!"

def usuario_escolha(escolha_usuario):
    if escolha_usuario == 1:
        return "Pedra"
    elif escolha_usuario == 2:
        return "Papel"
    else:
        return "Tesoura"
    
def main():
    escolha_ia = random.choice(escolhas)

    print("\nBem-vindo ao jogo de Pedra-Papel-Tesoura!")
    print("Escolha uma opção:")

    for index, escolha in enumerate(escolhas, start=1):
        print(f"{index}: {escolha}")

    escolha_usuario = input_int("\nDigite o número da sua escolha: ") 
    resultado_usuario = usuario_escolha(escolha_usuario)  
    resultado = jokenpo(resultado_usuario, escolha_ia)  

    print(f"\n\nVocê escolheu: {resultado_usuario}\n"
          f"O computador escolheu: {escolha_ia}\n"  
          f"{resultado}\n")

main()