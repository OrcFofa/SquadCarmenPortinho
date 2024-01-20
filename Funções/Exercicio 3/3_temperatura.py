#Conversor de Temperatura: Escreva um script que pergunta ao usuário se ele
#deseja converter uma temperatura de graus Celsius para Fahrenheit ou vice-versa.
#Para cada opção, crie uma função.


def Celsius_para_Fahrenheit(temperatura_C):
    temperatura_F = 1.8 * temperatura_C + 32
    return temperatura_F

def Fahrenheit_para_Celsius(temperatura_F):
    temperatura_C = (temperatura_F - 32) / 1.8
    return temperatura_C

def iniciar():
    escolha = input('Escolha o tipo de conversão que deseja (C para Fahrenheit, F para Celsius): ')

    if escolha.upper() == 'C':
        temperatura_C = float(input('Informe a temperatura em °C: '))
        temperatura_F = Celsius_para_Fahrenheit(temperatura_C)
        print('Temperatura em {:.1f}°F'.format(temperatura_F))

    elif escolha.upper() == 'F':
        temperatura_F = float(input('Informe a temperatura em °F: '))
        temperatura_C = Fahrenheit_para_Celsius(temperatura_F)
        print('Temperatura em {:.1f}°C'.format(temperatura_C))
    else:
        print('Insira "C" para Celsius ou "F" para Fahrenheit!')

iniciar()