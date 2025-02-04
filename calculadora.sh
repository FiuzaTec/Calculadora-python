#!/bin/bash

echo "Bem-vindo à calculadora em shell script!"
echo "Escolha uma operação:"
echo "1 - Adição"
echo "2 - Subtração"
echo "3 - Multiplicação"
echo "4 - Divisão"
read -p "Digite o número correspondente à operação: " operacao

read -p "Digite o primeiro número: " num1
read -p "Digite o segundo número: " num2

case $operacao in
  1) resultado=$((num1 + num2))
     echo "O resultado da adição é: $resultado";;
  2) resultado=$((num1 - num2))
     echo "O resultado da subtração é: $resultado";;
  3) resultado=$((num1 * num2))
     echo "O resultado da multiplicação é: $resultado";;
  4) 
     if [ $num2 -ne 0 ]; then
       resultado=$((num1 / num2))
       echo "O resultado da divisão é: $resultado"
     else
       echo "Erro: Divisão por zero não permitida."
     fi;;
  *) echo "Operação inválida";;
esac
