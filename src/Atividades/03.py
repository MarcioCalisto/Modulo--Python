turno = str(input("Digite seu turno Manhã(M), Tarde(T), Noite(N) / [A, T, N]"))

if turno == "A" or turno == "a":
    print("Bom dia!")
elif turno == "T" or turno == "t":
    print("Boa tarde!")
else:
    print("Boa noite!")