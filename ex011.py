'''
Desenvolva uma lógica que leia os valores de A, B e C de uma equação do
segundo grau e mostre o valor de Delta.
'''

a = input('Digite o valor de A: ')
float_a = float(a)

b = input('Digite o valor de B: ')
float_b = float(b)

c = input('Digite o valor de C: ')
float_c = float(c)

delta = float_b ** 2 - 4 * float_a * float_c

print(f'O valor de Δ (delta) é: {delta :.1f}')
