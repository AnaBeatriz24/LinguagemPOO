#Ana Beatriz de Freitas Teixeira
#2°Inforática Matutino
#Progamação Orientada a Objetos

#@Beatriz
#1) Pedido: falta preço
#2) Entregador: falta construtor
#3) Entregador: arrumar o exibir dados do entregador

from cliente import *
from pedido import *
from entregador import *

print("_____________AÇAÍ SHOW_____________")
print("___!!ALERTA!!PERIGOSO SE VICIAR!!___")
cliente = Cliente()
cliente.fazerPagamento()

pedido = Pedido()
# pedido.confirmaPedido()

dados = Entregador()  #Tentei colocar de uma forma menor, mas não parava de dar erro professora
dados.nome = "Nome do Entregador: Deivid"
dados.telefone = "Número para contato: 993382074"
dados.veiculo = "Veículo: Factor150"
dados.placa = "Número de Placa: EUP6U97"
dados.realizarEntrega()
