# 23 de novembro de 2024
# Sabado, noite nublada. 
# Visita de Samuel
# Capítulo 8: Funções
# Pg 178 - arguemento opcional

print()
def get_formatted_name(first_name, middle_name, last_name):
    # Devolve um nome completo formatado de modo elegante.
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

print()

# Deixando um parâmetro opcional:

def get_formated_name(first_name, last_name, middle_name=''):
    # Devolve um nome completo formatado de modo elegante.
    # Permite escrever ou omitir o nome do meio.
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

print("Omitindo o nome do meio.")
musician = get_formated_name('jimi', 'hendrix',)
print(musician)
print("Registrando o nome do meio.")
musician = get_formated_name('john', 'hooker', 'lee')
print(musician)