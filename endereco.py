class Endereco():
    def __init__(self) -> None:
        self._bairro = input("Digite o nome do seu bairro: ")
        self._rua = input("Digite o nome da sua rua: ")
        self._numero = "S/ Número"
        try:
            entrada = int(input("Digite o número da sua casa (caso não haja numero, digite '0'): "))
            if (self._numero.isnumeric()):
                self._numero = entrada
        except:
            while (not self._numero.isnumeric()):
                print ('Preencha Corretamente!!!')
                entrada = input("Digite o número da sua casa (caso não haja numero, digite '0'): ")
            if (self._numero.isnumeric()):
                self._numero = int(entrada)