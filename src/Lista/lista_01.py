# Listas, arrays

lista_vazia = []
print(f"Lista vazia: {lista_vazia}")
print(f"Tipo da lista: {type(lista_vazia)}")

lista_inteira = [1, 4, 6, 7, 8, 3]
print(f"Valores contador na lista: {lista_inteira}")

lista_tipos_diferentes = ['Brasil', 5, 'Titulos']
print(f"{lista_tipos_diferentes}")


# 


nome = "Márcio Caliso"
inteiro = 100
flutuante = 3.14
booleano = True

lista_varios_tipos = [nome, inteiro, flutuante, booleano]

print(f"{lista_varios_tipos}")


# 


lista_funcao = [10, 20, 30, 40, 50]

def lista(lista_funcao):
    print(f"Os valores são: {lista_funcao}")
    
lista_funcao()


# 


var1 = int(input("Informe um valor: "))
var2 = input("Informe um valor: ")
var3 = float(input("Informe um valor: "))
var4 = bool(input("Informe um valor: "))

lista_1 = [var1, var2, var3, var4]

lista_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista_2.reverse()
print("Lista reversa: ", lista_2)

lista_2.sort()
print("Lista em ordem crescente: ", lista_2)

print("Maior valor: ", max(lista_2))
print("Menor valor: ", min(lista_2))

def exibirLista(lst):
    
    print(f"Exibindo lista: {lst}")
    
exibirLista(lista_2)


#


cursos = ["ADS", "Engenharia da computação", "Engenharia de software"]

print(f"Nossos cursos são: {cursos}")
print("----------------------------\n\n")

cursos[2] = "Enfermagem"

print(f"Nossos cursos são: {cursos}\n\n")

print(cursos[0])


#


lista_3 = [10, 20, 30]
lista_4 = [40, 50, 60]

def somar(lista_3, lista_4):
    print(f"Lista 3 mais lista 4: {lista_3[0] + lista_4[2]}")
    
somar(lista_3, lista_4)