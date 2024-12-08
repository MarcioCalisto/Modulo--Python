principal = float(input("Digite o valor principal (R$): "))
taxaJuros = float(input("Digite a taxa de juros (R$): "))
tempo = float(input("Digite o tempo (em anos): "))
    
juros = (principal * taxaJuros * tempo) / 100
montante = principal + juros
        
print("\n--- Resultado ---")
print(f"Juros simples: R${juros:.2f}\n")
print(f"Montante total (principal + juros): R${montante:.2f}\n")
