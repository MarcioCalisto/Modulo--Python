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