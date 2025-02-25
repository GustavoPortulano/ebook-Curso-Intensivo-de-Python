# 30 de outubro de 2024
# Quarta-feira, noite normal. 23h06min
# Mais convidados

'''Você acabou de encontrar uma mesa de jantar maior,
portanto agora tem mais espaço disponível. Pense em mais três convidados
para o jantar.
* Comece com seu programa do Exercício 3.4 ou do Exercicio 3.5. Acrescente
uma intrução print no final de seu programa informando às pessoas que 
você encontrou uma mesa de jantar maior.
* Utilize insert( ) para adicionar um novo convidade no início de sua lista.
* Utilize insert( ) para adicionar um novo convidado no meio de sua lista.
* Utilize append( ) para adicionar um novo convidado no final de sua lista.
* Exiba um novo conjunto de mensagens de convite, uma para cada pessoa
que está em sua lista.'''

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

