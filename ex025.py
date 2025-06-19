'''
[DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta.
Analise seus comprimentos e diga se é possível formar um triângulo com essas retas. Matematicamente, para três segmentos formarem um triângulo, o comprimento de cada lado deve ser menor que a soma dos outros dois.
'''

segmento_um = input('Digite o valor do primeiro segmento: ')
segmento_dois = input('Digite o valor do segundo segmento: ')
segmento_tres = input('Digite o valor do terceiro segmento: ')

float_segmento_um = float(segmento_um)
float_segmento_dois = float(segmento_dois)
float_segmento_tres = float(segmento_tres)

verificar_tamanho = (
   (float_segmento_um < (float_segmento_dois + float_segmento_tres)) 
and (float_segmento_dois < (float_segmento_um + float_segmento_tres)) 
and (float_segmento_tres < (float_segmento_um + float_segmento_dois))
)

triangulo = 'Δ'

if verificar_tamanho:
    print(f'Os segmentos formam: {triangulo}')
else:
    print('Os segmentos não formam um triângulo!')