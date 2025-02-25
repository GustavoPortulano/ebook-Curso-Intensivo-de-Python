# 22 de novembro de 2024
# Sexta-feira, dia nublado
# Pg 165 - Removendo todas as instâncias de valores específicos de uma lista.

pets = ['dog','cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print("A lista contem", len(pets), " elementos.")
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print("A lista contem", len(pets), " elementos.")   
print(pets)

