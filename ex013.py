'''
Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o
seu novo salário, com 15% de aumento.
'''

salario_funcionario = input('Digite o seu salário R$')
float_salario_funcionario = float(salario_funcionario)

aumento = float_salario_funcionario + (float_salario_funcionario * 15 / 100)

print(f'Salário do funcionário R${float_salario_funcionario :.2f}')
print(f'Salário com aumento de 15%: R${aumento :.2f}')