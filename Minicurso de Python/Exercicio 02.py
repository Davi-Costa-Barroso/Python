# Autor: Davi Costa Barroso
# Link do Minicurso:
# https://www.youtube.com/playlist?list=PL032B_GjLSupaGtbbnl7-iDt-uV4-hzYh

# Exercício 02:
# Faça um programa que calcule e mostre a área de um trapézio. 
# Sabendo que: A = ((base maior + base menor) * altura)/2.

base_maior = int(input("Informe a base maior: "))
base_menor = int(input("Informe a base menor: "))
altura = int(input("Informe a altura: "))
a = ((base_maior + base_menor) * altura)/2
print("A área do trapézio é", a)