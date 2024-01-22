'''Escreva um programa que calcule o salário líquido.
   Lembrando de declarar o salário bruto e o percentual de desconto do Imposto de Renda.
   ●Renda até R$1.903,98:isento de imposto de renda;
   ●Renda entre R$1.903,99 e R$2.826,65:alíquota de 7,5%;
   ●Renda entre R$2.826,66 e R$3.751,05:alíquota de 15%;
   ●Renda entre R$3.751,06 e R$4.664,68:alíquota de 22,5%;
   ●Renda acima de R$4.664,68:alíquota máxima de 27,5%.'''

salario_bruto = float(input("Digite seu sálario (bruto): "))

if salario_bruto >= 1903.99 and salario_bruto <= 2826.65:
    salario_liquido = salario_bruto - (salario_bruto * 0.075)
    print(f"Seu sálario bruto é de {salario_bruto} o desconto é de 7.5% então seu sálario liquido é {salario_liquido:.2f}")

elif salario_bruto >= 2826.66 and salario_bruto <= 3751.05:
    salario_liquido = salario_bruto - (salario_bruto * 0.15)
    print(f"Seu sálario bruto é de {salario_bruto} o desconto é de 15% então seu sálario liquido é {salario_liquido:.2f}")

elif salario_bruto >= 3751.06 and salario_bruto <= 4664.68:
    salario_liquido = salario_bruto - (salario_bruto * 0.225)
    print(f"Seu sálario bruto é de {salario_bruto} o desconto é de 22,5% então seu sálario liquido é {salario_liquido:.2f}")

elif salario_bruto > 4664.68:
    salario_liquido = salario_bruto - (salario_bruto * 0.275)
    print(f"Seu sálario bruto é de {salario_bruto} o desconto é de 27,5% então seu sálario liquido é {salario_liquido:.2f}")

else:
    print(f"Seu sálario bruto é de {salario_bruto} o desconto é de 0% então seu sálario liquido é {salario_bruto}")