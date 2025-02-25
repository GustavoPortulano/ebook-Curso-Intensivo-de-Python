# 01 de novembro de 2024
# Sexta-feira
# Usando range() para criar uma lista de números

print("\n")
print("Criando uma lista de números:")
numbers = list(range(1, 6))
print(numbers, "\n")


print("Números pares entre 1 e 10:")
numeros_pares = list(range(2,11,2))
print(numeros_pares, "\n")

print("Lista dos 10 primeiros quadrados perfeitos:")
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)
print("\n")

