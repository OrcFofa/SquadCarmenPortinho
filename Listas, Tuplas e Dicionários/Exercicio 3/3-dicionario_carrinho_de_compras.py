''' 
Crie um dicionário representando um carrinho de compras.Adicione 
produtos(chaves) e quantidades(valores) ao carrinho. Calcule o 
total do carrinho de compra.
'''

print('''\nSeja bem vindo ao supermercado!
Fique a vontade para escolher os produtos 
e a quantidade que deseja comprar.
''')

carrinho_de_compras = {}

while True:
    produto = input("Digite o nome do produto: ")
    valor = int(input("Digite a quantidade: "))
    carrinho_de_compras[produto] = valor

    continuar = input('Quer adicionar mais produtos? ').lower()

    if continuar == "não" or continuar == "nao":
        break
    else:
        continue

quantidade = sum(carrinho_de_compras.values())
print('Sua lista de compras: ')

for produto in carrinho_de_compras.keys():
    print(f'{produto}')
print(f" Você colocou {quantidade} produtos em seu carrinho de compras")
