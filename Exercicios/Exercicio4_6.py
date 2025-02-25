# 02 de novembro de 2024
# Sábado, noite nublada

'''Exercício 4.6 - Números ímpares: Use o terceiro argumento da função range() para criar
uma lista de números ímpares de 1 a 20. Utilize o laço for para exibir todos os números.'''

print()
print("Lista de números ímpares.")
impares = []
for nr in range(1, 20, 2):
    impares.append(nr)
print(impares)