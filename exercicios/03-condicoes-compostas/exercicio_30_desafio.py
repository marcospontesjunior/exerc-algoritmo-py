"""[DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo 
de triângulo será formado:  
   - EQUILÁTERO: todos os lados iguais 
   - ISÓSCELES: dois lados iguais 
   - ESCALENO: todos os lados diferentes"""


def input_float(mensagem):
    while True:
        try:
            entrada = float(input(mensagem))
            return entrada
        except ValueError:
            print("Digite apenas valor numérico válido.")


def input_retas():
    reta_1 = input_float(
        "Digite a distância o tamanho do primeiro de segmento de reta: ")
    reta_2 = input_float(
        "Digite a distância o tamanho do segundo de segmento de reta: ")
    reta_3 = input_float(
        "Digite a distância o tamanho do terceiro de segmento de reta: ")
    return reta_1, reta_2, reta_3


def verificar_triangulo(retas):
    reta_1, reta_2, reta_3 = retas
    if reta_1 + reta_2 > reta_3 and reta_1 + reta_3 > reta_2 and reta_2 + reta_3 > reta_1:
        if reta_1 == reta_2 and reta_1 == reta_3:
            return "forma um triângulo EQUILÁTERO!"
        elif reta_1 == reta_2 or reta_1 == reta_3 or reta_2 == reta_3:
            return "forma um triângulo ISÓSCELES!"
        else:
            return "forma um triângulo ESCALENO!"
    else:
        return "não podem formar um triângulo!"


def main():
    retas = input_retas()
    resultado = verificar_triangulo(retas)

    print(f"\nOs seguimentos de reta {retas} {resultado}\n")

main()