class Endereco:
    def __init__(self):
        self._bairro = input("Digite o nome do seu bairro: ")
        self._rua = input("Digite o nome da sua rua: ")
        try:
            self._numero= int(input("Digite o número da sua casa: "))
        except:
            print ('Preencha Corretamente!')
            self._numero= int(input("Digite o número da sua casa: "))
