# 01 de novembro de 2024
# Sexta-feira

'''Exercicio 4.2 - Animais: Pense em pelo menos três animais diferenes que tenham uma
característica em comum. Armazene os nomes desses animais em uma lista e,
então, utilize um laço for para exibir o nome de cada animal.

* Modifique seu programa para exibir uma frase sobre cada animal, por
exemplo, Um cachorro seria um ótimo animal de estimação.

* Acrescente uma linha no final de sue programa informando o que esses 
animais têm em comum. Você poderia exibir uma frase como Qualquer um 
desses animais seria um ótimo animal de estimação.'''

animais = ['gato', 'onça', 'tigre']

print("Lista de animais:")
for animal in animais:
    print(animal)
print()

for animal in animais:
    print("O ", animal, " é um felino e é carnivoro.")
print("Dos animais listados, apenas o gato é um animal doméstico.\n")