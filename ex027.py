'''
27) Crie um programa que leia duas notas de um aluno e calcule a sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
 - Média até 4.9: REPROVADO
 - Média entre 5.0 e 6.9: RECUPERAÇÃO
 - Média 7.0 ou superior: A
'''

# ENTRADAS
primeira_nota = input('Digite sua primeira nota: ')
segunda_nota = input('Digite sua segunda nota: ')

# CONVERSOES
float_primeira_nota = float(primeira_nota)
float_segunda_nota = float(segunda_nota)

# PROCESSAMENTO
media = (float_primeira_nota + float_segunda_nota) / 2

# PROCESSAMENTO / VERIFICACAO
reprovado = media <= 4.9 and media >= 0
recuperacao = media >= 5.0 and media <= 6.9
aprovado = media >= 7.0 and media <= 10
nota_invalida = media > 10 or media < 0

# SAIDA
if reprovado:
    print(f'Média: {media} - REPROVADO')
elif recuperacao:
    print(f'Média: {media} - RECUPERAÇÃO')
elif aprovado:
    print(f'Média: {media} - APROVADO')
elif nota_invalida:
    print(f'Notas inválidas! - TENTE NOVAMENTE')

