try:
    a = int(input('Digite o primeiro numero: '))
    b = int(input('Digite o segundo numero: '))
    c = int(input('Digite o terceiro numero: '))

    maior = a
    if a == b == c:
        print('Os números são iguais.')
    else:
        if b > a and b > c:
            maior = b
        elif c > a and c > b:
            maior = c

        print(f'O maior número digitado é {maior}')
    
except ValueError:
    print(f'Por favor digite apenas números inteiros.')