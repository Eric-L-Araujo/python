
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


# função enumerate
# Às vezes é necessário saber qual o índice do objeto dentro do laço for. Para isso podemos usar a função enumerate


for indice, carro in enumerate(carros): 
     print(f"{indice}: {carro}")


# 0: gol
# 1: celta
# 2: palio
# 0: gol
# 1: celta
# 2: palio

# Filtro versão 1

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)



# Filtro versão 2

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)
print(numeros)



#Modificando valores versão 1
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)


#Modificando valores versão 2

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]

print(quadrado)



# [].clear = Limpa a lista
#  [].copy = retorna uma lista igual mas em uma nova instância 
#  [].count => Mostra quantas vezes um objeto aparece na lista.


lista.clear()










