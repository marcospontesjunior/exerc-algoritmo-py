"""O Índice de Massa Corpórea (IMC) é um valor calculado baseado na altura e no 
peso de uma pessoa. De acordo com o valor do IMC, podemos classificar o 
indivíduo dentro de certas faixas. 
 
   - abaixo de 18.5: Abaixo do peso 
   - entre 18.5 e 25: Peso ideal 
   - entre 25 e 30: Sobrepeso 
   - entre 30 e 40: Obesidade 
   - acima de 40: Obseidade mórbida 
 
Obs: O IMC é calculado pela expressão peso/altura² (peso dividido pelo quadrado 
da altura)"""

def input_letras(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.isalpha():
            return entrada
        else:
            print("Digite apenas letras.")        

def input_float(mensagem):
    while True:
        try:
            entrada = float(input(mensagem))
            return entrada
        except ValueError:
            print("Digite apenas valor numérico válido.")

def calcular_imc(peso, altura):
    return peso / (altura * 0.01) ** 2

def tabela_imc(resultado_calculo_imc):
    if resultado_calculo_imc < 18.5:
        return "ABAIXO DO PESO"
    elif resultado_calculo_imc < 25:
        return "PESO IDEAL"
    elif resultado_calculo_imc < 30:
        return "SOBREPESO"  
    elif resultado_calculo_imc < 35:
        return "OBESIDADE I"
    elif resultado_calculo_imc < 40:
        return "OBESIDADE II"
    else:
        return "OBESIDADE III" 

def main():
    print("\nCálculo de IMC - Vamos começar!!")

    nome = input_letras("\nDigite seu nome: ")
    peso = input_float(f"Digite o seu peso: ")
    altura = input_float("Agora, digite a sua altura em cm: ")

    resultado_calculo_imc = calcular_imc(peso, altura)
    resultado_tabela_imc = tabela_imc(resultado_calculo_imc)

    print(f"\n{nome}, com os dados informados, o resultado do seu cálculo de IMC é: {resultado_calculo_imc:.2f} \n-> {resultado_tabela_imc}\n")

main()