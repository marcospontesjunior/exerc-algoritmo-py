"""Crie um programa que leia duas notas de um aluno e calcule a sua média, 
mostrando uma mensagem no final, de acordo com a média atingida: 
   - Média até 4.9: REPROVADO 
   - Média entre 5.0 e 6.9: RECUPERAÇÃO 
   - Média 7.0 ou superior: APROVADO"""

def input_float(mensagem):
    while True:
        try:
            entrada = float(input(mensagem))
            return entrada
        except ValueError:
            print("Digite apenas valor numérico válido.")
        
def input_numeros():
    nota_1 = input_float("\nDigite digite o valor da primeira nota: ")
    nota_2 = input_float("Digite digite o valor da segunda nota: ")
    return nota_1, nota_2

def media_notas(notas):
    return (sum(notas) / len(notas))

def resultado_notas(media):
    if media <= 4.9:
        return "foi REPROVADO!"
    elif 5 <= media <= 6.9:
        return "está de RECUPERAÇÃO!"
    else:
        return "foi APROVADO!"

def main():
    notas = input_numeros()
    media = media_notas(notas)
    resultado = resultado_notas(media)

    print(f"\nCom suas notas {notas} você {resultado}\n")

main()