class Produto                                                       : 
    def __init__(self, codigo, nome, valor)                         : 
        self.codigo                                                 = codigo
        self.nome                                                   = nome
        self.valor                                                  = valor


class Carrinho                                                      : 
    def __init__(self)                                              : 
        self.produtos                                               = []

    def addCarrinho(self, produto)                                  : 
        self.produtos.append(produto)

    def listarProdutos(self)                                        : 
        for produto in self.produtos                                : 
            print(f"Código                                          : {produto.codigo}")
            print(f"Nome do Produto                                 : {produto.nome}")
            print(f"Preço                                           : {produto.valor}")

    def calcularTotal(self)                                         : 
        total                                                       = 0
        for produto in self.produtos                                : 
            total                                                   = total + produto.valor

        print(f"Valor total da sua compra                           : {total}")


carrinho                                                            = Carrinho()
while True                                                          : 
    print("-- SELECIONE UMA OPÇÃO --")
    print("1 - Adicionar produto ")
    print("2 - Listar Produtos ")
    print("3 - Finalizar compra ")
    print("4 - Sair ")

    opcao                                                           = int(input("Selecione entre 1 - 4: "))

    if opcao == 4:
        break

    if opcao == 1:
        codigo                                                      = int(input("Informe o código do produto: "))
        nome                                                        = input("Informe o nome do produto: ")
        valor                                                       = float(input("Informe o valor do produto: "))

        produto                                                     = Produto(codigo, nome, valor)
        carrinho.addCarrinho(produto)

    if opcao == 2:
        carrinho.listarProdutos()

    if opcao == 3:
        carrinho.calcularTotal()


######################################################################


class Escola                                                        : 
    def __init__(self, nome, endereco)                              : 
        self.nome                                                   = nome
        self.endereco                                               = endereco
        self.cursos                                                 = ["Dev FullStack", "Fotografia", "Design"]
        self.alunos                                                 = []

    def listarAlunos(self)                                          : 
        for aluno in self.alunos                                    : 
            print(f"Matricula                                       : {aluno.matricula}")
            print(f"Nome                                            : {aluno.nome}")
            print(f"Idade                                           : {aluno.idade}")
            print(f"Curso                                           : {aluno.curso}")
            print(f"-----------------------------\n")

    def matricularAluno(self, aluno)                                : 
        self.alunos.append(aluno)


class Aluno                                                         : 
    def __init__(self, matricula, nome, idade, curso)               : 
        self.matricula                                              = matricula
        self.nome                                                   = nome
        self.idade                                                  = idade
        self.curso                                                  = curso


aluno1                                                              = Aluno(1, "João", 19, "Dev FullStack")
aluno2                                                              = Aluno(2, "Maria", 21, "Fotografia")


escola                                                              = Escola("Infinity School", "Santos Dummont")
escola.matricularAluno(aluno1)
escola.matricularAluno(aluno2)

escola.listarAlunos()


#####################################################################

class Funcionario                                                   : 
    def __init__(self)                                              : 
        self.__matricula                                            = ""
        self.__nome                                                 = ""
        self.__salario                                              = 0

    @property
    def matricula(self)                                             : 
        return self.__matricula

    @property
    def nome(self)                                                  : 
        return self.__nome

    @property
    def salario(self)                                               : 
        return self.__salario

    @matricula.setter
    def matricula(self, matricula)                                  : 
        self.__matricula                                            = matricula

    @nome.setter
    def nome(self, nome)                                            : 
        self.__nome                                                 = nome

    @salario.setter
    def salario(self, salario)                                      : 
        self.__salario                                              = salario


class Estagiario(Funcionario)                                       : ...


class Gerente(Funcionario)                                          : ...


estagiario                                                          = Estagiario()
estagiario.matricula                                                = "3423423"
estagiario.nome                                                     = "Rodrigo"
estagiario.salario                                                  = 10000
print(estagiario.matricula)
print(estagiario.nome)
print(estagiario.salario)


class Funcionario                                                   : 
    def __init__(self, matricula, nome, salario)                    : 
        self.matricula                                              = matricula
        self.nome                                                   = nome
        self.salario                                                = salario


class Estagiario(Funcionario)                                       : ...


class Gerente(Funcionario)                                          : ...


estagiario                                                          = Estagiario(342342, "Lucas", 10000)
gerente                                                             = Gerente(546455, "Rodrigo", 60000)

######################################################################


