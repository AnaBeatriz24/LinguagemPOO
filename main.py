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

entregador = Entregador()
entregador.exibirDados()