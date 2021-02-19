class Entregador:
    
    def __init__(self):
        print("___________________________________________________________") 
        self._nome = ""
        self._telefone = ""
        self._veiculo = ""
        self._placa = ""
  
    def mostraDados(self):
        print('Nome do Entregador:', self._nome)
        print('Número para contato:', self._telefone)
        print('Nome do Veículo:', self._veiculo)
        print('Número da Placa:', self._placa)

    def realizarEntrega(self):
        print("!!SEU PEDIDO ESTÁ A CAMINHO!!")
        self.mostraDados()