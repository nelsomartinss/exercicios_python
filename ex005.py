'''
5) Faça um programa que leia as duas notas de um aluno em uma matéria e mostre
na tela a sua média na disciplina.
Ex:
Nota 1: 4.5
Nota 2: 8.5
A média entre 4.5 e 8.5 é igual a 6.5

'''

primeira_nota = input('Digite a primeira nota: ')
segunda_nota = input('Digite a segunda nota: ')

float_primeira_nota = float(primeira_nota)
float_segunda_nota = float(segunda_nota)
media = (float_primeira_nota + float_segunda_nota) / 2

print(f'Sua média é de: {media:.1f}')