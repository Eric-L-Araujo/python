opcao = int(input("Informe uma opção: \n[1] Sacar \n[2] Extrato:"))

if opcao == 1:
	valor = float(input("Informe a quantia para o saque: "))
	print(f"Valor de R${valor} sacado \nObrigado pela preferência!")

elif  opcao == 2:
	print("Exibindo extrato…")

else: 
   SystemError.exit("Opção inválida")
	
