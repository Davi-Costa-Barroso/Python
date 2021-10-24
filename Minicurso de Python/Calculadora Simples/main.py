# Autor: Davi Costa Barroso
# Link do Minicurso:
# https://www.youtube.com/playlist?list=PL032B_GjLSupaGtbbnl7-iDt-uV4-hzYh

# Calculadora Simples:
# Faça uma função para cada operação matemática 
# (Adição, subtração, multiplicação, divisão e raiz quadrada). 
# O usuário escolherá qual opção deseja fazer a partir de um menu. 
# O programa encerra quando é escolhido a opção “sair” no menu.

import calculadora
opcao = 0
while opcao != 6:
  print("1 - Adição")
  print("2 - Subtração")
  print("3 - Multiplicação")
  print("4 - Divisão")
  print("5 - Raiz quadrada")
  print("6 - Encerrar programa")
  opcao = int(input("Digite opção: "))
  if opcao == 1:
    print(calculadora.soma())
  elif opcao == 2:
    print(calculadora.subtracao())
  elif opcao == 3:
    print(calculadora.multiplicacao())
  elif opcao == 4:
    print(calculadora.divisao())
  elif opcao == 5:
    print(calculadora.raiz())
  else:
    print("Opção invalida")
