total = 10
print(total)

total = float(total)
print(total)

#media de notas alunos

nome = input("Qual é o seu nome? ")
primeira_nota = float(input("Valor da nota 1: "))
segunda_nota = float(input("Valor da nota 2: "))

media_notas = primeira_nota + segunda_nota / 2


if primeira_nota and segunda_nota != "": {
    print(f"A média de suas notas é: {media_notas}")
   
}
else: {
    print("Não foi possível calcular sua média")
}
   






