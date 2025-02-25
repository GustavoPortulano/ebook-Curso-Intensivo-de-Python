# 24 de novembro de 2024
# Domingo, noite fria, ida à Igreja
# Pg 180 - Devolvendo um dicionário

def get_formatted_name(first_name, last_name):
    # Devolve um nome completo formatado de modo elegante.
    full_name = first_name + ' ' + last_name
    return full_name.title()

# Usando a instrução break para sair do loop infinito.

while True:
    print("\nPlease tell me your name:")
    print("Enter 'q' at any time to quit.")
    f_name = input("First name: ")
    if f_name == 'q': break
    l_name = input("Last name: ")
    if l_name == 'q': break
    formated_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formated_name + "!")
    
print("q (sair). Fim do programa\n")