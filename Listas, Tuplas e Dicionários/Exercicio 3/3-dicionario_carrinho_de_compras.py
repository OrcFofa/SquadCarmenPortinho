''' 
Crie um dicionário representando um carrinho de compras.Adicione 
produtos(chaves) e quantidades(valores) ao carrinho. Calcule o 
total do carrinho de compra.
'''

print('''\nSeja bem vindo ao supermercado!
Fique a vontade para escolher os produtos 
e a quantidade que deseja comprar, quando concluir
solicite o valor total da compra.\n
''')

print('''
Maçã -------------------- R$ 0.50
Banana ------------------ R$ 0.25
Pêra -------------------- R$ 1.50
Caquí ------------------- R$ 0.90
Farinha ----------------- R$ 18.0
Açúcar ------------------ R$ 22.0
''')

carrinho_de_compras = {}

precos_alimentos = {
    'maça': 0.50,
    'banana': 0.25,
    'pera': 1.50,
    'caqui': 0.90,
    'farinha': 18.0,
    'açucar': 22.0
}

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
valor_total = sum(preco * carrinho_de_compras[produto] for produto, preco in precos_alimentos.items())
print('Sua lista de compras:')

for produto in carrinho_de_compras.keys():
    print(f'{produto}')
print(f" Você colocou {quantidade} produtos em seu carrinho de compras")
print(f"O valor total a ser pago é {valor_total}")