class Tamagoshi:
    def __init__(self, Nome, Idade) -> None:
        # Método inicializador da classe. Ele define os atributos básicos do bichinho virtual.
        # Ao criar um bichinho, o usuário fornece o nome e a idade.
        # A saúde e a fome são inicializadas com valores padrão de 100.
        self.nome = Nome
        self.idade = Idade
        self.fome = 100
        self.saude = 100

    @property
    def Idade(self):
        # Getter para o atributo Idade.
        # Proporciona acesso ao valor de __Idade, mantendo encapsulamento.
        return self.__Idade

    @Idade.setter
    def Idade(self, Idade):
        # Setter para o atributo Idade.
        # Permite modificar o valor de __Idade, com possível validação no futuro.
        self.__Idade = Idade

    @property
    def Saude(self):
        # Getter para o atributo Saude.
        # Acessa o valor atual de __Saude, que representa o nível de saúde do bichinho.
        return self.__Saude

    @Saude.setter
    def Saude(self, Saude):
        # Setter para o atributo Saude.
        # Permite alterar o valor de __Saude, que controla como o bichinho está em termos de saúde.
        self.__Saude = Saude

    @property
    def Fome(self):
        # Getter para o atributo Fome.
        # Proporciona acesso ao valor de __Fome, que representa o nível de fome do bichinho.
        return self.__Fome

    @Fome.setter
    def Fome(self, Fome):
        # Setter para o atributo Fome.
        # Permite alterar o valor de __Fome, indicando se o bichinho está faminto ou saciado.
        self.__Fome = Fome

    def get_Humor(self):
        # Método que avalia o humor do bichinho virtual com base em sua fome e saúde.
        # Usa condições para verificar os níveis de fome e saúde, e imprime o humor correspondente.
        if self.__Fome >= 60 and self.__Saude >= 75:
            print("Estou muitooooo bemmm!!!")  # O bichinho está em ótimo estado.
        elif self.__Fome >= 45 and self.__Saude >= 55:
            print(
                "Preciso de cuidados, pfvr."
            )  # O bichinho precisa de atenção, mas ainda está razoavelmente bem.
        elif self.__Fome >= 30 and self.__Saude >= 40:
            print(
                "Estou a passar muito mal, me ajude."
            )  # O bichinho está em uma situação preocupante.
        else:
            print("Estou morrendo!!!")  # O bichinho está em estado crítico.


# Criando uma instância do bichinho virtual com nome "Claudinho" e idade 10.
Claudinho = BichinhoVirtual("Claudinho", 10)

# Alterando os atributos de fome e saúde do bichinho diretamente pelos setters.
Claudinho.Fome = 50
Claudinho.Saude = 50

# Avaliando e exibindo o humor do bichinho com base nos valores de fome e saúde.
Claudinho.get_Humor()
