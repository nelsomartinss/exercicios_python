'''
Faça um algoritmo que leia a idade de vários alunos de uma turma. O programa vai parar quando for digitada a idade 999. No final, mostre quantos alunos existem na turma e qual é a média de idade do grupo.
'''

total_alunos = 0
total_idades = 0

while True:
    idade = input('\nDigite a idade do aluno: ')

    try:
        idade = int(idade)
    
        if idade == 999:
            print('\nPrograma encerrado...\nAté a próxima!\n')
            break
        else:
            total_idades+=idade
            total_alunos+=1
    except:
        print('Digite apenas números inteiros para a idade!\n')
        continue

    nota = input('Digite a nota do aluno: ').replace(',', '.')

    try:
        nota = float(nota)      
    except:
        print('\nIdade ou nota possue valor inválido!\n')
        continue

    

media = f'{total_idades / total_alunos :.1f}'

print(f'Quantidade de alunos na turma: {total_alunos}')
print(f'A média de idade dos alunos é: {str(media).replace('.', ',')}\n')