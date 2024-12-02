"""
A programação Orientada a Objeto(POO)
"""
# class Elevador:
#     def __init__(self, capacidade, qtd_andares, qtd_pessoas, andar_atual):
#         self.capacidade = capacidade
#         self.qtd_andares = qtd_andares
#         self.qtd_pessoas = qtd_pessoas
#         self.andar_atual = andar_atual

#     def subir(self):
#         if self.andar_atual < self.qtd_andares - 1:
#             self.andar_atual += 1
#             print('Subindo...')
#             print(f'Andar atual: {self.andar_atual}')
#         else:
#             print('Você já está no ultimo andar!')

#     def descer(self):
#         if self.andar_atual == 0:
#             print('Você já esta no terreo!!')
#         else:
#             self.andar_atual -= 1
#             print('Descendo...')
#             print(f'Andar atual: {self.andar_atual}')

#     def entrar(self, qtd_pessoas):
#         if self.qtd_pessoas + qtd_pessoas >= self.capacidade:
#             print('Elevador lotado!!!')
#         else:
#             self.qtd_pessoas += qtd_pessoas
#             print('Entrando...')
#             print(f'Quantidade de pessoas: {self.qtd_pessoas}')

#     def sair(self, qtd_pessoas):
#         if self.qtd_pessoas - qtd_pessoas < 0:
#             print('Não tem essa quantidade dentro do elevador!!')
#         else:
#             self.qtd_pessoas -= qtd_pessoas
#             print('Saindo...')
#             print(f'Quantidade de pessoas: {self.qtd_pessoas}')




# elevador = Elevador(20,15,7,5)

# plaza = Elevador(30, 10, 9, 9)

# elevador.subir()
# elevador.subir()
# elevador.subir()
# elevador.entrar(5)
# elevador.sair(7)
# elevador.descer()
# elevador.descer()
