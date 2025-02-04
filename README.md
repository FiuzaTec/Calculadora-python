# Calculadora-python
Calculadora simples
Este é um projeto simples de calculadora interativa escrita em Python. O programa permite realizar operações matemáticas básicas como soma, subtração, multiplicação e divisão de dois números fornecidos pelo usuário.

##Funcionalidades:
   Soma dois números.

   Subtrai dois números.

   Multiplica dois números.

   Divide dois números (com validação para evitar divisão por zero).

   Permite encerrar o programa de forma interativa.

##Como usar
   Clone o repositório ou baixe o arquivo Python para sua máquina:

git clone https://github.com/FiuzaTec/Calculadora-python.git
cd calculadora.py

## Exemplos de Uso

O programa solicita que você insira dois números e escolha uma operação. Abaixo está um exemplo de como o usuário deve interagir com o sistema:

# Exemplo 1: Soma
Digite o primeiro número: 10
Digite o segundo número: 5

Escolha uma operação:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão
5. Sair
Digite o número da opção desejada: 1

O resultado da soma é: 15.0

## Validações

-Divisão por zero: O programa verifica se o segundo número inserido para a operação de divisão é zero. Caso o usuário tente dividir por zero, o programa exibe uma mensagem de erro e pede que uma nova operação seja escolhida.
  
-Entrada de opção inválida: Caso o usuário insira um número de opção que não existe (por exemplo, digitando um número que não está listado no menu), o programa solicita que ele tente novamente e escolha uma opção válida.

-Entrada de número inválido: Se o usuário inserir algo que não seja um número ao solicitar os números para a operação, o programa gerará um erro e pedirá que o usuário insira novamente os números.

## Requisitos

-Python 3.x ou superior: O programa foi desenvolvido e testado utilizando o Python 3.x.
- Nenhuma biblioteca externa necessária*: O programa não requer bibliotecas externas, pois todas as operações são feitas com funções nativas do Python.

## Contribuições

Contribuições são bem-vindas! Se você tiver sugestões ou melhorias para este projeto, siga os passos abaixo:

1. *Faça um fork* deste repositório.

2. Explicação do Código em Python

O código calculadora.py é um programa interativo que permite ao usuário realizar operações matemáticas básicas. Ele funciona da seguinte maneira:

1. Solicita ao usuário dois números.


2. Exibe um menu de opções com as operações disponíveis.


3. O usuário escolhe uma operação (soma, subtração, multiplicação, divisão ou sair).


4. O programa executa a operação escolhida e exibe o resultado.


5. O processo se repete até que o usuário escolha sair.



##Estrutura do Código

O código está estruturado assim:

1. Loop Infinito (while True)

O programa usa um loop infinito para permitir que o usuário realize várias operações sem precisar reiniciar o programa manualmente. O loop só para quando o usuário escolhe a opção de sair.

while True:

2. Entrada de Dados

O programa solicita que o usuário digite dois números. Esses valores são convertidos para float para permitir cálculos com números decimais.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

3. Exibição do Menu de Operações

O menu apresenta cinco opções: soma, subtração, multiplicação, divisão e sair.

print("\nEscolha uma operação:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Sair")

4. Captura da Escolha do Usuário

O usuário escolhe uma das opções digitando um número correspondente.

escolha = input("Digite o número da opção desejada: ")

5. Estrutura de Condições (if e elif)

Dependendo da escolha do usuário, o programa executa a operação correspondente.

5.1. Soma

if escolha == "1":
    resultado = num1 + num2
    print(f"O resultado da soma é: {resultado}")

5.2. Subtração

elif escolha == "2":
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado}")

5.3. Multiplicação

elif escolha == "3":
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")

5.4. Divisão (com validação para evitar erro de divisão por zero)

Se o usuário tentar dividir por zero, o programa exibe uma mensagem de erro.

elif escolha == "4":
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida!")

5.5. Opção de Sair

Se o usuário escolher a opção "5", o programa exibe uma mensagem de despedida e encerra o loop com break.

elif escolha == "5":
    print("Saindo do programa. Até mais!")
    break

5.6. Opção Inválida

Se o usuário digitar um número que não está no menu, o programa exibe uma mensagem de erro e pede uma nova escolha.

else:
    print("Opção inválida. Tente novamente.")


---

Conclusão

Este código é um exemplo simples de interação com o usuário em Python, usando entradas de dados, estrutura condicional (if/elif/else) e um loop while True para manter a execução contínua até que o usuário decida sair.
