nome = "Guilherme Arthur de Carvalho"

print(nome[0])
# >>>G

# Exibir do inicio até a posição 9 do índice
print(nome[:9])
# >>> Gulherme

# Exibir do inicio até o final do índice
print(nome[10:])
# >>> Arthur de carvalho

# Exibe o que está no intervalo entre 10 e 16 do índice.
print(nome[10:16])
# >>> Arthur

# Exibe o que está no intervalo entre 10 e 16 do índice, mas pulando 2 "passos".
print(nome[10:16:2])
# >>> Atu

# Exibe uma cópia da string
print(nome[:])
# >>> Guilherme Arthur de carvalho

# Espelha toda a string: Sem start, sem stop e passar o step como -1. faz criar uma cópia da string, só que invertido.
print(nome[:: -1])
# >>> ohlavraC ed ruhtrA emrehliuG


