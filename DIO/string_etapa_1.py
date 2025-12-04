nome = "eRiC"
# Deixa string com letras maiúsculas
print(nome.upper())

# Deixa string com letras minúsculas
print(nome.lower())

# Deixa primeira letra da string em maiúscula e o restante em minúscula.
print(nome.title())



texto = "          Que vida boa!             "
# Remove espaços de strings
print(texto.strip())

# Remove espaços à esquerda
print(texto.lstrip())

# Remove espaços à direita
print(texto.rstrip())

menu = "Python"
print(menu.center(15)) 
# print(menu.center(15, "--")) 

print("-".join(menu))