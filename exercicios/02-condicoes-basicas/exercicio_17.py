"""Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 
80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba 
o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida."""

def valor_multa(km_acima, valor_per_km):
        return km_acima * valor_per_km

def main():
    valor_per_km = 5
    velocidade_carro = float(input("\nDigite a velocidade do carro: "))
    km_acima = velocidade_carro - 80
    
    if velocidade_carro > 80:
        valor_da_multa = valor_multa(km_acima, valor_per_km)
        print("\nVelocidade acima de 80km/h recebem uma multa de R$5,00 por cada km acima.\n"
            f"A velocidade do seu carro foi de {velocidade_carro} ultrapassando a velocidade limite!\n"
            f"Seu carro teve {km_acima}km/h acima do permitido. O valor da sua multa é de {valor_da_multa:.2f}\n")
    else:
        print("Tudo certo! Seu carro estava dentro dos limites de velocidade.")

main()