'''
28) Faça um programa que leia a largura e o comprimento de um terreno
retangular, calculando e mostrando a sua área em m². O programa também
devemostrar a classificação desse terreno, de acordo com a lista abaixo:
 - Abaixo de 100m² = TERRENO POPULAR
 - Entre 100m² e 500m² = TERRENO MASTER
 - Acima de 500m² = TERRENO VIP
'''

largura = input('Digite a largura do terreno: ')
comprimento = input('Digite o comprimento do terreno: ')

float_largura = float(largura)
float_comprimento = float(comprimento)

area = float_comprimento * float_largura

if area > 0:
    terreno_popular = area < 100 and area > 0
    terreno_master = area >= 100 and area <= 500
    terreno_vip = area > 500
else:
    print('Área inválida!')
    exit()

if terreno_popular:
    print(f'Área {area :.2f}')
    print(f'Terreno Popular')
elif terreno_master:
    print(f'Área {area :.2f}')
    print(f'Terreno Master')
elif terreno_vip:
    print(f'Área {area :.2f}')
    print(f'Terreno Vip')