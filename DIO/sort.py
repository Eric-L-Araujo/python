# sort = ordena a lista. reordena alfabeticamente, se é string.
# atributo (reverse = true) = ordena de tras para frente

# atributo (key=lambda x: len(x), reverse = true ) = para cada item, execute esse código . Serve para informar o tamanho da string e ordena o tamanho de cada item de forma crescente.


linguagens = ["python", "js", "c", "java"]

linguagens.sort(key=lambda x: len(x), reverse=True)

print(linguagens)


# sorted = ordena iteráveis, igual o sort.

sorted(linguagens, key=lambda x: len(x))

print(sorted(linguagens))