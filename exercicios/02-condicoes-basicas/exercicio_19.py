"""Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua 
média e mostre na tela. No final, analise a média e mostre se o aluno teve ou 
não um bom aproveitamento (se ficou acima da média 7.0)."""

def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

def main():
    nome = input("\nOlá, qual o seu nome: ")
    nota1 = float(input("Digite a nota da sua p1: "))
    nota2 = float(input("Digite a nota da sua p2: "))

    nota_media = calcular_media(nota1, nota2)

    if nota_media >= 7:
        print(f"\nOlá {nome}, sua média foi {nota_media} e você está aprovado.\n")
    else:
        print(f"\nOlá {nome}, sua média foi {nota_media} e você não obteve média suficiente para ser aprovado.\n")

main()