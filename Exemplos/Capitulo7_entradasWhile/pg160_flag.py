# 21 de novembro de 2024
# Quinta-feira, noite nublada
# Pg 160 - Usando uma flag

prompt = "\nTell me something, and I wil repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
print("Programa encerrado.")
