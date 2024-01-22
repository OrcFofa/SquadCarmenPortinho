# 4. Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda estrangeira.

carteira = float(input("Digite o valor que possui em sua carteira: R$"))
moedas = {
    "Dólares Americanos": 4.91,
    "Pesos Argentinos": 0.02,
    "Dólares Australianos": 3.18,
    "Dólares Canadenses": 3.64,
    "Francos Suíços": 0.42,
    "Euros": 5.36,
    "Libras esterlinas": 6.21
}

def valor_em_outra_moeda(carteira, valor_moeda, nome_moeda):
    try:
        valor = carteira/valor_moeda
        print(f"* {valor:.2f} {nome_moeda}")
    except TypeError as e:
        print(f"Erro: o tipo do dado informado está incorreto. \nDetalhes: {e}")

print(f"Com R${carteira:.2f} você pode comprar:")

for chave, valor in moedas.items():
    valor_em_outra_moeda(carteira, valor, chave)