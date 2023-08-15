"""Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) 
e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45."""

valor = float(input("Digite o valor para ser convertido: "))

converter = valor * 3.45

print(f"O valor R${valor} convertido para Dólar é de US${converter:.2f}")