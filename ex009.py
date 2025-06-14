'''
9) Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar.
'''

dinheiro_carteira = input('Digite quantos R$ você possui na carteira: ')
float_dinheiro_carteira = float(dinheiro_carteira)

dolar = 5.54
comprar_dolar = float_dinheiro_carteira / dolar

print(f'Com R${float_dinheiro_carteira :.2f} você pode comprar ${comprar_dolar :.2f}')