'''
24) Faça um algoritmo que pergunte a distância que um passageiro deseja
percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para
viagens até 200Km e R$0.45 para viagens mais longas.
'''

distancia_desejada = input("Digite a distância de km que deseja percorrer: ")

float_distancia_desejada = float(distancia_desejada)
verificar_distancia = float_distancia_desejada <= 200

if verificar_distancia:
    preco_passagem = float_distancia_desejada * 0.50
    print(f'Viagem de {float_distancia_desejada :.2f}Km')
    print(f'Total a pagar R${preco_passagem :.2f}')
else:
    preco_passagem = float_distancia_desejada * 0.45
    print(f'Viagem de {float_distancia_desejada :.2f}Km')
    print(f'Total a pagar R${preco_passagem :.2f}')