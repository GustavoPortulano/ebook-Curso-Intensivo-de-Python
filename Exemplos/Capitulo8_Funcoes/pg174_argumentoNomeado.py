# 23 de novembro de 2024
# Sabado, noite nublada. 
# Visita de Samuel, namorado de Bianca
# Capítulo 8: Funções
# Pg 174: Argumentos nomeados

def describe_pet(animal_type, pet_name):
    '''Exibe informações sobre um animal de estimação.'''
    print("\nI have a  " + animal_type + " .")
    print("My " + animal_type + " 's name is " + pet_name.title() + ".")
    # Cada parâmetro pertence a seu correto argumento
describe_pet(animal_type='hamster', pet_name='harry')

print("\n")