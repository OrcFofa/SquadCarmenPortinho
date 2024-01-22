
# Vamos construir um jogo de forca. O programa acolherá aleatpriamente uma palavra secreta de uma lista predefinida. A palavra
# secreta será representada por espaços em branco, um para cada letra da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
# tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente na palavra secreta, ela será revelada nas posições correspondentes. Se
# a letra não estiver na palavra, uma mensagem de erro deverá ser informada. Após um número máximo de erros, o jogador perde. O jogo
# continua até que o jogador adivinhe a palavra ou exceda o número máximo de tentativas.
# Dica: Você precisará importar uma biblioteca para resolver esse exercício


import random

def escolher_palavra():
    palavras = ["daniele", "alyne", "gessica", "laura", "renata", "thayna"]
    tam_lista = len(palavras)
    indice_aleatorio = random.randint(0, tam_lista - 1)
    return palavras[indice_aleatorio]

def exibir_palavra_oculta(palavra, letras_corretas):
    result = ""
    for letra in palavra:
        if letra in letras_corretas:
            result += letra 
        else:
            result += '_'
    return result.strip()


palavra_secret = escolher_palavra()
letras_corretas = set()
tentativas_max = 6

print("Jogo de Forca")

letras_unicas = set(palavra_secret)

while len(letras_corretas) < len(letras_unicas) and tentativas_max > 0:
    print(exibir_palavra_oculta(palavra_secret, letras_corretas))
    
    letra = input("Digite uma letra: ").lower()

    if letra in letras_corretas:
        print("Você já tentou essa letra.")
    elif letra in letras_unicas:
        letras_corretas.add(letra)
        print("Correto!")
    else:
        tentativas_max -= 1
        print(f"Incorreto. Tentativas restantes: {tentativas_max}")

if letras_corretas == letras_unicas:
    print("Parabéns! Você adivinhou a palavra:", palavra_secret)
else:
    print("Você excedeu o número de tentativas. Palavra secreta:", palavra_secret)

