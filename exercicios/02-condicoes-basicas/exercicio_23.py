"""Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos 
para todos, mas especialmente para mulheres. Faça um programa que leia nome, 
sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo 
que: 
   - Homens ganham 5% de desconto 
   - Mulheres ganham 13% de desconto
   - Outros ganham 10% de desconto"""

def input_letras(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.isalpha():
            return entrada
        else:
            print("Digite apenas letras.")

def input_opcao(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.lower() in ['m', 'f', 'o']:
            return entrada.lower()
        else:
            print("Digite apenas 'm', 'f' ou 'o'.")

def input_float(mensagem):
    while True:
        try:
            entrada = float(input(mensagem))
            return entrada
        except ValueError:
            print("Digite apenas valor numérico válido.")

def calcular_desconto(opcao, preco_produto):
    if opcao == "m":
        return preco_produto * 0.05
    elif opcao == "f":
        return preco_produto * 0.13
    else:
        return preco_produto * 0.10

def main():
    nome = input_letras("Digite seu nome: ")
    opcao = input_opcao("Escolha uma opção (M para masculino, F para feminino, O para outro): ")
    preco_produto = input_float("Digite o valor do produto: ")
    desconto = calcular_desconto(opcao, preco_produto)

    preco_com_desconto = preco_produto - desconto

    if opcao == "f":
        print(f"\nOlá, {nome}!\n"
              f"O preço original do produto é: R${preco_produto:.2f}\n"
              f"Você escolheu a opção '{opcao}', com desconto de R${desconto:.2f}\n"
              f"O preço com desconto é: R${preco_com_desconto:.2f}\n"
              f"Parabéns pelo seu dia. Feliz Dia da Mulher!\n")
    else:
        print(f"\nOlá, {nome}!\n"
              f"O preço original do produto é: R${preco_produto:.2f}\n"
              f"Você escolheu a opção '{opcao}', com desconto de R${desconto:.2f}\n"
              f"O preço com desconto é: R${preco_com_desconto:.2f}\n")

main()