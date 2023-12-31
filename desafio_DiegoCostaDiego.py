menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == '1':
        valor = float(input("Infome o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\nDeposito de R$ {valor:.2f} realizado.")
            print(f"\nSaldo em conta R${saldo:.2f}")
            

        else:
            print("Operação falhou! O valor informado é invalido.")
    
    elif opcao == '2':
        valor = float(input("Informe o valor do saque:"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! Valor limite de saque excedido.")

        elif excedeu_saques:
            print(" Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"\nSaque de R${valor:.2f} realizado.")
            print(f"\nSaldo em conta R$ {saldo:.2f}")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == '3':
       print("\n=============== EXTRATO ================")
       print("Não foram realizadas movimentações." if not extrato else extrato)
       print(f"\nSaldo: R$ {saldo:.2f}")
       print("=======================================")

    elif opcao == '0':
        print("\nObrigado por utilizar nossos serviços!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

