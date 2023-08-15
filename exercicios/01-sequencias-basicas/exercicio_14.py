"""A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva 
um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, 
sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado."""

km_rodado = float(input("Digite os km percorrido: "))
diaria = int(input("Digite a quantidade de dias alugados: "))

km_rodado = km_rodado * 0.20
valor_diaria = diaria * 90
valor_total = km_rodado + valor_diaria

print(f"Para cada km rodado o valor é de R$0,20 e a diária tem um custo de R$90." 
      f"\nO valor por dia é de R${valor_diaria:.2f}, o de km rodada é de R${km_rodado:.2}."
      f"\nSendo assim um valor total final sendo de R${valor_total:.2f}")