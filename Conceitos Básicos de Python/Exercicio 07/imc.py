peso = float(input('Digite seu peso (em kg): '))
altura = float(input('Digite sua altura (em metros ex.:1.65): '))
imc = peso / (altura * altura)

print(f'Seu IMC é: {imc:.1f}')