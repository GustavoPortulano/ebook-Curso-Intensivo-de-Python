# 31 de outubro de 2024
# Quinta-feira, dia normal. 00h06min
# Reduzindo a lista de convidados

'''Você acabou de descibrur que sua nova mesa de jantar
não chegará a tempo para o jantar e tem espaço para apenas
duas pessoas para o jantar.
* Comece o seu programa de Exercico 3.6. Acrescente uma nova linha que
mostre uma mensagem informando que você pode convidar apenas duas
pessoas para o jantar.
* Utilize pop( ) para remover os convidados de sua lista, um de cada vez, até
que apenas dois nomes permaneçam em sua lista. Sempre que remover um 
nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela
saiba que você sente muito por não poder convidá-la para o jantar.
* Apresente uma mensagem para cada uma das duas pessoas que continuam
na lista, permitindo que elas saibam que ainda estão convidadas.
* Utilize del para remover os dois últimos nomes de sua lista, de modo que você
tenha uma lista vazia. Mostre sua lista para garantir que você reamente tem
uma lista vazia no final de seu programa.'''

print()

lista_convidados = ['César', 'M. Antônio', 'Otavio', 'messalina', 'Livia', 'Cleopata']
print()
print(lista_convidados[0].title(), ", convido você para um jantar em minha casa.")
print(lista_convidados[1].title(), ", convido voce para um jantar em minha casa.")
print(lista_convidados[2].title(), ", convido voce para um jantar em minha casa.")
print(lista_convidados[3].title(), ", convido voce para um jantar em minha casa.")
print(lista_convidados[4].title(), ", convido voce para um jantar em minha casa.")
print(lista_convidados[5].title(), ", convido voce para um jantar em minha casa.\n")

print(20 * " -*- ")

print(lista_convidados[0].title(), ", encontrei uma mesa maior para o jantar, então vou convidar mais pessoas.")
print(lista_convidados[1].title(), ", encontrei uma mesa maior para o jantar, então vou convidar mais pessoas.")
print(lista_convidados[2].title(), ", encontrei uma mesa maior para o jantar, então vou convidar mais pessoas.")
print(lista_convidados[3].title(), ", encontrei uma mesa maior para o jantar, então vou convidar mais pessoas.")
print(lista_convidados[4].title(), ", encontrei uma mesa maior para o jantar, então vou convidar mais pessoas.")
print(lista_convidados[5].title(), ", encontrei uma mesa maior para o jantar, então vou convidar mais pessoas.\n")

lista_convidados.insert(0, 'escribônia')
lista_convidados.insert(3,  'mecenas')
lista_convidados.append('Fulvia')
print(lista_convidados)

print()
print("Novos convites:")
print(lista_convidados[0].title(), ", convido você para um jantar em minha casa.")
print(lista_convidados[1].title(), ", convido voce para um jantar em minha casa.")
print(lista_convidados[2].title(), ", convido voce para um jantar em minha casa.")
print(lista_convidados[3].title(), ", convido voce para um jantar em minha casa.")
print(lista_convidados[4].title(), ", convido voce para um jantar em minha casa.")
print(lista_convidados[5].title(), ", convido voce para um jantar em minha casa.")
print(lista_convidados[6].title(), ", convido voce para um jantar em minha casa.")
print(lista_convidados[7].title(), ", convido voce para um jantar em minha casa.")
print(lista_convidados[8].title(), ", convido voce para um jantar em minha casa.\n")

print(20 * " -*- ")

print()
print("Exercício 3.7: Reduzindo a lista de convidados:")
print(lista_convidados[0].title(), ", devido minha mesa não ter chegado, só poderei convidar duas pessoas para o jantar.")
print(lista_convidados[1].title(), ", devido minha mesa não ter chegado, só poderei convidar duas pessoas para o jantar.")
print(lista_convidados[2].title(), ", devido minha mesa não ter chegado, só poderei convidar duas pessoas para o jantar.")
print(lista_convidados[3].title(), ", devido minha mesa não ter chegado, só poderei convidar duas pessoas para o jantar.")
print(lista_convidados[4].title(), ", devido minha mesa não ter chegado, só poderei convidar duas pessoas para o jantar.")
print(lista_convidados[5].title(), ", devido minha mesa não ter chegado, só poderei convidar duas pessoas para o jantar.")
print(lista_convidados[6].title(), ", devido minha mesa não ter chegado, só poderei convidar duas pessoas para o jantar.")
print(lista_convidados[7].title(), ", devido minha mesa não ter chegado, só poderei convidar duas pessoas para o jantar.")
print(lista_convidados[8].title(), ", devido minha mesa não ter chegado, só poderei convidar duas pessoas para o jantar.\n")

print('Removendo nomes da lista:')
print(lista_convidados.pop(), ', lamento informar, mas vou reduzir o número de convidados do jantar.')
print(lista_convidados, "\n")
print(lista_convidados.pop(), ', lamento informar, mas vou reduzir o número de convidados do jantar.')
print(lista_convidados, "\n")
print(lista_convidados.pop(), ',lamento informar, mas vou reduzir o número de convidados do jantar.')
print(lista_convidados, "\n")
print(lista_convidados.pop(), ', lamento informar, mas vou reduzir o número de convidados do jantar.')
print(lista_convidados, "\n")
print(lista_convidados.pop(), ', lamento informar, mas vou reduzir o número de convidados do jantar.')
print(lista_convidados, "\n")
print(lista_convidados.pop(), ', lamento informar, mas vou reduzir o número de convidados do jantar.')
print(lista_convidados, "\n")
print(lista_convidados.pop(), ', lamento informar, mas vou reduzir o número de convidados do jantar.')
print(lista_convidados)

# Removendo os dois últimos elementos da lista.
del lista_convidados[0]
del lista_convidados[0]
print()
# Imprimindo a lista vazia.
print('Imprimindo a lista vazia.\nLista de convidados:', lista_convidados, '\n')