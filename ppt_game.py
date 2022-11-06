import random as rd

opcao = -1
menu_set = (9,1,2,3)
player_1 = -1
player_pc = -1
flag = 0

def menu():
    print("Jogo Pedra Tesoura Papel")
    print("1-Pedra")
    print("2-Tesoura")
    print("3-Papel")
    print("9-Fim de Jogo")
def resultado(jogador:int, maquina:int):
    tabela_resultado= {(1,1): 'Empate',
                   (1,2): 'Vitória',
                   (1,3): 'Derrota',
                   (2,1): 'Derrota',
                   (2,2): 'Empate',
                   (2,3): 'Vitória',
                   (3,1): 'Vitória',
                   (3,2): 'Derrota',
                   (3,3): 'Empate'}
    return tabela_resultado.get((jogador, maquina))

while opcao != 9:
    player_pc = rd.randint(1,3)
    menu()
    flag = 0
    while flag == 0:
        opcao = int(input("Digite sua Jogada: "))
        if menu_set.__contains__(opcao):
            flag = 1
    print("   ")
    print(resultado(opcao, player_pc))