class estacionamento():
    def __init__(self, veiculo, placa, modelo, horarioEntrada, minutoEntrada, horarioSaida, minutoSaida) -> None:
        self.__veiculo = veiculo
        self.__placa = placa
        self.__modelo = modelo
        self.__horarioEntrada = horarioEntrada
        self.__minutoEntrada = minutoEntrada
        self.__horarioEntrada = horarioEntrada
        self.__minutoSaida = minutoSaida
        
    @property # método que permite encapsular o acesso a um atributo.
    def veiculo(self): # Define o método veiculo que será usado como getter.
        return self.__veiculo # Retorna o valor do atributo privado __veiculo.
    
    @veiculo.setter  # Permiti definir o valor do atributo __veiculo como se fosse um atributo comum.
    def veiculo(self, veiculo): # Define o método veiculo que será usado como setter.
        return self.__veiculo # Define o valor do atributo privado __veiculo.
    
    @property
    def placa(serf):
        return self.__placa
    
    @placa.setter
    def placa(self, placa):
        return self.__placa
    
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, modelo):
        return self.__modelo
    
    @property
    def horarioEntrada(self):
        return self.__horarioEntrada
    
    @horarioEntrada.setter
    def horarioEntrada(self, horarioEntrada):
        return self.__horarioEntrada
    
    
