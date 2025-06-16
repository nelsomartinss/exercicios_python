'''
Crie um programa que leia o número de dias trabalhados em um mês e mostre o salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25 por hora trabalhada.
'''

dias_trabalhados = input('Digite a quantidade dias trabalhadas no mês: ')
int_dias_trabalhados = int(dias_trabalhados)

valor_dia_trabalho = 8 * 25
salario = int_dias_trabalhados * valor_dia_trabalho

print(f'Você trabalhou {int_dias_trabalhados} dias por 8h, sua hora vale R$25,00')
print(f'Seu salário é de R${salario :.2f}')