"""[DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um 
fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele 
já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule 
quantos dias de vida um fumante perderá e exiba o total em dias."""

def calcular_cigarros_fumados(cigarros_fumados_dia, anos_fumando, fator_conversor):
    dias_fumando = anos_fumando * fator_conversor
    return int(cigarros_fumados_dia * dias_fumando)

def calcular_tempo_perdido(cigarros_total_fumados, tempo_perdido_per_cigarro):
    return cigarros_total_fumados * tempo_perdido_per_cigarro

def calcular_dias_perdidos(minutos_perdidos):
    return minutos_perdidos // (24 * 60)

cigarros_fumados_dia = int(input("Digite a qtd de cigarros fumados por dia: "))
anos_fumando = int(input("Digite quantos anos é fumante: "))

tempo_perdido_per_cigarro = 10
fator_conversor = 365.25

cigarros_total_fumados = calcular_cigarros_fumados(cigarros_fumados_dia, anos_fumando, fator_conversor)
minutos_perdidos = calcular_tempo_perdido(cigarros_total_fumados, tempo_perdido_per_cigarro)
dias_perdidos = calcular_dias_perdidos(minutos_perdidos)

print(f"Fumando {cigarros_fumados_dia} cigarros por dia durante {anos_fumando} ano(s) você irá perder aproximadamente {dias_perdidos} dias de vida")