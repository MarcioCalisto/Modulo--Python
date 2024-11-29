class Endereco:
    def __init__(self, Rua, Bairro, Cidade) -> None:
        self.__rua = Rua
        self.__bairro = Bairro
        self.__cidade = Cidade
    
    @property
    def Rua(self):
        return self.__rua
    
    @property
    def Bairro(self):
        return self.__bairro
    
    @property
    def Cidade(self):
        return self.__cidade