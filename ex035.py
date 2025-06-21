'''
35) Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O
aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para carro de luxo. Além disso, o cliente paga por Km percorrido. Faça um programa que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a
tabela a seguir:
 - Carros populares (aluguel de R$90 por dia)
 - Até 100Km percorridos: R$0,20 por Km
 - Acima de 100Km percorridos: R$0,10 por Km
 - Carros de luxo (aluguel de R$150 por dia)
 - Até 200Km percorridos: R$0,30 por Km
 - Acima de 200Km percorridos: R$0,25 por Km
'''

print(f"\n{'*'*10} ALUGUEL DE CARROS {'*'*10}\n")
print(f'''MENU
[1] - CARRO POPULAR
[2] - CARRO DE LUXO 
''')

# CARRO POPULAR
valor_carro_popular = 90
valor_carro_popular_100km = 0.20
valor_carro_popular_acima_100km = 0.10
# CARRO DE LUXO
valor_carro_luxo = 150
valor_carro_luxo_200km = 0.30
valor_carro_luxo_acima_200km = 0.25

# ENTRADAS
tipo_carro = input('Digite o número correspondente ao tipo de carro foi alugado: ')
qtd_dias_alugado = input('Digite o número de dias que ficou com o carro: ')
km_percorrido = input('Digite quantos KM foram percorridos: ')

# CONVERSOES
int_tipo_carro = int(tipo_carro)
int_qtd_dias_alugado = int(qtd_dias_alugado)
float_km_percorrido = float(km_percorrido)

# VERIFICANDO ENTRADA
verificando_entrada = int_tipo_carro <= 0 or int_qtd_dias_alugado <= 0
if verificando_entrada:
    print('O tipo de carro ou a quantidade de dias alugado são inválidos!')
    exit()

# PROCESSAMENTO - VERIFICACOES
# CARRO POPULAR
carro_popular = int_tipo_carro == 1
carro_popular_100km = float_km_percorrido <= 100
# CARRO LUXO
carro_luxo = int_tipo_carro == 2
carro_luxo_200km = float_km_percorrido <= 200

# PROCESSAMENTO E SAIDA
if carro_popular:
    print('\nTipo de carro: POPULAR')
    print(f'Valor da diária: R${valor_carro_popular :.2f}')
    if carro_popular_100km:
        valor_total_dias = valor_carro_popular * int_qtd_dias_alugado
        valor_total_km = float_km_percorrido * valor_carro_popular_100km
        valor_total = valor_total_dias + valor_total_km
        print(f'Quantidade de KM percorrido: {float_km_percorrido :.1f}')
        print(f'Valor total: R${valor_total :.2f}\n')
    else:
        valor_total_dias = valor_carro_popular * int_qtd_dias_alugado
        valor_total_km = float_km_percorrido * valor_carro_popular_acima_100km
        valor_total = valor_total_dias + valor_total_km
        print(f'Quantidade de KM percorrido: {float_km_percorrido :.1f}')
        print(f'Valor total: R${valor_total :.2f}\n')

elif carro_luxo:
    print('\nTipo de carro: LUXO')
    print(f'Valor da diária: R${valor_carro_luxo :.2f}')
    if carro_luxo_200km:
        valor_total_dias = valor_carro_luxo * int_qtd_dias_alugado
        valor_total_km = float_km_percorrido * valor_carro_luxo_200km
        valor_total = valor_total_dias + valor_total_km
        print(f'Quantidade de KM percorrido: {float_km_percorrido :.1f}')
        print(f'Valor total: R${valor_total :.2f}\n')
    else:
        valor_total_dias = valor_carro_luxo * int_qtd_dias_alugado
        valor_total_km = float_km_percorrido * valor_carro_luxo_acima_200km
        valor_total = valor_total_dias + valor_total_km
        print(f'Quantidade de KM percorrido: {float_km_percorrido :.1f}')
        print(f'Valor total: R${valor_total :.2f}\n')