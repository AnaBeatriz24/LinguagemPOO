from endereco import*
class Cliente:
    def __init__(self):
        print("___________________________________________________________")

        self._nome = input("Digite nome: ")
        try:
          self._telefone = int(input("Digite número para contato: "))
        except NameError:
          print('Somente números!')
        except ValueError:
          print('Adicione um número válido')
        
        self._email = input("Digite seu email: ")
        self._endereco = Endereco()
        print("___________________________________________________________")

    
    def fazerPagamento(self):
        selecao = """
        1 - Dinheiro
        2 - Cartão de Débito
        3 - Crédito
        Digite o número: """ 
        print("!!Aceitamos Cartão de Crédito e Débito!!")
        try:
          self._formapaga = int(input(selecao))
        except:
          print('Adicione sua forma de pagamento(1, 2 ou 3)')

        print("___________________________________________________________")
