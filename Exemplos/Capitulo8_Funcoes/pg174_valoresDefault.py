# 23 de novembro de 2024
# Sabado, noite nublada. 
# Visita de Samuel
# Capítulo 8: Funções
# Pg 174: Valores default

def describe_pet(pet_name, animal_type='dog'):
    # Exibe informações sobre um animal de estimação
    # animal_type está com um valor default
    print("\nI have a ", animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title())
describe_pet(pet_name='willie')
describe_pet(pet_name='fremem')
describe_pet('spike henrique')
describe_pet(pet_name='harry', animal_type='mouse')


    