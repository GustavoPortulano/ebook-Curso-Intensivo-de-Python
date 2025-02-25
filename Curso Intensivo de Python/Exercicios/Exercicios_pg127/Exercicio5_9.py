# 08 de novembro de 2024
# Sexta-feira. Noite nublada

'''Exercício 5.9 - Sem usuários: Acrescente um teste if em hello_admin.py para garantir
que a lista de usuários não esteja vazia.
* Se a lista estiver vazia, mostre a mensagem Precisamos encontrar alguns usuários.
* Remova todos os nomes de usuários de sua lista e certifique-se de que a 
mensagem correta seja exibida.'''

print()

usuarios =['ana', 'bela', 'cintia', 'denize', 'erica', 'admin']
# Removendo todos os elementos de uma lista. Método clear()
usuarios.clear()

if usuarios:
    for usuario in usuarios:
        print("Olá", usuario.title())
else:
    print("A lista de usuários está vazia.")
    print("Precisamos de encontrar novos usuários.\n")



