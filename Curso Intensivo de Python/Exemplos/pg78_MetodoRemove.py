# 30 de outubro de 2024
# Noite normal 22h34m
# Removendo um item de acordo com o valor
# Método remove( )

# Removendo o valor ducati
print()
print("Removendo o valor ducati:")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

print()

motorcycles.remove('ducati')
print(motorcycles)
print()

# Removendo com um texto explicativo.

print(10 * " *-* ")
print()
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

print("Removendo com uma explicação:")
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

print()