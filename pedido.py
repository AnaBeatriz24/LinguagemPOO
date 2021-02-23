class Pedido():
    def __init__(self):
        self.formapaga = ""
        self.tipo = ""
        self.produto = ""
        self.preco = 0
        self.itensDisponiveis = {
            "batida": { 
                "ricardão": {
                    "itens": "Açaí, Amendoim, mel, guaraná em pó", 
                    "preco": 13.00,
                },
                "shake": {
                    "itens": "Açaí, Leite em Pó, Creme de Leite, Leite Condensado",
                    "preco": 12.00,
                },
                "shake com frutas": {
                    "itens": "Açaí, Leite em Pó, Creme de Leite, Leite Condensado, Banana, Abacaxi, Uva, Mamão, Kiwi",
                    "preco": 15.00,
                },
            },
            "tigela": {
                "energy": {
                    "itens": "Açaí, Banana, Leite em Pó, Creme de Leite, Leite Condensado",
                    "preco": 16.00,
                },
                "ribeirinho": {
                    "itens": "Açaí , Tapioca",
                    "preco": 10.00
                },
                "mel e granola": {
                    "itens": "Açaí , Mel , Granola",
                    "preco": 14.00
                },
                "kids": {
                    "itens": "Açaí, Mm’s, Banana, Granulado, Canudo de Chocolate, Cobertura de Morango",
                    "preco": 18.00
                },
            },
        }
  
    def fazerPedido(self) -> None:
        print("+----------------------[ OPÇÕES ]----------------------+")
        opcao = 0
        while (opcao not in [1, 2]):
            try:
                opcao = int(input("""
                1 - Tigela
                2 - Batida
                """))
            except:
                opcao = int(input("Insira um valor válido: "))

        if opcao == 1:
            self.tipo = "tigela"
        else:
            self.tipo = "batida"

        aux = self.itensDisponiveis

        itens = [valor for chave, valor in sorted(aux[self.tipo].items())]
        chaves = [chave for chave, valor in sorted(aux[self.tipo].items())]
        for j in range(len(itens)):
            print("+--------------------------+")
            print((j+1),"-",chaves[j])
            print("Itens:",itens[j]["itens"])
            print("Preço: R$",itens[j]["preco"])
            print("+--------------------------+")
        codigo = int(input("Insira o código do produto:"))
        self.produto = chaves[codigo-1]
        self.preco = itens[codigo-1]["preco"]
        print("+------------------------------------------------------+")
        self._fazerPagamento()

    def confirmarPedido(self) -> None:
        print("\n+----------------------------------------------------------+")
        print("Você comprou uma {} {} contendo:\n{}\nno valor de {} reais para pagar no {}\n\nDeseja prosseguir (S/N)?".format(
           self.tipo.title(), 
           self.produto.title(), 
           self.itensDisponiveis[self.tipo][self.produto]["itens"],
           self.preco,
           self.formapaga
           )
        )
        e_agr = input().upper()
        while (e_agr not in ["S", "N"]):
            e_agr = input("Insira um valor válido (S/N): ").upper()
        
        if e_agr == "S":
            print("Certo. Seu pedido será enviado para a entrega")
        else:
            print("Lamentamos por desistir do seu pedido :(\nSe houver alguma reclamação, favor guardar para si pois \nainda não temos SAC")
            exit()

        print("+----------------------------------------------------------+\n")

    def _fazerPagamento(self) -> None:
        formas_pag = ["Dinheiro","Cartão de Débito", "Crédito"]
        selecao = """
        1 - Dinheiro
        2 - Cartão de Débito
        3 - Crédito 
        """ 

        try:
            entrada = int(input(selecao))
            self.formapaga = formas_pag[entrada - 1]
        except:
            while(self.formapaga not in formas_pag):
                entrada = int(input("Escolha uma forma de pagamento (1, 2 ou 3): "))
                self.formapaga = formas_pag[entrada - 1]

        print("+----------------------------------------------------------+\n")
