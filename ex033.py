'''
33) Escreva um programa para aprovar ou não o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''

# ENTRADAS0
valor_casa = input('Digite o valor da casa: ')
salario_comprador = input('Digite o salário do comprador: ')
anos_pagando = input('Digite em quantos anos pretente pagar: ')

# CONVERSOES
float_valor_casa = float(valor_casa)
float_salario_comprador = float(salario_comprador)
int_anos_pagando = int(anos_pagando)

# PROCESSAMENTO
meses_pagando = int_anos_pagando * 12
prestacao_casa = float_valor_casa / meses_pagando
salario_30 = float_salario_comprador * 30 /100

# PROCESSAMENTO - VERIFICACOES
emprestimo_aprovado = prestacao_casa <= salario_30

# SAIDA
if emprestimo_aprovado:
    print('✅ Empréstimo Aprovado!')
    print(f'Valor da prestação: RS{prestacao_casa :.2f}')
else:
    print('❌ Empréstimo Reprovado!')
    print(f'O valor da prestação excede 30% do seu salário')
