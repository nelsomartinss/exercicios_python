'''
[DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule quantos dias de vida um fumante perderá e exiba o total em dias.
'''

# Entradas
quantidade_cigarros_dia = input('Quantos cigarros você fuma por dia?\n')
int_quantidade_cigarros_dia = int(quantidade_cigarros_dia)
quantidade_de_anos_fumando = input('A quantos anos você fuma?\n')
int_quantidade_de_anos_fumando = int(quantidade_de_anos_fumando)

# Processamento
quantidade_cigarros_fumados_vida = int_quantidade_de_anos_fumando * int_quantidade_cigarros_dia 
tempo_perdido_por_cigarro = quantidade_cigarros_fumados_vida * 10
total_dias_perdidos = (tempo_perdido_por_cigarro / 60) / 24

# Saída
print(f'Você fumou {int_quantidade_cigarros_dia} cigarros por dia durante {quantidade_de_anos_fumando} anos!')
print(f'Você perdeu o equivalente a {total_dias_perdidos :.1f} dia(s) de vida!')