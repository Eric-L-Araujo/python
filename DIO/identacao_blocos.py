def sacar(valor):

   saldo = 500

   if saldo >= valor:
      print('Valor sacado')
   else:
      print('Saldo insuficiente')
   print('Seja bem-vindo(a)!')


def depositar(valor):
   saldo = 500
   print('Saldo anterior:' ,saldo)
   saldo += valor
   print('O valor de ' ,valor, 'foi depositado na sua conta')
   print('Seu saldo total é de R$' ,saldo)

 
depositar(10)
