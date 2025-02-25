# 21 de novembro de 2024
# Quinta-feira, noite nublada
# Decidindo quando o usuário quer sair

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
print("\nFim do programa!")