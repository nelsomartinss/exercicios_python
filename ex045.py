'''
O programa acima vai ter um problema quando digitarmos o primeiro valor
maior que o último. Resolva esse problema com um código que funcione em qualquer situação.
'''

valor_inicial = input('Digite o valor inicial da contagem: ')
valor_final = input('Digite o valor final da contagem: ')
incremento = input('Digite o incremento: ')

verificando_numeros_inteiros = valor_inicial.isdigit() and valor_final.isdigit() and incremento.isdigit()

if verificando_numeros_inteiros:
    inicio = int(valor_inicial)
    final = int(valor_final)
    int_incremento = int(incremento)
    contador = inicio
else:
    print('Digite apenas números inteiros!')
    exit()

print('Contagem:', end=' ')

if contador < final:
    while contador <= final:
        print(f'{contador}', end=' ')
        contador+=int_incremento
else:
    while contador >= final:
        print(f'{contador}', end=' ')
        contador-=int_incremento

print('Acabou!')