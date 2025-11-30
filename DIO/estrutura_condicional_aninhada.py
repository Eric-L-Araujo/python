conta_normal = True
conta_universitaria = True

cheque_especial = 788
saldo = 2000
saque = 350


if conta_normal:
	if saldo >= saque:
		print('Saque realizado com sucesso!')
	elif saque <= (saldo + cheque_especial): 
		print('Saque realizado com o uso do cheque especial!')


if conta_universitaria:
   if saldo >= saque:
      print('Saque realizado com sucesso!')
   else: 
      print('Saldo insuficiente')
