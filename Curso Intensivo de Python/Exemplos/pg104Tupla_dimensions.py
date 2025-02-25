# 03 de novembro de 2024
# Domingo. Tarde nublada
# Sobrescrevendo uma tupla

dimensions = (200, 50)
print()
print("Original dimensions: ")
# Laço for
for dimension in dimensions:
    print(dimension)
print("Exibindo a tupla criada:")
print(dimensions)

print("Sobrescrevendo novos valores:")
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)