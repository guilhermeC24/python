OPC = 0
saida=True

while saida==True:
    print("1 - Bom dia")
    print("2 - Boa tarde")
    print("3 - Boa noite")
    print("4 - Sair")
    OPC = int(input("Insira a opção que deseja: "))

    match OPC:
        case 1:
            print("Bom dia")
        case 2:
            print("Boa tarde")
        case 3:
            print("Boa noite")
        case 4:
            saida = False
            print("A sair...")