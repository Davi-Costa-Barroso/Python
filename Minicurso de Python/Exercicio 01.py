# Autor: Davi Costa Barroso
# Link do Minicurso:
# https://www.youtube.com/playlist?list=PL032B_GjLSupaGtbbnl7-iDt-uV4-hzYh

# Exercício 01:
# Faça um algoritmo para ler o salário de um funcionário e aumentar em 10%.
# Após o aumento, desconte 10% de impostos. 
# Imprima o salário inicial, o salário com o aumento e o salário final.

salario = float(input("Informe o salário: "))
salario_com_aumento = salario + (salario * 0.1)
salario_final = salario_com_aumento - (salario_com_aumento * 0.1)
print("Salário incial: ",salario)
print("Salário com aumento: ", salario_com_aumento)
print("Salário final: ", salario_final)