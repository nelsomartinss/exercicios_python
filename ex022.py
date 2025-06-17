'''
22) Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua
situação em relação ao alistamento militar.
 - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o
alistamento.
 - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do
alistamento.
'''

idade = input('Digite a sua idade: ')
int_idade = int(idade)

if int_idade < 18:
    faltam_anos = 18 - int_idade
    print(f'Você deve se alistar em {faltam_anos} anos!')
else:
    if int_idade == 18:
        print('Você já pode e deve se alistar!')
    else:
        passam_anos = int_idade - 18
        print(f'Se não se alistou, você deveria ter se alistado a {passam_anos} anos')