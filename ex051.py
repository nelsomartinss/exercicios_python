'''
Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela qual foi o maior e qual foi o menor preço digitados.
'''

i= 1
maior_valor = None
menor_valor = None
lista_produtos = []

while i <= 8:
    preco_produto = input(f'Digite o valor do {i}° produto: R$')

    try:
        float_preco = float(preco_produto)
    except ValueError:
        print('Digite apenas números!')
        continue
    
    lista_produtos.append(float_preco)
    maior_valor = max(lista_produtos)
    menor_valor = min(lista_produtos)

    '''
    if maior_valor is None or float_preco > maior_valor
        maior_valor = float_preco

    if menor_valor is None or float_preco < menor_valor
        menor_valor = float_preco
    '''

    i+=1

print(f'\nO maior valor digitado: R${maior_valor :.2f}')
print(f'O menor valor digitado: R${menor_valor :.2f}\n')