class Funcionario                                                   : 
    def __init__(self, matricula, nome, salario)                    : 
        self.matricula                                              = matricula
        self.nome                                                   = nome
        self.salario                                                = salario


class Gerente(Funcionario)                                          : 
    def __init__(self, matricula, nome, salario, Setor, Comissao)   : 
        super().__init__(matricula, nome, salario)
        self.Setor                                                  = Setor
        self.Comissao                                               = Comissao

    def Contratar(self, qtd_funcionarios)                           : 
        if qtd_funcionarios < 10                                    : 
            print(f"Contratar                                       : {10 - qtd_funcionarios}")
        else                                                        : 
            print("Temos gente o suficiente")


class Estagiario(Funcionario)                                       : 
    def __init__(self, matricula, nome, salario, qtd_Horas)         : 
        super().__init__(matricula, nome, salario)
        self.qtd_Horas                                              = qtd_Horas

    def contratacao(self)                                           : 
        if self.qtd_Horas >= 300:
            print("Contratato!!!")
        else                                                        : 
            print("Ainda não acabou.")


estagiario                                                          = Estagiario("01", "marcio", "2.000", 300)
estagiario.contratacao()
print(f"Matricula                                                   : {estagiario.matricula}")
print(f"Nome                                                        : {estagiario.nome}")
print(f"Sálario                                                     : {estagiario.salario}")
print(f"Quantidade Horas                                            : {estagiario.qtd_Horas}")
estagiario.contratacao

print("--------------------------------------------\n")

gerente                                                             = Gerente("02", "joao", "3.000", "gerencia", "2.000")
gerente.Contratar(5)
print(f"Matricula                                                   : {gerente.matricula}")
print(f"Nome                                                        : {gerente.nome}")
print(f"Sálario                                                     : {gerente.salario}")
print(f"Setor                                                       : {gerente.Setor}")
print(f"Comissão                                                    : {gerente.Comissao}")

######################################################################


class Conta                                                         : 
    def __init__(self, Numero, Titular, Saldo) -> None              : 
        self.__Numero                                               = Numero
        self.__Titular                                              = Titular
        self.__Saldo                                                = Saldo

    @property
    def Numero(self)                                                : 
        return self.__Numero

    @Numero.setter
    def Numero(self, Numero)                                        : 
        self.__Numero                                               = Numero

    @property
    def Titular(self)                                               : 
        return self.__Titular

    @Titular.setter
    def Titular(self, Titular)                                      : 
        self.__Titular                                              = Titular

    @property
    def Saldo(self)                                                 : 
        return self.__Saldo

    @Saldo.setter
    def Saldo(self, Saldo)                                          : 
        self.__Saldo                                                = Saldo

    def sacar(self, Valor)                                          : 
        if self.Saldo - Valor > 0                                   : 
            self.Saldo                                              -= Valor
            print("Saque realizado.")

    def depositar(self, Valor)                                      : 
        if Valor > 0                                                : 
            self.Saldo                                              += Valor
            print("Deposito feito.")


class ContaCorrente(Conta)                                          : 
    def __init__(self, Numero, Titular, Saldo, Limite) -> None      : 
        super().__init__(Numero, Titular, Saldo)
        self.__Limite                                               = Limite

    @property
    def Limite(self)                                                : 
        return self.__Limite

    @Limite.setter
    def Limite(self, Limite)                                        : 
        self.__Limite                                               = Limite

    def extrato(self)                                               : 
        print(f"Número da conta                                     : {self.__Numero}")
        print(f"Número da conta                                     : {self.__Titular}")
        print(f"Número da conta                                     : {self.__Saldo}")
        print(f"Número da conta                                     : {self.__Limite}")


class Poupanca(Conta)                                               : 
    def __init__(self, Numero, Titular, Saldo, rendimento) -> None  : 
        super().__init__(Numero, Titular, Saldo)
        self.rendimento                                             = rendimento

    def RendimentoMensal(self)                                      : 
        self.__Saldo                                                = self.__Saldo + (self.__Saldo * (self.rendimento / 100))
        print(f"Saldo após o rendimento                             : {self.__Saldo}")


Conta01                                                             = Conta("020202-2", "Calixto", "6.000,00")
print(f"Número da conta                                             : {Conta01.Numero}")
print(f"Nome do titular                                             : {Conta01.Titular}")
print(f"Saldo do titular                                            : {Conta01.Saldo}")
