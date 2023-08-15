"""[DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta. 
Analise seus comprimentos e diga se é possível formar um triângulo com essas 
retas. Matematicamente, para três segmentos formarem um triângulo, o comprimento 
de cada lado deve ser menor que a soma dos outros dois."""

def input_float(mensagem):
    while True:
        try:
            entrada = float(input(mensagem))
            return entrada
        except ValueError:
            print("Digite apenas valor numérico válido.")

def input_retas():
    reta_1 = input_float("Digite a distância o tamanho do primeiro de segmento de reta: ")
    reta_2 = input_float("Digite a distância o tamanho do segundo de segmento de reta: ")
    reta_3 = input_float("Digite a distância o tamanho do terceiro de segmento de reta: ")
    return reta_1, reta_2, reta_3

def verificar_triangulo(retas):
    reta_1, reta_2, reta_3 = retas
    if reta_1 + reta_2 > reta_3 and reta_1 + reta_3 > reta_2 and reta_2 + reta_3 > reta_1:
        return "podem formar um triângulo!"
    else:
        return "não podem formar um triângulo!"

def main():
    retas = input_retas()
    resultado = verificar_triangulo(retas)

    print(f"\nMatematicamente, para três segmentos formarem um triângulo, o comprimento de cada lado deve ser menor que a soma dos outros dois.\n"
          f"Os seguimentos de reta {retas} {resultado}\n")

main()