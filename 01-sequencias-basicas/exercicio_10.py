"""Faça um algoritmo que leia a largura e altura de uma parede, calcule e 
mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, 
sabendo que cada litro de tinta pinta uma área de 2metros quadrados."""

def area (largura, altura):
    if altura == largura:
        return altura ** 2
    else:
        return altura * largura

largura = float(input("Digite a largura da parade: "))
altura = float(input("Digite a altura da parade: "))

area_parede = area(largura, altura)
qtd_tinta = area_parede / 2

print(f"A área da parede é de {area_parede}m² e será necessário {qtd_tinta}L de tinta para pintar a parede por completo!")