# Interpolação de strings

nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"
saldo = 7899.89078

# old format
print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

# utilizando format
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}." .format(nome, idade, profissao, linguagem))

# format com indices
print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}." .format (linguagem, profissao, idade, nome))


# Com nomeação das variáveis
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format (nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

# Com f-string
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}. Saldo: {saldo:.2F}")