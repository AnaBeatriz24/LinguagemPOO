class Entregador:
    
  def __init__(self, nome, telefone, veiculo, placa):
     print("___________________________________________________________") 
     self._nome= nome
     self._telefone= telefone
     self._veiculo= veiculo
     self._placa= placa
  
  def mostraDados(self):
    print('Nome do Entregador:', self._nome)
    print('Número para contato:', self._telefone)
    print('Nome do Veículo:', self._veiculo)
    print('Número da Placa:', self._placa)

  def realizarEntrega(self):
    print ("!!SEU PEDIDO ESTÁ A CAMINHO!!")

     #self._nomE=print ("Nome do Entregador:Deivid Roberto")
     #self.telefonE=print ("Telefone para contato:93382074")
     #self.veiculo=print ("Veículo: Moto (Factor150)")
     #self.placa=print ("Placa:EUP6U97")
