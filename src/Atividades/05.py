while True:
    
    num = int(input("Informe um número para exibir na tabuada [0 p/ sair] : "))
    
    if num == 0:
        break
    cont = 0
    while cont < 10:
        cont += 1
        print(f"{num} x {cont:2} = {num * cont:3}")
print("Programa encerrado, volte sempre!")                                          