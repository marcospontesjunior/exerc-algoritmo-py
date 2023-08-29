"""Uma empresa precisa reajustar o salário dos seus funcionários, dando um 
aumento de acordo com alguns fatores. Faça um programa que leia o salário atual, 
o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa. 
No final, mostre o seu novo salário, baseado na tabela a seguir: 
 
- Mulheres 
  - menos de 15 anos de empresa: +5% 
  - de 15 até 20 anos de empresa: +12% 
  - mais de 20 anos de empresa: +23% 
- Homens 
  - menos de 20 anos de empresa: +3% 
  - de 20 até 30 anos de empresa: +13% 
  - mais de 30 anos de empresa: +25%
- Outros
  - menos de 20 anos de empresa: +4% 
  - de 20 até 30 anos de empresa: +12.5% 
  - mais de 30 anos de empresa: +24%"""


def input_float(mensagem):
    while True:
        try:
            entrada = float(input(mensagem))
            return entrada
        except ValueError:
            print("Digite apenas valor numérico válido.")


def input_genero(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada in ["H", "M", "O", "h", "m", "o"]:
            return entrada
        else:
            print("Escolha inválida. Tente novamente.")


def calcular_reajuste(genero, tempo_empresa, salario):
    if genero in ["H", "h"]:
        valor_reajuste = [0.03, 0.13, 0.25]
    elif genero in ["M", "m"]:
        valor_reajuste = [0.05, 0.12, 0.23]
    else:
        valor_reajuste = [0.04, 0.125, 0.24]

    if tempo_empresa <= 20:
        indice_reajuste = 0
    elif 20 < tempo_empresa <= 30:
        indice_reajuste = 1
    else:
        indice_reajuste = 2

    adicional = salario * valor_reajuste[indice_reajuste]
    return adicional


def main():
    genero = input_genero(
        "\nDigite H/h para Homem, M/m para Mulher ou O/o para Outro: ")
    tempo_empresa = input_float("Digite o tempo que trabalha na empresa: ")
    salario = input_float("Digite o valor do seu atual salário: ")

    adicional = calcular_reajuste(genero, tempo_empresa, salario)

    salario_com_reajuste = salario + adicional

    print(
        f"\nTrabalhando {tempo_empresa} anos com o novo reajuste, seu salário passará a ser de R${salario_com_reajuste}\n")


main()