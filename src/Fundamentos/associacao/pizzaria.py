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
    
class Empresa:
    def __init__(self, nome, area) -> None:
        self.__nome = nome
        self.__area = area
        self.__enderecos = []
        
    @property
    def nome(self):
        return self.__nome
    
    @Setter.nome
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def area(self):
        return self.__area
    
    @Setter.area 
    def area(self, area):
        self.__area = area
        
    def inserirEndereco(self, rua, bairro, cidade):
        self.obj_endereco = Endereco(rua, bairro, cidade)
        self.__enderecos.append(self.obj_endereco)
        print(f"Endereço cadastrado com sucesso!!")
        
    def exibirEnderecos(self):
        for endereco in self.__enderecos:
            print(
                f"Rua: {endereco.rua} - Bairro: {endereco.bairro} - Cidade: {endereco.cidade}"
            )
            
pizza_hut = Empresa("Pizza Hut", "Alimentício")
pizza_hut.inserirEndereco("Av Santos Dummont", "Aldeota", "Fortaleza")
pizza_hut.inserirEndereco("Pe. Antonio Thomaz", "Água Fria", "Fortaleza")
pizza_hut.exibirEnderecos()