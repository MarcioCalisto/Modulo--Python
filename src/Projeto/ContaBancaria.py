class ContaBancaria:
    def __init__(self, titular, numerodaconta, saldo, vip) -> None:
        self.titular = titular
        self.numerodaconta = numerodaconta
        self.saldo = saldo
        self.vip = vip

pessoa_1 = ContaBancaria('Marcio Calisto', 202020.5, 10, 'sim')
print(pessoa_1.numerodaconta)