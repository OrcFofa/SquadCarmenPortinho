# 9. Solicite ao usuário o número de horas de exercício físico por semana.
#Calcule o total de calorias queimadas em um mês, considerando uma média de 5 calorias por minuto de exercício.

horas_semana = float(input('Digite o número de horas de exercício físico por semana:'))

MES = 30 #Atribuindo que um mês contém 30 dias

horas_em_minutos = horas_semana*60 #Transformando as horas em minutos
calorias_gasta = 5*horas_em_minutos*MES #Calculo


print(f'O total de calorias gastas no mês foi de {calorias_gasta}')

