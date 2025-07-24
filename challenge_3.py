# Mensagem de boas-vindas
enter = "Bem-vindo ao Banco Clark!"
LENGTH = 43 

print()
print(enter.center(LENGTH))

# Menu de opções traduzido
menu = """
    ===================================
                   MENU
    -----------------------------------
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Sair
    ===================================

=> """

balance = 0
limit = 500
extract = ""
number_of_withdrawals = 0
WITHDRAWAL_LIMIT = 3


while True:

    option = input(menu)

    if option == "1":
        try:
            value = float(input("Informe o valor do depósito: "))

            if value > 0:
                balance += value
                extract += f"Depósito: R$ {value:.2f}\n"
                print()
                print("Depósito realizado com sucesso!".center(LENGTH))
        
            else:
                print()
                print("Operação falhou! O valor informado é inválido.".center(LENGTH))

        except ValueError:
            print()
            print("Entrada inválida. Por favor, digite um número.".center(LENGTH))
            print("Selecione o serviço novamente.".center(LENGTH))

    elif option == "2":
        try: 
            value = float(input("Informe o valor do saque: "))
        
            exceeded_the_balance = value > balance 
            exceeded_the_withdrawal = value > limit 
            exceeded_the_extract = number_of_withdrawals >= WITHDRAWAL_LIMIT

            if value <= 0:
                print()
                print("Operação falhou! O valor do saque deve ser positivo.".center(LENGTH))

            elif exceeded_the_balance:
                print()
                print("Operação falhou! Você não tem saldo suficiente.".center(LENGTH))
        
            elif exceeded_the_withdrawal:
                print()
                print("Operação falhou! O valor do saque excede o limite.".center(LENGTH))
        
            elif exceeded_the_extract:
                print()
                print("Operação falhou! Número máximo de saques excedido.".center(LENGTH))

            elif balance > 0:
                balance -= value
                extract += f"Saque:    R$ {value:.2f}\n"
                number_of_withdrawals += 1
                print()
                print("Saque realizado com sucesso!".center(LENGTH))

            else:
                # Caso o valor seja válido mas o saldo seja 0
                print()
                print("Operação falhou! Saldo insuficiente.".center(LENGTH))

        except ValueError:
            print()
            print("Entrada inválida. Por favor, digite um número.".center(LENGTH))
            print("Selecione o serviço novamente.".center(LENGTH))
    
    elif option == "3":
        print()
        print("Exibindo extrato...".center(LENGTH))
        print()
        print("=" * LENGTH)
        print("EXTRATO".center(LENGTH))
        print("-" * LENGTH)

        if not extract:
            print()
            print("Não foram realizadas movimentações.".center(LENGTH))
        else:
            print(extract, end="")

        balance_text = f"Saldo: R$ {balance:.2f}"
        print()
        print(balance_text.rjust(LENGTH))
        print("=" * LENGTH)
        print()
        print("Selecione o próximo serviço que deseja utilizar.".center(LENGTH))
        
    elif option == "4":
        print()
        print("Obrigado por ser cliente do Banco Clark!".center(LENGTH))
        print()
        break

    else:
        print()
        print("Operação inválida, por favor selecione novamente a operação desejada.".center(LENGTH))
