# Inserir 3 números e o programa dizer qual o maior e menor

num1 = int(input("Insira o 1o número: "))
num2 = int(input("Insira o 2o número: "))
num3 = int(input("Insira o 3o número: "))
num_maior = num1
num_menor = num1
if num2 > num_maior:
    num_maior = num2
if num3 > num_maior:
    num_maior = num3
if num2 < num_menor:
    num_menor = num2
if num3 < num_menor:
    num_menor = num3
print(f"Número maior: {num_maior}  &  Número menor: {num_menor}") 