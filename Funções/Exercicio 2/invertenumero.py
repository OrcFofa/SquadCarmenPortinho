def invertendo(num):
    num_invertido = 0
    while num > 0:
        num_invertido = num_invertido*10 + (num%10)
        num = num//10
    return num_invertido

def main():
    numero = int(input("Digite um número: "))

    inv = invertendo(numero)
    print(f'O número {numero} invertido é {inv}')

if __name__ == '__main__':
    main()