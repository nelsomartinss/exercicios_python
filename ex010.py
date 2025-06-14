''' 
10) Faça um algoritmo que leia a largura e altura de uma parede, calcule e
mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2metros quadrados. 
'''

largura = input('Digite a largura da parede: ')
float_largura = float(largura)

altura = input('Digite a altura da parede: ')
float_altura = float(altura)

area = float_largura * float_altura

rendimento_lata = 2
quantidade_tinta = area / rendimento_lata

print(f'Sua parede tem {area:.1f}m² de área.')
print(f'Serão necessários {quantidade_tinta :.1f} litros de tinta para pintá-la.')