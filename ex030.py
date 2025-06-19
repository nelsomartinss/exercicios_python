'''
30) [DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo
de triângulo será formado:
 - EQUILÁTERO: todos os lados iguais
 - ISÓSCELES: dois lados iguais
 - ESCALENO: todos os lados diferentes
'''

# ENTRADAS
segmento_um = input('Digite o valor do primeiro segmento: ')
segmento_dois = input('Digite o valor do segundo segmento: ')
segmento_tres = input('Digite o valor do terceiro segmento: ')

# CONVERSOES
float_segmento_um = float(segmento_um)
float_segmento_dois = float(segmento_dois)
float_segmento_tres = float(segmento_tres)

# VERIFICACAO / PROCESSAMENTO - FORMA TRIANGULO?
verificar_tamanho = (
   (float_segmento_um < (float_segmento_dois + float_segmento_tres)) 
and (float_segmento_dois < (float_segmento_um + float_segmento_tres)) 
and (float_segmento_tres < (float_segmento_um + float_segmento_dois))
)

if verificar_tamanho:
    print(f'Os segmentos formam um triângulo')
else:
    print('Os segmentos não formam um triângulo!')
    exit()

# LISTA PARA VERIFICACAO DE VALOR
segmentos = [float_segmento_um, float_segmento_dois, float_segmento_tres]    

# VERIFICAO / PROCESSAMENTO - TIPO DE TRIANGULO
if all(segs > 0 for segs in segmentos):
    equilatero = (
        float_segmento_um == float_segmento_dois == float_segmento_tres
        )
    isosceles = (
        float_segmento_um == float_segmento_dois != float_segmento_tres or
        float_segmento_dois == float_segmento_tres != float_segmento_um or 
        float_segmento_tres == float_segmento_um != float_segmento_dois
    )
    escaleno = (
        float_segmento_um != float_segmento_dois and
        float_segmento_dois != float_segmento_tres and
        float_segmento_tres != float_segmento_um
    )
else:
    print('Triângulo não pode ser criado!')
    exit()

# SAIDA
if equilatero:
    print('Todos os lados do triângulo são iguais - EQUILÁTERO')
elif isosceles:
    print('O triângulo possui dois lados iguais - ISÓSCELES')
elif escaleno:
    print('Todos os lados do triângulo são diferenres - ESCALENO')