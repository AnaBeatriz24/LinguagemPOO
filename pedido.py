class Pedido:
    def __init__(self):

        print("___________________________________________________________")
        #self._preco= 10.0
        print("Tigela Pequena= R$10,00(Até 2 itens)")
        print("Tigela Média= R$15,00(Até 3 itens)")
        print("Tigela Grande= R$20,00(Até 4 itens")
        print("Barca Pequena=R$25,00(Até 5 itens)")
        print("Barca Média=R$30,00(Até 7 itens)")
        print("Barca Grande=R$35,00(Até 9 itens)")
        print("Itens Disponíveis: Banana,Maçã,Morango, Kiwi, Uva")
        print("Leite Condesado, Cobertura de Chocolate, Nutella, Granola, Flocos, Leite em pó, Tapioca, Chantilly, Farinha Láctea, Ovomaltine, Bis, Sucrilhos, Aveia, Jujuba, Paçoca, Biscoito, Mel, Creme de Leite, Cobertura Morango")
        self._nomeProduto= input("Açaí na Barca ou na Tigela: ")
        self._quantidade= input("Pequena, Média ou Grande: ")
        self._fruta= input("Itens Disponíveis: ")
        print("___________________________________________________________")


    def confirmaPedido(self):
        print("Você comprou uma",self._nomeProduto,self._quantidade, "com", self._fruta)
        print("___________________________________________________________")