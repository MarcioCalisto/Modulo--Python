class Salario:
    """
    Classe responsável por calcular o salário de um funcionário com base em:
    - Valor por hora trabalhada (valorHora)
    - Quantidade de horas trabalhadas no mês (qtdHora)
    - Comissão adicional (comissao)
    """

    def __init__(self, valorHora, qtdHora, comissao) -> None:
        """
        Inicializa os atributos necessários para o cálculo do salário.
        Parâmetros:
        - valorHora (float): Valor recebido por hora trabalhada.
        - qtdHora (int): Quantidade de horas trabalhadas.
        - comissao (float): Valor da comissão adicional.
        """
        self.valorHora = valorHora
        self.qtdHora = qtdHora
        self.comissao = comissao

    def CalcularSalario(self):
        """
        Calcula o salário total com base no valor hora, quantidade de horas e comissão.
        Retorna:
        - float: Salário total do funcionário.
        """
        return (self.valorHora * self.qtdHora) + self.comissao


class Funcionario:
    """
    Classe que representa um funcionário e utiliza a classe Salario para calcular
    o salário total do mesmo.
    """

    def __init__(self, nome, idade, valorHora, qtdHora, comissao) -> None:
        """
        Inicializa o funcionário com seus dados básicos e associa o objeto Salario.
        Parâmetros:
        - nome (str): Nome do funcionário.
        - idade (int): Idade do funcionário.
        - valorHora (float): Valor recebido por hora trabalhada.
        - qtdHora (int): Quantidade de horas trabalhadas no mês.
        - comissao (float): Valor da comissão adicional.
        """
        self.nome = nome
        self.idade = idade
        self.Salario = Salario(valorHora, qtdHora, comissao)

    def SalarioTotal(self):
        """
        Retorna o salário total do funcionário.
        Retorna:
        - float: Salário total calculado.
        """
        return self.Salario.CalcularSalario()


# Instância da classe Funcionario.
Funcionario = Funcionario("Márcio Calisto", 16, 22, 160, 1500)

# Exibe o salário total calculado.
print(f"Salário Total: {Funcionario.SalarioTotal()}")
