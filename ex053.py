'''
Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final:
a) Quantos homens foram cadastrados
b) Quantas mulheres foram cadastradas
c) A média de idade do grupo
d) A média de idade dos homens
e) Quantas mulheres tem mais de 20 anos
'''

i = 1
qtd_sexo_feminino = 0
qtd_sexo_masculino = 0
soma_idades = 0
soma_idade_homens = 0
qtd_mulheres_mais_20 = 0

while i <= 5:
    idade = input(f'\nDigite a idade da {i}º pessoa: ')
    
    try:
        idade = int(idade)
    except:
        print('Digite apenas valores númericos inteiros para idade.')
        continue

    sexo = input(F'\n[F] para FEMININO e [M] para MASCULINO\nDigite o sexo dessa pessoa: ').upper()

    if sexo == 'F':
        qtd_sexo_feminino+=1
        if idade > 20:
            qtd_mulheres_mais_20+=1
    elif sexo == 'M':
        qtd_sexo_masculino+=1
        soma_idade_homens+=idade
    else:
        print('\nDigite apenas F ou M!')
        continue
    
    soma_idades+=idade
    i+=1

media_idades = soma_idades / 5
media_idades_homens =  soma_idade_homens / qtd_sexo_masculino

print(f"\nQuantidade de homens cadastrados: {qtd_sexo_masculino}")
print(f"Quantidade de mulheres cadastradas: {qtd_sexo_feminino}")
print(f"A média das idades digitadas é: {media_idades}")
print(f"A média de idade dos homens é: {media_idades_homens}")
print(f"A quantidade de mulheres maiores de 20 anos: {qtd_mulheres_mais_20}\n")
    
