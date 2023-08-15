"""Faça um algoritmo que pergunte a distância que um passageiro deseja 
percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para 
viagens até 200Km e R$0.45 para viagens mais longas."""

def input_float(mensagem):
    while True:
        try:
            entrada = float(input(mensagem))
            return entrada
        except ValueError:
            print("Digite apenas valor numérico válido.")

def calcular_distancia(distancia_percorrida):
    if distancia_percorrida <= 200:
        return distancia_percorrida * 0.50
    else:
        return distancia_percorrida * 0.45


def main(): 
    distancia_percorrida = input_float("Digite a distância em km que deseja percorrer: ")
    resulto_distancia = calcular_distancia(distancia_percorrida)

    print(f"\nPara uma distância até 200 km é cobrado um valor de R$0,50 por Km e acima disso o valor é de R$0,45\n"
          f"A distância desejada é de {distancia_percorrida:.0f} km, logo o valor cobrado será de R${resulto_distancia:.2f}\n")

main()