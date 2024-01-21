idade = int(input('Nesse programa, vamos descobrir se você é considerado(a) criança, adolescente, adulto(a) ou idoso(a)\nPara isso,informe qual é a sua idade?: '))

if idade < 12 and idade > 0:
        print('Você é uma criança!')
elif idade >= 12 and idade < 18:
        print('Você é adolescente!')
elif idade >=18 and idade < 60:
        print('Você é adulto(a)!')
elif idade >=60:
        print('Você é idoso(a)')
