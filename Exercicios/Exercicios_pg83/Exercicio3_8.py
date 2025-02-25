# 31 de outubro de 2024
# Quinta-feira. Noite normal. 23h37min
# Exibindo uma lista em ordem inversa

'''3.8 _ Conhecendo o mundo: Pense em pelo menos cinco lugares do mundo em que
você gostaria de visitar.
* Armazene as localidades em uma lista. Certifique-se de que a lista não esteja
em ordem alfabética.

* Exiba sua lista na ordem original. Não se preocupe em exibir a lista de forma
elegante; basta exibi-la como uma lista Python pura.

* utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a
lista propriamente dita.

* Utilize sorted() para exibir sualista em ordem alfabética inversa sem alterar
a ordem da lista original.

* Mostre que sua lista manteve sua ordem original exibindo-a novamente.

* Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar
que sua ordem mudou.

* Utilize reverse() par amudar a ordem de sua lista novamente. Exiba a lista
para mostrar que ela voltou à sua ordem original.

* Utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem alfabética.
Exiba a lista para mostar que sua ordem mudou.

* Utilize sort() para mudar sua list ade modo que ela seja armazenada em
ordem alfabética inversa. Exiba a lista para mostrar que sua ordem mudou.''' 

print()
lugares = ['namíbia', 'tibet', 'china', 'india', 'amazonas']
print("Exibindo a lista original:")
print(lugares)

print(20 * " = ", "\n")

print("Exibindo a lista em ordem alfabética:")
print(sorted(lugares))
print("Lista original:")
print(lugares, "\n")

print(20 * " = ")

print("Lista em ordem reversa.")
lugares.reverse()
print(lugares)
print("Restaurando a lista.")
lugares.reverse()
print(lugares)

print(20 * " = ")

print("Exibindo a lista em ordem alfabética.")
print(lugares)
lugares.sort()
print(lugares)

print(20 * " = ")

print("Ordem alfabética inversa.")
lugares.sort(reverse=True)
print(lugares)
print()
