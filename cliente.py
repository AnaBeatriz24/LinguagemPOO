class Cliente:
    def __init__(self):
        print("___________________________________________________________")

        self._nome = input("Digite nome: ")
        self._telefone = input("Digite número para contato: ")
        self._email = input("Digite seu email: ")
        self._endereco = Endereco()
        print("___________________________________________________________")

    
    def fazerPagamento(self):
        selecao = """
        1 - Dinheiro
        2 - Cartão de Débito
        3 - Crédito
        """ 
        print("!!Aceitamos Cartão de Crédito e Débito!!")
        self._formapaga = int(input(selecao))
        print("___________________________________________________________")
