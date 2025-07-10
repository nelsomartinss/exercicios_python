'''
Crie um programa que leia o sexo e a idade de várias pessoas. O programa vai
perguntar se o usuário quer continuar ou não a cada pessoa. No final, mostre:
a) qual é a maior idade lida
b) quantos homens foram cadastrados
c) qual é a idade da mulher mais jovem
d) qual é a média de idade entre os homens
'''

execucao = True
sexos_validos = 'fm'
somatorio_idades_homens = 0
numero_homens = 0
media_homens = 0.0
numero_mulheres = 0
maior = None
menorf = None

while execucao:
    while True:
        idade = input('\nDigite a sua idade: ')
        try:
            idade = int(idade)
            if maior is None or idade > maior:
                maior = idade

            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
                continue
            break  
        except ValueError:
            print("Erro: Digite um valor numérico inteiro.")


    while True:
        sexo = input('Digite o seu sexo (m/f): ').lower().replace(' ', '')
        if sexo in sexos_validos:
            if sexo == 'm':
                somatorio_idades_homens += idade
                numero_homens += 1
            elif sexo == 'f':
                numero_mulheres += 1
                if menorf is None or idade < menorf:
                    menorf = idade
            break 
        else:
            print('Por favor, digite um sexo válido!\n')

    while True:
        sair = input('\nDeseja sair? (s/n): ').lower().strip()
        if sair == 's':
            print('Encerrando...')
            execucao = False
            break
        elif sair == 'n':
            break
        else:
            print('Valor inválido! Digite apenas "s" ou "n".')
            continue

media_homens = str(f'{somatorio_idades_homens / numero_homens :.1f}').replace('.', ',')

print(f'\nVocê cadastrou {numero_homens} homens e {numero_mulheres} mulheres.')
print(f'A maior idade cadastrada foi {maior}.')

if menorf != None:
    print(f'A mulher mais jovem possui {menorf} anos de idade.')
else:
    print('Você não cadastrou mulheres')

print(f'A média das idades dos homens é {media_homens}\n')