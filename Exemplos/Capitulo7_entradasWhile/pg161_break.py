# 21 de novembro de 2024
# Quinta-feira, noite nublada
# Pg 160: Usando break para sair de um laço

prompt = "\nPlease ente the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + ".")
print("\nPrograma encerrado.")