'''
36) Um programa de vida saudável quer dar pontos atividades físicas que podem
ser trocados por dinheiro. O sistema funciona assim:
 - Cada hora de atividade física no mês vale pontos
 - até 10h de atividade no mês: ganha 2 pontos por hora
 - de 10h até 20h de atividade no mês: ganha 5 pontos por hora
 - acima de 20h de atividade no mês: ganha 10 pontos por hora
 - A cada ponto ganho, o cliente fatura R$0,05 (5 centavos)

Faça um programa que leia quantas horas de atividade uma pessoa teve por mês, calcule e mostre quantos pontos ela teve e quanto dinheiro ela conseguiu ganhar.
'''

# ENTRADAS
horas = input('Digite quantas horas de atividade física que você realizou no último mês: ')

# CONVERSOES
float_horas = float(horas)

# VALORES
pontos_ate_dez =  2
pontos_dez_a_vinte = 5
pontos_acima_vinte = 10
valor_ponto = 0.05

# VERIFICACOES
dez_horas = float_horas > 0 and float_horas < 10
dez_a_vinte_horas = float_horas >= 10 and float_horas <= 20
acima_vinte_horas = float_horas > 20

# PROCESSAMENTO
if dez_horas:
    total_pontos = float_horas * pontos_ate_dez
    valor_faturado = total_pontos * valor_ponto
elif dez_a_vinte_horas:
    total_pontos = float_horas * pontos_dez_a_vinte
    valor_faturado = total_pontos * valor_ponto
elif acima_vinte_horas:
    total_pontos = float_horas * pontos_acima_vinte
    valor_faturado = total_pontos * valor_ponto
else:
    print('Você não pontuou')
    exit()

# SAIDA
print(f'Você fez {float_horas}h de atividades físicas!')
print(f'Isso da uma total de {total_pontos} pontos')
print(f'Valor faturado: R${valor_faturado :.2f}')