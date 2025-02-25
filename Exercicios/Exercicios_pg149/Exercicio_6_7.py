# 20 de novembro de 2024
# Quarta-feira, noite chuvosa
# Samuel dormiu em casa
# Omar almoçou em casa
# Ida a Lagoa Santa após receber ligação de que estavam furtando madeira na casa.

'''Exercício 6.7 - Pessoas: Comece com o program que você escreveu no Exercício 6.1.
Crie dois novos dicionários que representem pessoas diferentes e 
armazena os três dicionários em uma lista chamada people. Percorra sua lista
de possoas com um laço. À medida que percorrer a lista, apresente tudo que
você sabe sobre cada pessoa.'''

print()

ana = {'nome':'ana', 'sobrenome':'silvestre'}
bella = {'nome':'bela', 'sobrenome':'lovelance'}
celia = {'nome':'celia', 'sobrenome':'cristina'}

pessoas = [ana, bella, celia]

print("Imprimindo a lista com os dicionários:")
for pessoa in pessoas:
    print(pessoa)
print()

print("Imprimindo informações pessoais:")
for pessoa in pessoas:
    if pessoa == ana:
        print("Primeiro nome: ", pessoa['nome'].title())
        print("Sobrenome: ", pessoa['sobrenome'].title())
        print("Nome completo: ", pessoa['nome'].title(), pessoa['sobrenome'].title(), "\n")
    elif pessoa == bella:
        print("Primeiro nome: ", pessoa['nome'].title())
        print("Sobrenome: ", pessoa['sobrenome'].title())
        print("Nome completo: ", pessoa['nome'].title(), pessoa['sobrenome'].title(), "\n")
    elif pessoa == celia:
        print("Primeiro nome: ", pessoa['nome'].title())
        print("Sobrenome: ", pessoa['sobrenome'].title())
        print("Nome completo: ", pessoa['nome'].title(), pessoa['sobrenome'].title(), "\n")