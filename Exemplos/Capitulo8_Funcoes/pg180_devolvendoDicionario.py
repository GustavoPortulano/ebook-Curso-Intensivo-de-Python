# 24 de novembro de 2024
# Domingo, noite fria, ida à Igreja
# Pg 180 - Devolvendo um dicionário

def build_person(first_name, last_name):
    # Devolve um dicionário com informações sobre uma pessoa.
    person = {'first':first_name, 'last':last_name}
    return person
musician = build_person('jimi','hendrix')
print("\nDevolvendo o dicionário através de uma função:")
print(musician, "\n")

print()
print("Alteração que permite armazenar uma informação opcional,",
      "\nno caso, a idade de uma pessoa:\n")

def build_person(first_name, last_name, age=''):
    # Devolve um diconário com informações de uma pessoa:
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician, "\n")