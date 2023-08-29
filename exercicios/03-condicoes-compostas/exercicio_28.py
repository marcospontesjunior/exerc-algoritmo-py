"""Faça um programa que leia a largura e o comprimento de um terreno 
retangular, calculando e mostrando a sua área em m². O programa também 
devemostrar a classificação desse terreno, de acordo com a lista abaixo: 
   - Abaixo de 100m² = TERRENO POPULAR 
   - Entre 100m² e 500m² = TERRENO MASTER 
   - Acima de 500m² = TERRENO VIP"""

def input_float(mensagem):
    while True:
        try:
            entrada = float(input(mensagem))
            return entrada
        except ValueError:
            print("Digite apenas valor numérico válido.")
        
def input_medidas():
    largura = input_float("\nDigite digite a largura do terreno: ")
    comprimento = input_float("Digite digite o comprimento do terreno: ")
    return largura, comprimento

def area_terreno(medidas):
    largura, comprimento = medidas
    if comprimento == largura:
        return comprimento ** 2
    else:
        return comprimento * largura

def classificacao_terreno(area):
    if area < 100:
        return "TERRENO POPULAR!"
    elif 100 <= area <= 500:
        return "TERRENO MASTER!"
    else:
        return "TERRENO VIP!"

def main():
    medidas = input_medidas()
    area = area_terreno(medidas)
    classificacao = classificacao_terreno(area)

    print(f"\nCom essas medidas o terreno tem {area}m². A classificação do terreno é: {classificacao}\n")

main()