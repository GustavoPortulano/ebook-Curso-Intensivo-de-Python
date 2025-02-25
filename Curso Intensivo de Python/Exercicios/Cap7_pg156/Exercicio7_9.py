# 22 de novembro de 2024
# Sexta-feira, tarde nublada

'''Exercício 7.9 - Sem pastrami: Usando a lista sandwich_orders do exercício 7.8, garanta
qu o sanduiche de pastrami apareça na lista pelo menso três vezes.
Acrescente um código próximo ao inicio de seu programa para exibir uma
mensagem inforando que a lanchonete está sem pastrami e, então, use um
laço while para remover todas as ocorrências de pastrami em sadwich_orders.
Garanta que nenhum sanduíche de pastrami acabe em finished_sandwiches.
'''

sandwich_order = ['pastrami', 'pão com ovo','patrami' ,'misto quente',
                  'hamburguer', 'cachorro quente', 'pastrami']
finished_sandwiches = []

print("A lanchonete está sem pastrami.\n")

while sandwich_order:
    sandwichs = sandwich_order.pop()
    print("Sanduiches pronto: ", sandwichs)
    if sandwich_order == ['pastrami']:
        sandwich_order.remove('pastrami')
    finished_sandwiches.append(sandwichs)

print("\nSanduiches finalizados e entregues:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)