'''
34) O Índice de Massa Corpórea (IMC) é um valor calculado baseado na altura e no peso de uma pessoa. De acordo com o valor do IMC, podemos classificar o indivíduo dentro de certas faixas.
 - abaixo de 18.5: Abaixo do peso
 - entre 18.5 e 25: Peso ideal
 - entre 25 e 30: Sobrepeso
 - entre 30 e 40: Obesidade
 - acima de 40: Obseidade 0
Obs: O IMC é calculado pela expressão peso/altura² (peso dividido pelo quadrado da altura)
'''

print(f"\n{'*'*10} IMC {'*'*10}\n")
print('''TABELA:
- abaixo de 18.5: Abaixo do peso
- entre 18.5 e 25: Peso ideal
- entre 25 e 30: Sobrepeso
- entre 30 e 40: Obesidade
- acima de 40: Obesidade mórbida          
\n''')

# ENTRADAS
peso = input('Digite seu peso: ')
altura = input('Digite sua altura: ')

# CONVERSOES
float_peso = float(peso)
float_altura = float(altura)

# VERIFICANDO INPUTS
if float_peso <= 0 or float_altura <= 0:
    print('\nPeso ou altura inválidos!\n')
    exit()

# PROCESSAMENTO - IMC
imc = float_peso / (float_altura ** 2)

# PROCESSAMENTO - VERIFICANDO IMC
abaixo_peso = imc < 18.5
peso_ideal = imc >= 18.5 and imc <= 25
sobrepeso = imc > 25 and imc <= 30
obesidade = imc > 30 and imc <= 40
obesidade_morbida = imc > 40

# SAIDA
if abaixo_peso:
    print(f'\nIMC: {imc :.2f} - ABAIXO DO PESO\n')
elif peso_ideal:
    print(f'\nIMC: {imc :.2f} - PESO IDEAL\n')
elif sobrepeso:
    print(f'\nIMC: {imc :.2f} - SOBREPESO\n')
elif obesidade:
    print(f'\nIMC: {imc :.2f} - OBESIDADE\n')
elif obesidade_morbida:
    print(f'\nIMC: {imc :.2f} - OBESIDADE MORBIDA\n')
