# 23 de novembro de 2024
# Sabado, noite nublada. 
# Visita de Samuel
# Capítulo 8: Funções
# Pg 178 - devolvendo um valor simples

print()
def get_formatted_name(first_name, last_name):
    # Devolve um nome completo formatado de modo elegante.
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')

print("Nome formatado: ")
print(musician)
