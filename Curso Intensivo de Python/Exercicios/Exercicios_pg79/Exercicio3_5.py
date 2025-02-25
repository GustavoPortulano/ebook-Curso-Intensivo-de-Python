# 30 de outubro de 2024
# Quarta-feira, noite normal. 23h06min
# Alterando a lista de convidados

'''Você acabou de saber que um de seus 
convidados não poderá comparece ao jantar, portanto será necessário enviar
um novo conjunto de convites. Você deverá pensar em outra pessoa para
convidar.
* Comece com seu programa de Exercício 3.4; Acrescente uma instrução print
no final de seu programa, especificando o nome do convidade que não poderá
comparecer.
* Modifique sua lista, substituindo o nome do convidade que não poderá
comparecer pelo nome da nova pessoa que você está convidando.
* Exiba um segundo conjunto de mensagens com o convite, um para cada pessoa 
que continua presente em sua lista.'''

print()

lista_convidados = ['César', 'M. Antônio', 'Otavio', 'messalina', 'Livia', 'cleopata']
print()
print(lista_convidados[0].title(), ", convido você para um jantar em minha casa.")
print(lista_convidados[1].title(), ", convido voce para um jantar em minha casa.")
print(lista_convidados[2].title(), ", convido voce para um jantar em minha casa.")
print(lista_convidados[3].title(), ", convido voce para um jantar em minha casa.")
print(lista_convidados[4].title(), ", convido voce para um jantar em minha casa.")
print(lista_convidados[5].title(), ", convido voce para um jantar em minha casa.")

print()
print(10 * "*-*")
print()

print(lista_convidados[1].title(), " informou que não poderá comparecer ao nosso jantar.")
del lista_convidados[1]
print(lista_convidados)
lista_convidados.append('Julia')
print("Nova lista de convidados:")
print(lista_convidados)
print()
print("Novos convites:")
print(lista_convidados[0].title(), ", convido você para um jantar em minha casa.")
print(lista_convidados[1].title(), ", convido voce para um jantar em minha casa.")
print(lista_convidados[2].title(), ", convido voce para um jantar em minha casa.")
print(lista_convidados[3].title(), ", convido voce para um jantar em minha casa.")
print(lista_convidados[4].title(), ", convido voce para um jantar em minha casa.")
print(lista_convidados[5].title(), ", convido voce para um jantar em minha casa.")

print()