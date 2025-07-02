'''
Desenvolva um aplicativo que mostre na tela o resultado da expressão 500 +
450 + 400 + 350 + 300 + ... + 50 + 
'''

contador = 500
somatorio = 0

while contador >= 0:
    somatorio+=contador
    contador-=50

print(f'A soma total é {somatorio}')