# 28 de outubro de 2024
# Noite nublada. 23h03m
# Acrescentando elemento. Método append(): última posição.
# Acrescentando elemento. Método insert(): qualquer posição.

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')

print()
print("Acrescentando ducati na lista.")
print(motorcycles)
print()

print("Criando listas dinamicamente:")
motorcycles2 = []
motorcycles2.append('honda')
motorcycles2.append('yamaha')
motorcycles2.append('suzuki')
print(motorcycles2)
print()

print("Iserindo elementos em uma lista, em qualquer posição.")
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
print()

print("Removendo elementos com DEL.")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
print()

print("Removendo elementos com POP.")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print("Motocicleta removida:")
print(popped_motorcycles)
print()

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("the last motorcycle I owned was a " + last_owned.title() + ".")
print()