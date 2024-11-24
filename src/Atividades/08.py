triangulo = int(input("Digite o tamanho do triangulo: "))
contador = 1

for i in range(1, triangulo + 1):
    print()
    for i in range(1, i + 1):
        print("*", end = '')
        contador += 1
    print()