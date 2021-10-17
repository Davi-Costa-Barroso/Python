# Autor: Davi Costa Barroso
# Link do Minicurso:
# https://www.youtube.com/playlist?list=PL032B_GjLSupaGtbbnl7-iDt-uV4-hzYh

#Exercício 05:
#Verifique quantos valores da lista abaixo são maiores do que 15. 
#lista = [2, 4, 6, 10, 20, 1, 8, 19, 15, 7, 41, 3, 16, 12]

lista = [2, 4, 6, 10, 20, 1, 8, 19, 15, 7, 41, 3, 16, 12]
contador = 0
for elemento in lista:
  if elemento > 15:
    contador = contador + 1
print("Quantidade de valores maiores do que 15: ", contador)