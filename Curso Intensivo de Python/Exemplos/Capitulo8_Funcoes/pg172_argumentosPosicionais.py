# 23 de novembro de 2024
# Sabado, madrugada nublada. 
# Visita das irmãs da igreja
# Capítulo 8: Funções
# Pg 171: Argumentos posicionais

def describe_pet(animal_type, pet_name):
    '''Exibe informações sobre um animal de estimação.'''
    print("\nI have a  " + animal_type + " .")
    print("My " + animal_type + " 's name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')

# Pg 172: Várias chamadas de função.
describe_pet('dog', 'willie')

print("\n")

