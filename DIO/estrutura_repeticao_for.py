# Exemplos utilizando o iterável

texto = input('Informe o texto: ')
VOGAIS = 'AEIOU'

for letras in texto:
	if letras.upper() in VOGAIS:
		print(letras, end='')

else:
	print("\nExecuta no final do laço")


# range (stop)  -> range object
# range(start, stop[,step]) -> range object

list (range(0, 4))

# Exemplos utilizando o iterável
for numero in range(0, 11):
	print(numero, end= " ")


# Exibindo a tabuada do 5
for numero in range(0, 31, 3):
	print(numero, end = " ")
	
