'''
23) Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos
para todos, mas especialmente para mulheres. Faça um programa que leia nome,
sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo
que:
 - Homens ganham 5% de desconto
 - Mulheres ganham 13% de desconto
'''

nome = input('Digite seu nome: ')
sexo = input('Digite [M] para o sexo masculino ou [F] para o feminino: ').upper()
valor_compras = input('Digite o valor total das suas compras: ')
float_valor_compras = float(valor_compras)

if sexo == 'M' or sexo == 'F':
    if sexo == 'F':
        valor_desconto = float_valor_compras - (float_valor_compras * 13 / 100)

        print('Feliz dia da mulher!')
        print(f'Valor total R${float_valor_compras :.2f}')
        print(f'Valor com 13% de desconto R${valor_desconto}')
    elif sexo == 'M':
        valor_desconto = float_valor_compras - (float_valor_compras * 5 / 100)
        print(f'Valor total R${float_valor_compras :.2f}')
        print(f'Valor com 5% de desconto R${valor_desconto}')
else:
    print('Sexo inválido!')

