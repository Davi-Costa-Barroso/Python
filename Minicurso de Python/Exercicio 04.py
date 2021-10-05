# Autor: Davi Costa Barroso
# Link do Minicurso:
# https://www.youtube.com/playlist?list=PL032B_GjLSupaGtbbnl7-iDt-uV4-hzYh

#Exercício 04:
#Faça um programa que receba 4 notas de um aluno, 
#calcule a média e imprima aprovado ou reprovado. 
#O aluno é aprovado se a média for maior ou igual a 7.

nota1 = float(input("Informe nota 1: "))
nota2 = float(input("Informe nota 2: "))
nota3 = float(input("Informe nota 3: "))
nota4 = float(input("Informe nota 4: "))
media = ( nota1 + nota2 + nota3 + nota4 )/4
print("A média é", media)
if media >= 7:
  print("Aprovado")
else:
  print("Reprovado")