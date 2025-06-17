'''
19) Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua média e mostre na tela. No final, analise a média e mostre se o aluno teve ou não um bom aproveitamento (se ficou acima da média 7.0).
'''

primeira_nota = input('Digite sua primeira nota: ')
segunda_nota = input('Digite sua segunda nota: ')

float_primeira_nota = float(primeira_nota)
float_segunda_nota = float(segunda_nota)
media = (float_primeira_nota + float_segunda_nota) / 2

print(f'Primeira nota: {float_primeira_nota :.1f}')
print(f'Segunda nota: {float_segunda_nota :.1f}')
print(f'Média: {media :.1f}')

if media >= 7:
    print('Você foi aprovado!')
else:
    print('Você foi reprovado!')