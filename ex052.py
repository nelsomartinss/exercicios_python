'''
Crie um algoritmo que leia a idade de 10 pessoas, mostrando no final:
a) Qual é a média de idade do grupo
b) Quantas pessoas tem mais de 18 anos
c) Quantas pessoas tem menos de 5 anos
d) Qual foi a maior idade lida
'''

i = 1
soma = 0
media = 0
pessoas_maiores_18 = 0
pessoas_menores_5 = 0
maior = None
menor = None

while i <= 10:
    idade_pessoas = input(f'Digite a idade da {i}º pessoa: ')
    try:
        idade_pessoas = int(idade_pessoas)
    except:
        print('Digite valores númericos inteiros.\n')
        continue

    if idade_pessoas > 18:
        pessoas_maiores_18+=1
    if idade_pessoas < 5:
        pessoas_menores_5+=1
    
    # testando outra forma de resolver...
    if maior is None or idade_pessoas > maior:
        maior = idade_pessoas
    if menor is None or idade_pessoas < menor:
        menor = idade_pessoas

    i+=1
    soma+=idade_pessoas

media = soma / 10
print(f'\nMédia da idade das pessoas: {media :.1f}')
print(f'A maior idade digitada foi: {maior}')
print(f'A menor idade digitada foi: {menor}\n')