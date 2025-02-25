# 18 de novembro de 2024
# Segunda-feira, noite normal

'''Exercício 6.4 - Glossário 2: Agora que você sabe como percorrer um dicionário com
um laço, limpe o código do Exercício 6.3, substituindo sua
sequência de instruções print por um laço que percorra as chaves e os valores
do dicionário. Quando tiver certeza de que seu laço funciona, acrescente mais
cinco termos de Python ao seu glossário. Ao executar seu programa novamente,
essas palavras e significados novos deverão ser automaticamente incuidos
na saida.'''

print("\nExercício 6.4")

glossario = {'false':'valor booleano de falso',
             'true':'valor booleano de verdadeiro',
             'none':'ausência de um valor',
             'if':'estrutura condicional SE',
             'not':'inverte o valor booleano de uma expressão',
             'and':'analisa duas condições simultaneamente, retornando verdadeiro se ambas forem verdadeiras',
             'or':'analisa várias condições e retorna verdadeiro de uma for verdadeira',
             'else':'define um bloco de código se as condições anteriores forem falsas',
             'elif':'usada após uma instrução if caso a primeira opão não for verdadeira',
             'is':'operador de comparação que verifica se duas variáveis referenciam o mesmo objeto na memória'}

print("Exibindo o dicionário sem um laço:")
print(glossario)
print("\n")

print("Exibindo o dicionário com um laço usando o método items():")

for key, value in glossario.items():
    print(key.upper() +  ":", value + ".")

    