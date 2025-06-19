'''
29) Desenvolva um programa que leia o nome de um funcionário, seu salário,
quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de
acordo com a tabela a seguir:
 - Até 3 anos de empresa: aumento de 3%
 - entre 3 e 10 anos: aumento de 12.5%
 - 10 anos ou mais: aumento de 20%
'''

nome = input('Digite o seu nome: ')
salario = input('Digite o seu salário: ')
anos_trabalho = input('Digite a quantidade de anos de trabalho: ')

float_salario = float(salario)
int_anos_trabalho = int(anos_trabalho)

tres_anos = int_anos_trabalho >= 1 and int_anos_trabalho <= 3
tres_a_dez_anos = int_anos_trabalho > 3 and int_anos_trabalho <= 10
acima_dez_anos = int_anos_trabalho > 10

if tres_anos:
    aumento = float_salario + float_salario * 3 / 100
    print('Aumento de 3%')
    print(f'Salário Reajustado: R${aumento :.2f}')
elif tres_a_dez_anos:
    aumento = float_salario + float_salario * 12.5 / 100
    print('Aumento de 12.5%')
    print(f'Salário Reajustado: R${aumento :.2f}')
elif acima_dez_anos:
    aumento = float_salario + float_salario * 20 / 100
    print('Aumento de 20%')
    print(f'Salário Reajustado: R${aumento :.2f}')