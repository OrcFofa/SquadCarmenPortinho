# Escreva um programa que calcule o tempo de uma viagem. Faça um comparativo do mesmopercurso de avião, carro e ônibus.
# Levando em consideração:
# avião = 600 km/h
# carro = 100 km/h
# ônibus = 80 km/h

def calcular_tempo(distancia, velocidade):
    tempo = distancia / velocidade
    return tempo

velocidade_aviao = 600 
velocidade_carro = 100 
velocidade_onibus = 80 

distancia_viagem = float(input("Digite a distância da viagem em quilômetros: "))

tempo_aviao = calcular_tempo(distancia_viagem, velocidade_aviao)
tempo_carro = calcular_tempo(distancia_viagem, velocidade_carro)
tempo_onibus = calcular_tempo(distancia_viagem, velocidade_onibus)

print(f"Tempo de viagem de avião: {tempo_aviao:.2f} horas")
print(f"Tempo de viagem de carro: {tempo_carro:.2f} horas")
print(f"Tempo de viagem de ônibus: {tempo_onibus:.2f} horas")