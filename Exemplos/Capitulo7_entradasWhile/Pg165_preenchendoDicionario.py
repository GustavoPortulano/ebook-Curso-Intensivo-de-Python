# 22 de novembro de 2024
# Sexta-feira, tarde nublada
# Pg 165 - Preenchendo um dicionário com dados de entrada do usuário

responses = {}

# Define uma flag para indicar que a enquete está ativa:
polling_active = True

while polling_active:
    # Pede o nome da pessoa e a resposta:
    name = str(input("\nWhat is your name? "))
    response = str(input("Which mountain would you like to climb someday? "))
    responses[name] = response
    # Descobre se outra pessoa vai responder à enquete:
    repeat = str(input("Would you like to let another person respond? (Yes/no) "))
    if repeat == 'no':
        polling_active = False 
        
    # A enquete foi concluida. Mostra os resultados:
    print("\n--- Poll results ---")
    for name, response in responses.items():
        print(name.title() + " would like to climb " + response.title() + ".")
