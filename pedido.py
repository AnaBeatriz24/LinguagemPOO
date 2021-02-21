from acaiTigela import*
from acaiBatida import*
#class Pedido:

#    def _init_(self):
#        self.tipo = input( "" )
#        self.tamanho = input( "" )
#        self.itensEscolhidos = []
#        self.itensDisponiveis = {
#            1: "Banana",
#            2: "Maçã",
#            3: "Morango",
#            4: "Kiwi",
#            5: "Uva", 
#            6:"Leite Condesado",
#            7: "Granola",
#            8: "Flocos", 
#            9: "Leite em pó", 
#            10: "Farinha Láctea", 
#            11: "Sucrilhos", 
#            12: "Mel", 
#            13: "Creme de Leite", 
#            14: "Guaraná em pó" }
#        self.tipoacai()
#        print("_________________________Cardápio_____________________________")
#        print("Tigela Pequena= R$10,00(Até 2 itens)")
#        print("Tigela Média= R$15,00(Até 3 itens)")
#        print("Tigela Grande= R$20,00(Até 4 itens")
#        print("Batida= R$10,00(400ml ate 2 itens)")

  
#    def tipoacai(self):
#        selecao = """
#        Escolha como irá querer seu açai:
#        1 - Tigela (a partir de R$ 10,00)
#        2 - Batida (R$ 10,00)
#        \n
#        """

        # verifica o tipo do pedido
#        try:
#            self.tipo = int(input(selecao))
#        except TypeError:
#            while (self.tipo not in [1, 2]):
#                self.tipo = int(input("Insira um valor válido"))

        # se for tigela entra aqui
#        if (self.tipo == 1):
#            self.tipo = "tigela de açaí"
#            selecao = """
#            Escolha o tamanho da sua tigela:
#            1 - P => R$ 10,00 com 2 itens
#            2 - M => R$ 20,00 com até 4 itens
#            3 - G => R$ 28,00 com ate 6 itens
#            \n
#            """
#            try:
#                self.tamanho = int(input(selecao))
#            except TypeError:
#                while (self.tamanho not in [1, 2, 3]):
#                    self.tamanho = int(input("Insira um valor válido"))
            
#            if self.tamanho == 1:
#                self.tamanho = "P"
#                self.preco = "R$ 10,00"
#            elif self.tamanho == 2:
#                self.tamanho = "M"
#                self.preco = "R$ 10,00"
#            else:
#                self.tamanho = "G"
#                self.preco = "R$ 10,00"


        # se for batida entra aqui
        #elif (self.tipo == 2):
            #self.tipo = "batida de açaí"
            #self.preco = "R$ 10,00"

            #print("Escolha seus itens (obs: para pedir o mesmo item mais de uma vez basta repetir seu código):")
#            for i in range(len(self.itensDisponiveis)):
#                print(f"{i+1} - {self.itensDisponiveis[i+1]}")
#            for i in range(1, 3):
                #self.itensEscolhidos.append(self.itensDisponiveis[int#(input(f"Item {i}:"))])


    #def confirmaPedido(self):
     #   print(f"Você comprou uma {self.tipo} com {self.itensEscolhidos}")
      #  print("___________________________________________________________")



class Pedido:
  def __init__(self):
    self._acai1 = acaiTigela()
    self._acai2 = acaiBatida()
    self.escolha = int(input('Selecione o número do '))
