'''
Faça um programa que peça a quantidade de quilômetros,
transforme em metros,centímetros e milímetros.
'''

user_input = int(input("Digite um valor em quilômetros: "))

def transform_to_mm_cm(km):
    mm = km * 1000
    cm = km * 100
    print(f'O valor inserido corresponde a {mm} milímetros!')
    print(f'O valor inserido corresponde a {cm} centímetros!')

transform_to_mm_cm(user_input)