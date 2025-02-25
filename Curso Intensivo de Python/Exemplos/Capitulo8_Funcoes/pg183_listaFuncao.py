# 25 de novembro de 2024
# Segunda-feira, noite fria
# Ida ao dentista
# Pg 182 - Passando uma lista para uma função

def greet_users(names):
    # Exibe uma saudação simples para um usuário
    for name in names: 
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannan', 'ty', 'margot', 'tostoy']
greet_users(usernames)