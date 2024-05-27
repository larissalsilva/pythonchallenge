menu = """

1- Depositar
2- Sacar
3- Extrato
4- Sair

=> """

saldo = 0
limite = 500
extrato = ""
qntd_saque = 0
lmt_saque = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Valor inválido, tente novamente.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        exc_saldo = valor > saldo

        exc_limite = valor > limite

        exc_saque = qntd_saque >= lmt_saque

        if exc_saldo:
            print("Saldo insuficiente! Tente novamente.")

        elif exc_limite:
            print("Valor do saque maior que o limite! Tente novamente.")

        elif exc_saque:
            print("Você utilizou todos seus saques! Tente novamente amanhã.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            qntd_saque += 1

        else:
            print("Valor inválido! Tente novamente.")

    elif opcao == "3":
        print("\n============ EXTRATO ============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==================================")

    elif opcao == "4":
        break

    else:
        print("Selecione uma opção válida do menu.")