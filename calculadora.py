while True:
    # Recebe dois números do usuário e os converte para float
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Exibe o menu de operações para o usuário
    print("\nEscolha uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    # Recebe a escolha do usuário
    escolha = input("Digite o número da opção desejada: ")

    # Realiza operação com base na escolha
    if escolha == "1":
        resultado = num1 + num2
        print(f"O resultado da soma é: {resultado}")
    elif escolha == "2":
        resultado = num1 - num2
        print(f"O resultado da subtração é: {resultado}")
    elif escolha == "3":
        resultado = num1 * num2
        print(f"O resultado da multiplicação é: {resultado}")
    elif escolha == "4":
        if num2 != 0:  # Verifica se o segundo número é diferente de zero
            resultado = num1 / num2
            print(f"O resultado da divisão é: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida!")
    elif escolha == "5":  # Encerra o programa
        print("Saindo do programa. Até mais!")
        break
    else:  # Caso o usuário digite uma opção inválida
        print("Opção inválida. Tente novamente.")

    print("\n")  # Adiciona uma linha em branco para melhorar a legibilidade
