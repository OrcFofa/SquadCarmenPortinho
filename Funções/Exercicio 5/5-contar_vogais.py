'''Crie uma função chamada contar_vogais que recebe uma string como parâmetro.
   Implemente a lógica para contar o número de vogais na string e retorne o total de vogais.
   Solicite ao usuário para inserir uma frase e utilize a função para contar as vogais.'''

def contar_vogais (frase):
    vogais = 0 
    frase = frase.lower()

    for letra in frase:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            vogais += 1

    print(f"Essa frase tem {vogais} vogais")


frase = input("Insira uma frase: ")
contar_vogais(frase)