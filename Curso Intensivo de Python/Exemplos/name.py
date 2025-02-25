# 25 de outubro de 2024

#Pg 53: Mudando para letras maiúsculas e minúsculas usando métodos

print()

name = "ada lovelace"
print(name.title())     # Primeiras letras maiúsculas
print(name.upper())     # Todas as letras maiúsculas
print(name.lower())     # Todas as letras minúsculas

print()

# 26 de outubro de 2024
# Pg 57 - Combinando ou concatenando strings
print("Pg 57 - Combinando ou concatenando strings")

print("Exemplo 1")
first_name = "ada"
last_name = "lovelace"

full_name = first_name + " " + last_name
print(full_name)
print()

print("Exemplo 2")
first_name = "ada"
last_name = "lovelace"
message = "Hello, " + full_name.title() + "!"
print(message)
print()

# Pg 58 - Acrescentando espaços em branco em strings com tabulações ou quebras de linha.
print("Pg 58 - Acrescentando espaços em branco em strings com tabulações ou quebras de linha")
print("Python")     # Saida de texto normal
print("\tPython")   # Saida de texto com tabulação
print("Languages:\n\tPython\n\tJavaScript")     # Saida com quebra de linhas e tabulações
print()

# Pg 58 - Removendo espaços em branco.
print("Removendo espaços em branco.")
# rstrip(): elimina espaços em brando à direita do texto
favorite_language = "python "
print(favorite_language)
print(favorite_language.rstrip())
print()

print("Removendo espaços à esquerda e no interior do texto.")
favorite_language = " python "
print(favorite_language.rstrip())       # Removendo espaço à esquerda
print(favorite_language.lstrip())       # Removendo espaço à direira
print(favorite_language.strip())        # Removoendo espaco ao centro

print("\n")

print("Você é chato")
