nome = "Eric"

# Dessa forma, definimos uma string tripla para poder formatar o texto da forma como eu desejar.
mensagem = f"""
Olá meu nome é  {nome},
Eu estou 
aprendendo 
Python
"""

segunda_mensagem = input(f"""

xxxxxxxxxxxxxxxxxx MENU xxxxxxxxxxxxxxxxxx
[1] Iniciar app
[2] Excluir app
[3] Modificar App
[4] Voltar para o início
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                Até logo <3

""")
print(segunda_mensagem)
# >>> Olá meu nome é  Eric,
# Eu estou aprendendo Python