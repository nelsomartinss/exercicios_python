'''
37) Uma empresa precisa reajustar o salário dos seus funcionários, dando um aumento de acordo com alguns fatores. Faça um programa que leia o salário atual, o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa. No final, mostre o seu novo salário, baseado na tabela a seguir:
- Mulheres
 - menos de 15 anos de empresa: +5%
 - de 15 até 20 anos de empresa: +12%
 - mais de 20 anos de empresa: +23%
- Homens
 - menos de 20 anos de empresa: +3%
 - de 20 até 30 anos de empresa: +13%
 - mais de 30 anos de empresa: +25%
'''

print(f"\n{'*'*10} AUMENTO SALARIAL {'*'*10}")
print('''
- Mulheres
 - menos de 15 anos de empresa: +5%
 - de 15 até 20 anos de empresa: +12%
 - mais de 20 anos de empresa: +23%
      
- Homens
 - menos de 20 anos de empresa: +3%
 - de 20 até 30 anos de empresa: +13%
 - mais de 30 anos de empresa: +25%
''')

# VALORES
porcentagem_mulher_menos_15 = 5
porcentagem_mulher_15_20 = 12
porcentagem_mulher_mais_20 = 23

porcentagem_homem_menos_20 = 3
porcentagem_homem_20_30 = 13
porcentagem_homem_mais_30 = 25

# ENTRADAS 
salario_atual = input('Digite seu salário atual: ')
genero = input('Digite [M] para masculino e [F] para feminino - Gênero: ').upper()
tempo_trabalho = input('Digite a quantidade de anos de trabalho: ')

# CONVERSOES
float_salario_atual = float(salario_atual)
float_tempo_trabalho = float(tempo_trabalho)

# VERIFICACOES INICIAIS
if float_salario_atual <= 0 or float_tempo_trabalho <= 0:
    print('\nO salário atual ou o ano não podem ser zero ou menor que zero')
    print('Tente novamente...\n')
    exit()

if genero != 'M' and genero != 'F':
    print('\nO campo de gênero só aceita [M] para masculino e [F] para feminino!')
    print('Tente novamente...\n')
    exit()

# CONDICOES
mulher_menos_15 = genero == 'F' and float_tempo_trabalho < 15
mulher_15_20 = genero == 'F' and float_tempo_trabalho >= 15 and float_tempo_trabalho <= 20
mulher_mais_20 = genero == 'F' and float_tempo_trabalho > 20

homem_menos_20 = genero == 'M' and float_tempo_trabalho < 20
homem_20_30 = genero = 'M' and float_tempo_trabalho >= 20 and float_tempo_trabalho <= 30
homem_mais_30 = genero = 'M' and float_tempo_trabalho > 30

# PROCESSAMENTO
if mulher_menos_15:
    porcentagem_aumento = porcentagem_mulher_menos_15
    aumento = float_salario_atual + (float_salario_atual * porcentagem_mulher_menos_15 / 100)
elif mulher_15_20:
    porcentagem_aumento = porcentagem_mulher_15_20
    aumento = float_salario_atual + (float_salario_atual * porcentagem_mulher_15_20 / 100)
elif mulher_mais_20:
    porcentagem_aumento = porcentagem_mulher_mais_20
    aumento = float_salario_atual + (float_salario_atual * porcentagem_mulher_mais_20 / 100)
elif homem_menos_20:
    porcentagem_aumento = porcentagem_homem_menos_20
    aumento = float_salario_atual + (float_salario_atual * porcentagem_homem_menos_20 / 100)
elif homem_20_30:
    porcentagem_aumento = porcentagem_homem_20_30
    aumento = float_salario_atual + (float_salario_atual * porcentagem_homem_20_30 / 100)
elif homem_mais_30:
    porcentagem_aumento = porcentagem_homem_mais_30
    aumento = float_salario_atual + (float_salario_atual * porcentagem_homem_mais_30 / 100)

# SAIDA
print(f"\nSalário atual: R${float_salario_atual :.2f}")
print(f"Anos de trabalho: {float_tempo_trabalho}")
print(f"Seu aumento é de +{porcentagem_aumento}%")
print(f'Salário Atualizado: R${aumento :.2f}\n')

