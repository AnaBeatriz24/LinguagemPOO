from endereco import *


class Cliente:
    def __init__(self):
        print("___________________________________________________________")

        self._nome = input("Digite nome: ")
        self._telefone = input("Digite número para contato: ")
        self._email = input("Digite seu email: ")
        self._endereco = Endereco()
        print("___________________________________________________________")

    def fazerPagamento(self):
        print("!!Aceitamos Cartão de Crédito e Débito!!")
        self._formapaga = input("Dinheiro, Cartão de Débito ou Crédito: ")
        print("___________________________________________________________")

