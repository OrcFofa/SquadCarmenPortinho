'''Crie duas tuplas.
   Concatene-as para formar uma nova tupla.'''

#criando a 1° tupla
tupla1 = []
item1 = tupla1.append(input("Digite o item 1 da primeira tupla: "))
item2 = tupla1.append(input("Digite o item 2 da primeira tupla: "))
item3 = tupla1.append(input("Digite o item 3 da primeira tupla: "))


#criando a 2° tupla
tupla2 = []
item1 = tupla2.append(input("Digite o item 1 da segunda tupla: "))
item2 = tupla2.append(input("Digite o item 2 da segunda tupla: "))
item3 = tupla2.append(input("Digite o item 3 da segunda tupla: "))


#juntando e modificando
tupla_nova = tupla1 + tupla2
tupla_nova = sorted(tupla_nova)
tupla_nova = tuple(tupla_nova)

#imprimindo de forma crescente
print(tupla_nova)
