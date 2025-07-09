'''
Desenvolva um aplicativo que leia o salário e o sexo de vários funcionários. No final, mostre o total de salários pagos aos homens e o total pago às mulheres. O programa vai perguntar ao usuário se ele quer continuar ou não sempre que ler os dados de um funcionário.
'''

total_mulheres = 0
total_homens = 0

while True:
    salario = input('\nDigite o salário do funcionário: ')

    try:
        salario = float(salario)
    except:
        print('\nAlgo deu errado!\nDigite um valor númerico!\n')    

    lista_sexo = 'fm'
    sexo = input('\n[F] - FEMININO\n[M] - MASCULINO\nDigite o sexo do funcionário: ').lower()

    if sexo in lista_sexo:
        if sexo == 'f':
            total_mulheres+=salario
        elif sexo == 'm':
            total_homens+=salario
    else:
        print('\nPor favor digite um sexo válido!\n')
        continue

    continuar_sair = input('\nDeseja continuar s/n?\n').lower()
    if continuar_sair == 's':
        continue
    elif continuar_sair == 'n':
        break
    else:
        print('\nResposta inválida!\nContinunando...\n')

print(f'\nTotal do salário pago as mulheres: R${total_mulheres :.2f}')
print(f'Total do salário pago aos homens: R${total_homens :.2f}\n')
print('\nAté a próxima!\n')