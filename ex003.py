''' 
3) Crie um programa que leia o nome e o salário de um funcionário, mostrando no
final uma mensagem.
Ex:
Nome do Funcionário: Maria do Carmo
Salário: 1850,45
O funcionário Maria do Carmo tem um salário de R$1850,45 em Junho. 
'''

nome = input('Digite o seu nome: ')
salario = input('Digite o seu salário: ')

salario_float = float(salario)

print(f'Nome do funcionário: {nome}')
print(f'Salário: {salario_float}')
print(f'O funcionário {nome} tem um salário de R${salario_float:.2f} em Junho.')