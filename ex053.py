'''
Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final:
a) Quantos homens foram cadastrados
b) Quantas mulheres foram cadastradas
c) A média de idade do grupo
d) A média de idade dos homens
e) Quantas mulheres tem mais de 20 anos
'''

i = 1
qtd_sexo_feminino = 0
qtd_sexo_masculino = 0

while i <= 5:
    sexo = input(F'\n[F] para FEMININO e [M] para MASCULINO\nDigite o sexo da {i}º pessoa: ').upper()

    if sexo == 'F':
        qtd_sexo_feminino+=1
    elif sexo == 'M':
        qtd_sexo_masculino+=1
    else:
        print('\nDigite apenas F ou M!')
        continue

    idade = input(f'Digite a idade dessa pessoa: ')
    
    try:
        idade = int(idade)
    except:
        print('Digite apenas valores númericos inteiros para idade.')
        continue

    i+=1
