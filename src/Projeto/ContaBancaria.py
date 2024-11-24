class ContaBancaria:
    def __init__(self, titular, numerodaconta, saldo, vip) -> None:
        self.titular = titular
        self.numerodaconta = numerodaconta
        self.saldo = saldo
        self.vip = vip

pessoa_1 = ContaBancaria('Marcio Calisto', 202020.5, 10, 'sim')
print(pessoa_1.numerodaconta)

# Upgrade - 0.1

titular = input("Informe o nome do titular: ")
numeroDaConta = float(input("Informe o número da conta: "))
saldo = float(input("Informe o saldo do titular: "))
vip = bool(input("Informe se você é vip S - N: "))

class ContaBancaria:
    def __init__(self) -> None:
        self.titular = titular
        self.numerodaconta = numeroDaConta
        self.saldo = saldo
        self.vip = vip
        
        if vip == True:
            print(input("Deseja ver seus beneficios S - N: "))
        else:
            print(input("Deseja se fazer o cadastro vip S - N: "))
            
Pessoa_2 = ContaBancaria()  

# Upgrade - 0.2

class ContaBancaria:
    def __init__(self, titular, numeroDaConta, saldo, vip) -> None:
        self.titular = titular 
        self.numerodaconta = numeroDaConta
        self.saldo = saldo
        self.vip = vip
    
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor
            print(self.saldo)
            
    def depositar(self, valor):
        if valor >= 0:
            self.saldo = self.saldo + valor
        else:
            print("Valor inválido!")

titular = input("Digite o nome do titular: ")
numeroDaConta = float(input("Digite o número da conta: "))
saldo = float(input("Digite o saldo do titular: "))
vip = bool(input("Informe o vip: "))

Pessoa_3 = ContaBancaria(titular, numeroDaConta, saldo, vip)

print(f"Seu saldo antigo: {Pessoa_3.saldo}")

Pessoa_3.saldo = 3000.00

print(f"Seu saldo atual: {Pessoa_3.saldo}")

Pessoa_3.sacar(2000)

print(f"Seu saldo após o saque: {Pessoa_3.saldo}")

Pessoa_3.depositar(1500)

print(f"Seu saldo após o deposito: {Pessoa_3.saldo}")