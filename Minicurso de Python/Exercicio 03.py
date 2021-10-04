# Autor: Davi Costa Barroso
# Link do Minicurso:
# https://www.youtube.com/playlist?list=PL032B_GjLSupaGtbbnl7-iDt-uV4-hzYh

#Exercício 03:
#Faça um programa que receba um valor inteiro e 
#informe se o valor digitado é positivo, negativo ou neutro.

valor = int(input("Informe valor inteiro: "))
if valor == 0:
  print("Esse valor é negativo.")
elif valor < 0:
  print("Esse valor é negativo.")
else:
  print("Esse valor é positivo")