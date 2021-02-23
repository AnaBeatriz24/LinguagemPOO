#Ana Beatriz de Freitas Teixeira
#Klauanny Cordeiro Maia
#2°Informática Matutino
#Progamação Orientada a Objetos


from cliente import *
from pedido import *
from entregador import *

print("+------------------------[ AÇAÍ SHOW ]------------------------+")
print("+-------[ ALERTA: ESTE PRODUTO PODE CAUSAR DEPENDECIA ]-------+")

cliente = Cliente()

novoPedido = Pedido()
novoPedido.fazerPedido()
novoPedido.confirmarPedido()

entregador = Entregador()
entregador.exibirDados()
