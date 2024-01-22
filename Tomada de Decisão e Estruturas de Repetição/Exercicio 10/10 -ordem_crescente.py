"""
Faça um programa que lê três números inteiros e os mostra em ordem crescente.
"""
#criando uma lista
listaDeNumeros = [] 

#solicitando números
numero1= int(input('Por favor digite um número inteiro: '))
numero2= int(input('Por favor digite outro número inteiro: '))
numero3= int(input('Por favor digite mais um número número inteiro: '))

#adicionando números na lista
listaDeNumeros.append(numero1)
listaDeNumeros.append(numero2)
listaDeNumeros.append(numero3)


#ordenando os números
listaDeNumeros.sort()

#mostrando a lista em ordem crescente
print(listaDeNumeros)


