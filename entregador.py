
class Entregador():
    def __init__(self) -> None:
        self.nome = 'Deivid Roberto'
        self.telefone = 69992678932
        self.placa = 'GTI3409'
        self.veiculo = 'Pop 100'
        self.corVeiculo = "Rosa Shock"
    
    def exibirDados(self) -> None:
        print('Nome do Entregador:', self.nome)
        print('Número para contato:', self.telefone)
        print('Nome do Veículo:', self.veiculo)
        print('Número da Placa:', self.placa)
        print('Cor do veículp:', self.corVeiculo)
