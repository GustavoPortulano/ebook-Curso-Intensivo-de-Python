# 26 de novembro de 2024
# Terça-feira, noite fria
# Ida a Lagoa Santa ao encontro de corretores para a venda da casa
# Pg183 - Modificando uma lista em uma função

# Modificando a lista sem o uso de uma função:
# Começa com alguns designs que devem ser impressos:
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simula a impressão de cada design, até que não haja mais nenhum.
# Transfere cada design para completed_models após a impressão 

while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Simula a criação de uma impressão 3D a partir do design
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Exibe todos os modelos finalizados
print("\nThe following models have been printed:")
print(29 * '-')
for completed_model in completed_models:
    print(completed_model)
print(29 * '-')
print("Fim do processo de impressão.\n")