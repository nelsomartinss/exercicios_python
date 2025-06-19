'''
 [DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)
'''
print(f"\n{5*'*'} PEDRA, PAPEL E TESOURA {'*'*5}")
print("\nDigite:\n[1] - PEDRA\n[2] - PAPEL\n[3] - TESOURA\n")

# ENTRADA
jogada_um = input('JOGADOR 1: ')
jogada_dois = input('JOGADOR 2: ')

# CONVERSOES
int_jogada_um = int(jogada_um)
int_jogada_dois = int(jogada_dois)

lista_jogadas = [1, 2, 3]

if (int_jogada_um, int_jogada_dois) in lista_jogadas:
    # PROCESSAMENTO - RESULTADO JOGADA
    pedra_ganha_tesoura = (int_jogada_um == 1 and int_jogada_dois == 3) or (int_jogada_um == 3 and int_jogada_dois == 1)
    tesoura_ganha_papel = (int_jogada_um == 3 and int_jogada_dois == 2) or (int_jogada_um == 2 and int_jogada_dois == 3)
    papel_ganha_pedra = (int_jogada_um == 2 and int_jogada_dois == 1) or (int_jogada_um == 1 and int_jogada_dois == 2)
    empate = int_jogada_um == int_jogada_dois
else:
   print('\nJOGADA INVÁLIDA!\n')
   exit()

# SAIDA
if pedra_ganha_tesoura:
    print('\nPEDRA GANHA DE TESOURA\n')
elif papel_ganha_pedra:
    print('\nPAPEL GANHA DE PEDRA\n')
elif tesoura_ganha_papel:
    print('\nTESOURA GANHA DE PAPEL\n')
elif empate:
    print('\nEMPATE\n')