'''
Desenvolva um algoritmo que leia o nome, a idade e o sexo de várias pessoas.
O programa vai perguntar se o usuário quer ou não continuar. No final, mostre:
a) O nome da pessoa mais velha
b) O nome da mulher mais jovem
c) A média de idade do grupo
d) Quantos homens tem mais de 30 anos
e) Quantas mulheres tem menos de 18 anos
'''

verificacao = True
mais_velho = None
mais_novo = None

while verificacao:
    nome = input('\nDigite seu nome: ')
    
    while True:
        idade = input('Digite sua idade: ')
        try:
            idade = int(idade)
        except ValueError:

    

    sexo = input('Digite seu sexo: ')
    