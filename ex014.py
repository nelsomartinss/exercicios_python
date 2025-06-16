'''
A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva
um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar,
sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.
'''

quantidade_km = input('Digite a quantidade de Km que foi percorrido: ')
quantidade_dias = input('Digite a quantidade de dias você ficou com o carro: ')

float_quantidade_km = float(quantidade_km)
int_quantidade_dias = int(quantidade_dias)

valor_total_km = float_quantidade_km * 0.20
valor_total_dias = int_quantidade_dias * 90
valor_total = valor_total_km + valor_total_dias

print(f'Você ficou {int_quantidade_dias} dias com o carro, total R${valor_total_dias :.2f}')
print(f"Você percorreu {float_quantidade_km :.1f}Km, total R${valor_total_km :.2f}")
print(f'O valor total é de R${valor_total :.2f}')