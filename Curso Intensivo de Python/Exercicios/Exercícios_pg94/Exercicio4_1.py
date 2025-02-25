# 01 de novembro de 2024
# Sexta-feira

'''Exercício 4.1 - Pizzas: Pense em pelo menos três tipos de pizzas favoritas. Armazene os
nomes dessas pizzas e, então, utilize um laço for para exibir o nome de cada pizza.

* Modifique seu laço for para mostrar uma frase usando o nome da pizza em 
vez de exibir apenas o nome dela. Para cada pizza, você deve ter uma linha
na saida contendo uma frase simples como Gosto de pizza de pepperoni.

* Acrescentu uma linha no final de seu programa, fora do laço for, que informe
quanto você gosta de pizza. A saida deve ser constituida de três ou mais
linhas sobre os tipos de pizza que você gosta e de uma frase adiciona, por 
exemplo, Eu realmente adoro pizza.'''

print("\n")

pizzas =['a moda', 'catupiry', 'napolitana']
print("Lista de pizzas:")
for pizza in pizzas:
    print(pizza)
    print("Eu gosto de pizza sabor " + pizza + "\n")
print("Eu gosto muito de pizza.\n")
