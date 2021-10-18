# Autor: Davi Costa Barroso
# Link do Minicurso:
# https://www.youtube.com/playlist?list=PL032B_GjLSupaGtbbnl7-iDt-uV4-hzYh

#Exercício 06:
# Escreva um algoritmo que receba 6 valores, 
# armazene os negativos em uma lista e
# imprima a quantidade de valores positivos.

lista = []
contar_positivos = 0
for i in range(6):
  valor = int(input("Informe valor: "))
  if valor < 0:
    lista.append(valor)
  elif valor > 0:
    contar_positivos = contar_positivos + 1
print("Lista de negativos: ", lista)
print("Quantidade de valores positivos: ", contar_positivos)