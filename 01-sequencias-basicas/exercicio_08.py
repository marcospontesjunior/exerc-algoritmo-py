"""Desenvolva um programa que leia uma distância em metros e mostre os valores 
relativos em outras medidas. 
Ex:  
Digite uma distância em metros: 185.72 
A distância de 85.7m corresponde a: 
0.18572Km 
1.8572Hm 
18.572Dam 
1857.2dm 
18572.0cm 
185720.0mm"""

distancia = float(input("Digite uma distância em metros: "))

km = (distancia / 1000)
hm = (distancia / 100)
dam = (distancia / 10)
dm = (distancia * 10)
cm = (distancia * 100)
mm = (distancia * 1000)

print(f"A distância de {distancia} corresponde a:\n"
      f"{km} km | {dm} dm\n"
      f"{hm} hm  | {cm} cm\n"
      f"{dam} dam | {mm} mm")