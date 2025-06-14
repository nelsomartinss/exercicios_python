'''
8) Desenvolva um programa que leia uma distância em metros e mostre os valores
relativos em outras medidas.
Ex:
Digite uma distância em metros: 185.72
A distância de 185.72m corresponde a:
0.18572Km
1.8572Hm
18.572Dam
1857.2dm
18572.0cm
185720.0mm
'''

distancia_metros = input('Digite uma distância em metros: ')
float_distancia_metros = float(distancia_metros)

conversor_km = float_distancia_metros / 1000
conversor_hm = float_distancia_metros / 100
conversor_dam = float_distancia_metros / 10

conversor_dm = float_distancia_metros * 10
conversor_cm = float_distancia_metros * 100
conversor_mm = float_distancia_metros * 1000

print(f'A distância de {float_distancia_metros:.2f}m corresponde a:')
print(f'{conversor_km}Km')
print(f'{conversor_hm}Hm')
print(f'{conversor_dam}Dam')
print(f'{conversor_dm}dm')
print(f'{conversor_cm}cm')
print(f'{conversor_mm}mm')