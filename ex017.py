'''
17) Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.
'''

velocidade_carro = input('Digite a velocidade do carro: ')
float_velocidade_carro = float(velocidade_carro)

velocidade_maxima = 80

if float_velocidade_carro > velocidade_maxima:
    kms_acima_velocidade = float_velocidade_carro - velocidade_maxima
    valor_multa = kms_acima_velocidade * 5

    print(f'Você excedeu o limite de velocidade em {kms_acima_velocidade :.1f}km/h')
    print(f'Valor da multa RS{valor_multa}')
else:
    print('Você não excedeu o limite de 80km/h')
    print('Boa viagem!')