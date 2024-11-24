class Elevador:
    def __init__(self, capacidade, qtd_andares, qtd_pessoas, andar_atual) -> None:
        self.capacidade = capacidade
        self.qtd_andares = qtd_andares
        self.qtd_pessoas = qtd_pessoas
        self.andar_atual = andar_atual
    
    def subir(self):
        if self.andar_atual < self.qtd_andares - 1:
            self.andar_atual += 1
            print("Subindo...")
            print(f"Andar atual: {self.andar_atual}")
        else:
            print("Você já está no ultimo andar...")
            
    def descer(self):
        if self.andar_atual == 0:
            print("Você já está no terreo...")
        else:
            self.andar_atual -= 1
            print("Descendo...")
            print(f"Andar atual: {self.andar_atual}")
    
    def entrar(self, qtd_pessoas):
        if self.qtd_pessoas + qtd_pessoas >= self.capacidade:
            print("Elevador lotado...")
        else:
            self.qtd_pessoas += qtd_pessoas
            print("Entrando...")
            print(f"Quantidade de pessoas atual: {self.qtd_pessoas}")
            
    def sair(self, qtd_pessoas):
        if self.qtd_pessoas - qtd_pessoas < 0:
            print("Não tem essa quantidade dentro do elevador...")
        else:
            self.qtd_pessoas -= qtd_pessoas
            print("Saindo...")
            print(f"Quantidade de pessoas atual: {self.qtd_pessoas}")
            
            
            
elevador_hapvida = Elevador(10, 13, 5, 6)

elevador_plaza_tower = Elevador(10, 2, 4, 1)



elevador_hapvida.subir()
elevador_hapvida.entrar(2)
elevador_hapvida.sair(1)
elevador_hapvida.descer()

elevador_plaza_tower.subir()
elevador_plaza_tower.entrar(2)
elevador_plaza_tower.sair(1)
elevador_plaza_tower.descer()
