'''Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e 
   classifique-o equilátero:todos os lados com o mesmo valor
   isósceles:dois lados como mesmo valor
   escaleno:todos os lados com medidas distintas.'''

a = input("Digite o comprimento do primeiro lado do triângulo: ")
b = input("Digite o comprimento do segundo lado do triângulo: ")
c= input("Digite o comprimento do terceiro lado do triângulo: ")

if a == b and b==c:
    print("Esse é um triângulo equilátero")
elif a==b or b==c or a==c:
    print("Esse é um triângulo isósceles")
else:
    print("Esse é um triângulo escaleno")