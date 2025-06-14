''' 
Crie um programa que leia o preço de um produto, calcule e mostre o seu
PREÇO PROMOCIONAL, com 5% de desconto. 
'''

preco_produto = input('Digite o preço do produto: ')
float_preco_produto = float(preco_produto)

valor_promocional = float_preco_produto - ((5 / float_preco_produto) * 100)

print(f'Valor do produto R${float_preco_produto :.2f}')
print(f'Valor do produto com 5% de desconto: R${valor_promocional :.2f}')