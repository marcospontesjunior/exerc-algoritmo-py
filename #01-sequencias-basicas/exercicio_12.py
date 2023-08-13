"""Crie um programa que leia o preço de um produto, calcule e mostre o seu 
PREÇO PROMOCIONAL, com 5% de desconto."""

preco_produto = float(input("Digite o preço do produto: "))

desconto = preco_produto * 0.05
valor_final = preco_produto - desconto

print(f"O valor do produto é R${preco_produto:.2f}. Com 5% de desconto o valor final do produto é de: R${valor_final:.2f}")