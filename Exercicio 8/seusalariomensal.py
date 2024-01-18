'''
Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês.
'''
valor_hora_trabalhada = float(input("Quanto ganha por hora trabalhada?  "))
horas_trabalhadas = int(input("Quantas horas trabalhou esse mês? "))
salario_receber = valor_hora_trabalhada * horas_trabalhadas

print(f'Seu salario será R${salario_receber:.2f}')