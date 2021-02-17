from cliente import *
from pedido import *
from entregador import *

print("\033[4;40;45m_____________AÇAÍ SHOW_____________/033[m")
print("___!!ALERTA!!PERIGOSO SE VICIAR!!___")
cliente = Cliente()
cliente.fazerPagamento()

pedido = Pedido()
pedido.confirmaPedido()

dados = Entregador  #Tentei colocar de uma forma menor, mas não parava de dar erro professora
dados.nome = "Nome do Entregador: Deivid"
dados.telefone = "Número para contato: 993382074"
dados.veiculo = "Veículo: Factor150"
dados.placa = "Número de Placa: EUP6U97"
print(dados.nome)
print(dados.telefone)
print(dados.veiculo)
print(dados.placa)
#dados.realizarEntrega() #isso não tá pegando, não sei pq, mas quando apaga esse comando o programa funciona, mas não aparece a frase
