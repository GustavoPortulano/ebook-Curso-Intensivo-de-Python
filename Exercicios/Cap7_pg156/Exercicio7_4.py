# 21 de novembro de 2024
# Quinta-feira, noite nublada

'''Exercício 7.4 - Ingredientes para uma pizza: Escreva um laço que peça ao usuário para 
fornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja
fornecido. À medida que cada ingrediente é especificado, apredente uma
mensagem informando que você acrescentará esse ingrediente à pizza.'''

ingrediente = ""
while ingrediente != 'quit':
    ingrediente = str(input("Digite um ingrediente. \nPara sair do programa, digite 'quit': "))
    if ingrediente != 'quit':
        print("\n" + ingrediente.title(), " acrescido(a) à sua pizza!\n")
print("Pizza finalizada.\n")