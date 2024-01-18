'''
Faça um programa que peça a quantidade de quilômetros,
transforme em metros,centímetros e milímetros.
'''

user_input = int(input("Digite um valor em quilômetros: "))

def transform_to_m_mm_cm(km):
    m = km * 1000 # Multiplicamos o valor de km por mil para obter o valor em metros,
    cm = km * 100000 # por cem mil para obter o valor em centímetros,
    mm = km * 1000000 # e por um milhão para obter o valor em milímetros.
    print(f'O valor inserido corresponde a {m} metros, {cm} centímetros e {mm} milímetros!')

transform_to_m_mm_cm(user_input)