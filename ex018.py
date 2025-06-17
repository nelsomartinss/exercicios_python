'''
18) Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade dela e depois mostre se ela pode ou não votar.
'''

idade = input('Digite a sua idade: ')
int_idade = int(idade)

if int_idade >= 16:
    print('Você pode votar!')
else:
    print('Você não pode votar!')