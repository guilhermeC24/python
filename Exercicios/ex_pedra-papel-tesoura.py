# Exercicio Pedra-Papel-Tesouro
'''
Pedra > Tesoura
Papel > Pedra
Tesoura > Papel

'''

j1 = 0
j2 = 0
saida=True

while saida==True:
    print("\n Jogador 1")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    print("4 - Sair")
    j1 = int(input("Insira a sua jogada: "))

    print("Jogador 2")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    print("4 - Sair")
    j2 = int(input("Insira a sua jogada: "))


    match j1:
        case 1:
            if j2 == 1:
                print("Os 2 jogadores empataram com Pedra - Pedra")
            elif j2 == 2:
                print("O jogador 2 ganhou com Papel > Pedra")
            elif j2 == 3:
                print("O jogador 1 ganhou com Pedra > Tesoura")

        case 2:
            if j2 == 1:
                print("O jogador 1 ganhou com Papel > Pedra")
            elif j2 == 2:
                print("Os 2 jogadores empataram com Papel - Papel")
            elif j2 == 3:
                print("O jogador 2 ganhou com Tesoura > Papel")


        case 3:
            if j2 == 1:
                print("O jogador 2 ganhou com Pedra > Tesoura")
            elif j2 == 2:
                print("O jogador 1 ganhou com Tesoura > Papel")
            elif j2 == 3:
                print("Os 2 jogadores empataram com Tesoura - Tesoura")

        case 4:
            saida = False
            print("A sair...")