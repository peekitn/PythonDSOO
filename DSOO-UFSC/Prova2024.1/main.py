# Importando as classes dos arquivos que você criou
from cliente import Cliente
from cliente_fidelidade import ClienteFidelidade
from tipo_pedido import TipoPedido
from pedido import Pedido
from controlador_pedidos import ControladorPedidos

# 1. Instanciando o Controlador
print("Inicializando o sistema...")
controlador = ControladorPedidos()

# 2. Instanciando os Clientes
# Cliente comum
cliente_joao = Cliente(cpf="111.111.111-11", nome="João Silva", endereco="Rua A, 123", telefone="9999-1111")

# Cliente fidelidade (recebe todos os dados do cliente + código e desconto de 10%)
cliente_maria_vip = ClienteFidelidade(codigo_fidelidade=1001, desconto=0.10, cpf="222.222.222-22", nome="Maria Souza", endereco="Av B, 456", telefone="8888-2222")

# 3. Instanciando os Tipos de Pedido
tipo_normal = TipoPedido(descricao="Entrega Padrão", fator_distancia=1.5) # R$ 1.50 por km
tipo_fragil = TipoPedido(descricao="Entrega Frágil", fator_distancia=3.0) # R$ 3.00 por km

# 4. Instanciando os Pedidos
pedido_1 = Pedido(numero=1, cliente=cliente_joao, tipo=tipo_normal)
pedido_2 = Pedido(numero=2, cliente=cliente_maria_vip, tipo=tipo_fragil)

# 5. Adicionando Itens aos Pedidos (usando o método da classe)
# Pedido do João
pedido_1.inclui_item_pedido(codigo=101, descricao="Pizza de Calabresa", preco=45.00)
pedido_1.inclui_item_pedido(codigo=102, descricao="Refrigerante 2L", preco=12.00)
# Valor em itens do pedido 1 = R$ 57.00

# Pedido da Maria
pedido_2.inclui_item_pedido(codigo=201, descricao="Torta de Morango (Frágil)", preco=80.00)
# Valor em itens do pedido 2 = R$ 80.00

# 6. Incluindo os pedidos no Controlador
controlador.incluir_pedido(pedido_1)
controlador.incluir_pedido(pedido_2)

# 7. Realizando os cálculos de Faturamento (Teste da Questão 06)
print("\n--- Fechamento de Faturas ---")
distancia_entrega = 10.0 # Simulando uma entrega a 10km de distância

# Cálculo do João (Cliente Comum): 
# Itens (57.00) + [Fator (1.5) * Distancia (10)] -> 57 + 15 = R$ 72.00
faturamento_joao = controlador.calcular_faturamento_pedidos(distancia=distancia_entrega, cpf="111.111.111-11")
print(f"Faturamento de {cliente_joao.nome}: R$ {faturamento_joao:.2f}")

# Cálculo da Maria (Cliente Fidelidade com 10% de desconto): 
# Itens (80.00) + [Fator (3.0) * Distancia (10)] -> 80 + 30 = 110.00
# Desconto de 10% sobre 110.00 = - R$ 11.00 -> Total: R$ 99.00
faturamento_maria = controlador.calcular_faturamento_pedidos(distancia=distancia_entrega, cpf="222.222.222-22")
print(f"Faturamento de {cliente_maria_vip.nome} (VIP): R$ {faturamento_maria:.2f}")