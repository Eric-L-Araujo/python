
# A lista é uma sequência, portanto, podemos acessar seus dados utilizando índices. Contamos o índice de determinada sequência a partir do zero.
# -1: pega o último item da lista
# -2: pega o penúltimo item da lista
# -3: pega o antepenúltimo
frutas = ["laranja", "maçã", "uva", "pera", "banana"]

print(frutas[-3])

# Cada letra da palavra python é um valor dentro da lista
letras = list("python")


print(letras[0])

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][1])
print(matriz[1])
print(matriz[2])

# Fatiamento, exemplo:

lista = ['p', 'y', 't', 'h', 'o', 'n']

print(lista[2:])
#  ['t', 'h', 'o', 'n']

print(lista[:2])
#  ['p', 'y']

print(lista[1:3])
#  ['y', 't']

print(lista[0:3:2])
# ['p', 't']

print(lista[::])
#  ['p', 'y', 't', 'h', 'o', 'n']

print(lista[::-1])
# Invertido
#  ['p', 'y', 't', 'h', 'o', 'n']


# Iterar listas

# carros = ["gol", "celta", "palio"]

# for carro in carros:
#      print(carro)

carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
     print(f"{indice}: {carro}")

# 0: gol
# 1: celta
# 2: palio


