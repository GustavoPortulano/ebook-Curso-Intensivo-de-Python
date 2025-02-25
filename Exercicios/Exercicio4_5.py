# 02 de novembro de 2024
# Sábado. Noite nublada

'''Exercicio 4.5 - Somando um milhão: Crie uma lista de números de um até um milhão e, 
em seguida, use min() e max() para garantir que a sua list realmente começa em um e 
termina em um milhão. Além disso, utilize a função sum().'''

print()
print("Lista de números de um a 100.")

lista = []
for nr in range(1, 101):
    lista.append(nr)
print(lista)
print()
print("Menor número da lista: ", min(lista))
print("Maior número da lista: ", max(lista))
print("Soma dos números da lista: ", sum(lista))