"""Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O 
aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para 
carro de luxo. Além disso, o cliente paga por Km percorrido. Faça um programa 
que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e 
quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a 
tabela a seguir: 
 
   - Carros populares (aluguel de R$90 por dia) 
      - Até 100Km percorridos: R$0,20 por Km 
      - Acima de 100Km percorridos: R$0,10 por Km 
   - Carros de luxo (aluguel de R$150 por dia) 
      - Até 200Km percorridos: R$0,30 por Km 
      - Acima de 200Km percorridos: R$0,25 por Km"""

def input_letras(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.isalpha():
            return entrada
        else:
            print("Digite apenas letras.")        

def input_int(mensagem):
    while True:
        try:
            entrada = int(input(mensagem))
            return entrada
        except ValueError:
            print("Digite apenas valor numérico válido.")

def input_escolha_veiculo(mensagem):
    while True:
            entrada = int(input(mensagem))
            if entrada >= 1 and entrada <= 2:
                return entrada
            else:
                print("Escolha inválida. Tente novamente.")            
 
def calculo_diaria(resultado_usuario, dias_aluguel):
    if resultado_usuario == "Popular":
        return dias_aluguel * 90
    else:
        return dias_aluguel * 150
    
def calculo_km_rodado(resultado_usuario, km_rodados):
    if resultado_usuario == "Popular":
        valor_km = 0.2 if km_rodados <= 100 else 0.1
    else:
        valor_km = 0.3 if km_rodados <= 200 else 0.25
    return km_rodados * valor_km
                    
def main():

    print("\nAluguel de veículos!")

    nome = input_letras("\nDigite seu nome: ")
    modelo_veiculo = input_escolha_veiculo("Digite 1 para modelo popular ou 2 para modelo de luxo: ")
    dias_aluguel = input_int("Digite a quantidade de dias do aluguel do veículo: ")
    km_rodados = input_int("Digite a quantidade de km rodados: ")

    resultado_usuario = "Popular" if modelo_veiculo == 1 else "Luxo"
    valor_diaria = calculo_diaria(resultado_usuario, dias_aluguel)
    valor_km_rodado = calculo_km_rodado(resultado_usuario, km_rodados)

    valor_final = valor_diaria + valor_km_rodado

    print("\n---- TABELA ----")
    print(f"\nÀ diária de um carro 'Popular' é de R$90,00 e de um carro 'Luxo' é de R$150,00\n"
          f"\nValor para Km rodados:"
          f"\nPopular: até 100km percorrido é cobrado R$0,20 per km. Acima de 100km é cobrado o valor R$0,10 per km."
          f"\nLuxo: até 200km percorrido é cobrado R$0,30 per km. Acima de 200km é cobrado o valor R$0,25 per km.\n")
    print("----------------")

    print(f"\nOlá {nome}, o modelo do veículo escolheido foi '{resultado_usuario}'.")
    print(f"O valor da sua diária com o modelo escolhido foi: R${valor_diaria:.2f} e o valor per Km rodado foi de R${valor_km_rodado:.2f}"
          f"\nSendo assim, o valor final a ser pago é de: R${valor_final:.2f}\n")
    
main()