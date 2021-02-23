#Ana Beatriz de Freitas Teixeira
#2°Inforática Matutino
#Progamação Orientada a Objetos

#@Beatriz
#1) Pedido: falta preço - feito
#2) Entregador: falta construtor - feito
#3) Entregador: arrumar o exibir dados do entregador - feito

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