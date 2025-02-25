# 08 de novembro de 2024
# Sexta-feria. Noite nublada

'''Exercício 5.10: Verificando nomes de usuários. Faça o seguinte para criar um programa
que simule o modo como os sites garantem que todos tenham um nome de
usuário único. 
* Crie uma lista chamada currente_users com cinco ou mais nomes de usuários.
* Crie outra lista chamada new_users com cinco nomes de usuários. Garanta
que um ou dois dos novos usuários também estejam na lista current_users.
* Percorra a lista new_users com um laço para ver se cada novo nome de usuário
já foi usado. Em caso afirmativo, moste uma mensagem informando que 
a pessoa deverá fornecer um novo nome. Se um mome de usuário não foi
usado, apresente uma mensagem dizendo que o nome do usuário está disponível.
* Certifique-se de que sua comparação nãolevará em conta as diferenças 
entre letras maiúsculas e minúsculas. Se 'John' foi usado, 'JOnH' não 
deverá ser aceito.'''

print()
# Criando a 1ª lista com letras minúsculas
current_users = []
current_users.append('marco'.lower())
current_users.append('antônio'.lower())
current_users.append('aurélio'.lower())
current_users.append('CESAR'.lower())
current_users.append('Bruto'.lower())
current_users.append('AGRipa'.lower())

# Criando a segunda lista em minúsculas
print()
# Criando a 1ª lista com letras minúsculas
new_users = []
new_users.append('jULIA'.lower())
new_users.append('EscribônIA'.lower())
new_users.append('Livila'.lower())
new_users.append('cesar'.lower())
new_users.append('CleopatrA'.lower())
new_users.append('Marco'.lower())

print("Lista de usuários:")
print(current_users)
print(new_users)

print("\n")

for new_user in new_users:
    if new_user in current_users:
        print(new_user.title(),", bem vindo(a). Lamentamos mas seu nome não está disponível.")
        print("Solicitamos que registre outro nome de usuário.\n")
    else:
        print(new_user.title(),", bem vindo(a). Seu nome está disponível.\n")