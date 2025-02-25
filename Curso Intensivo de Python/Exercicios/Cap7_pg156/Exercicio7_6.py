# 21 de novembro de 2024
# Quinta-feria, noite nublada

'''Exercício 7.6 - Três saidas: Escreva três versões diferentes do exercício 7.4.
* use um teste condicional na instrução while para encerrar o laço;'''

print("Primeiro exercicio")
ingrediente = ""
while ingrediente != 'quit':
    ingrediente = str(input("Digite um ingrediente. \nPara sair do programa, digite 'quit': "))
    if ingrediente != 'quit':
        print("\n" + ingrediente.title(), " acrescido(a) à sua pizza!\n")
print("Pizza finalizada.\n")

print("Segundo exercício")
'''* use uma variável active para controlar o tempo em que o laço executará,'''

active = 0

while  active <= 3:
    ingrediente = str(input("Digite um ingrediente. \nPara sair do programa, digite 'quit': "))
    print("\n" + ingrediente.title(), " acrescido(a) à sua pizza!\n")
    active += 1
print("Pizza finalizada.\n")


print("Terceiro exercício")
'''* use uma instrução break para sair do laço quando o usuário
fornecer o valor 'quit'.'''

ingrediente = ""
while ingrediente != 'quit':
    ingrediente = str(input("Digite um ingrediente. \nPara sair do programa, digite 'quit': "))
    if ingrediente != 'quit':
        print("\n" + ingrediente.title(), " acrescido(a) à sua pizza!\n")
    else:
        break
print("Pizza finalizada.\n")