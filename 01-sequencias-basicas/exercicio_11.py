"""Desenvolva uma lógica que leia os valores de A, B e C de uma equação do 
segundo grau e mostre o valor de Delta."""

def calc_delta(a, b, c):
    return b ** 2 - 4 * a * c

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = calc_delta(a, b, c)

print(f"O valor de Delta é {delta}")