# 22 de novembro de 2024
# Sexta-feira, tarde nublada.

'''Exercício 7.8 - Lanchonete: Crie uma lista chamada sandwich_orders e a preencha com
os nomes de vários sanduíches. Em seguida, crie uma lista vazia chamada
finished_sandwiches. Percorra a lista de pedidos de sanduíches com um laço e 
mostre uma mensagem para cada pedido, por exemplo, Preparei seu
sanduíche de atum. À medida que cada sanduíche for preparado, transfira-o
para a lista de sanduíches prontos. depois que todos os sanduíches estiverem 
prontos, mostre uma mensagem que liste cada sanduíche preparado.'''

sandwich_order = ['pão com ovo', 'misto quente', 'hamburguer', 'cachorro quente']
finished_sandwiches = []

while sandwich_order:
    sandwichs = sandwich_order.pop()
    print("Sanduiches pronto: ", sandwichs)
    finished_sandwiches.append(sandwichs)

print("\nSanduiches finalizados e entregues:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)