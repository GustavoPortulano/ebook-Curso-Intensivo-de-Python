# 22 de novembro de 2024
# Sexta-feira, dia chuvoso
# Pg 164 - Transferindo de uma lista para outra

'''Considere umna lista de usuários recèm-registrados em um site, porém
não verificados. Depois de confeir esses usuários, como podemos transferi-los
para uma lista separada de usuários confirmados? Uma 
maneira seria usar um laço while para extrair os usuários da lista de
usuários não confirmados à medida que os veirficarmos e então
adicioná-los em uma lista separada de usuários confirmados.'''


# Começa com os usuários que precisam ser confirmados
# e com uma lista vazia para armazenar os usuários confirmados.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

print(unconfirmed_users)

# Verifica cada usuário até que não haja mais usuários não confirmados. 
# Transfere cada usuário verificado para a lista de usuários confirmados.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("\nVerifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Exibe todos os usuários confirmados.
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
