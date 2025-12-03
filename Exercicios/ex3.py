
num = int(input("Insira um número: "))

match (num>0, num==0, num<0):
        case (False, True, False):
            print("O número é 0")
        case(False, False, True):
            print("O número é negativo.")
        case(True, False, False):

                if num % 2 == 0:
                    print("O número é positivo e par.")
                else:
                    print("O número é positivo e impar.")
                if num % 3 == 0 and num % 5 == 0:
                    print("O número é divisivel por 3 e por 5.")
                else:
                    print("Outros números positivos.")
