'''
Desenvolva um aplicativo que leia o peso e a altura de 7 pessoas, mostrando
no final:
a) Qual foi a média de altura do grupo
b) Quantas pessoas pesam mais de 90Kg
c) Quantas pessoas que pesam menos de 50Kg tem menos de 1.60m
d) Quantas pessoas que medem mais de 1.90m pesam mais de 100Kg.
'''

i = 1
soma_alturas = 0
soma_acima_90 = 0
soma_pessoas_menos_50_menor_160cm = 0
soma_pessoas_mais_100_maior_190cm = 0
media_altura = 0

print('')
while i <= 7:
    peso = input(f'Digite o peso da {i}° pessoa: ')

    try:
        peso = float(peso)
        if peso > 90:
            soma_acima_90+=1
    except ValueError:
        print('Digite apenas valores númericos...')
        continue

    altura = input(f'Digite a altura da {i}° pessoa: ')

    try:
        altura = float(peso)
        soma_alturas+=altura
    except ValueError:
        print('Digite apenas valores númericos...')
        continue

    if peso < 50 and altura < 1.60:
        soma_pessoas_menos_50_menor_160cm+=1

    if peso > 100 and altura > 1.90:
        soma_pessoas_mais_100_maior_190cm+=1

    media_altura = soma_alturas / i
    i+=1

print(f'\nA média de altura do grupo: {media_altura :.2f}')
print(f'Número de pessoas que pesam mais de 90kg: {soma_acima_90 :.0f}')
print(f'Número de pessoas que pesam menos de 50Kg tem menos de 1.60m: {soma_pessoas_menos_50_menor_160cm :.0f}')
print(f'Número de pessoas que medem mais de 1.90m pesam mais de 100Kg: {soma_pessoas_mais_100_maior_190cm :.0f}\n')