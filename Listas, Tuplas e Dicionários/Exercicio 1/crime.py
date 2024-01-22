perguntas = [
    "Telefonou para a vítima? ",
    "Esteve no local do crime? ",
    "Mora perto da vítima? ",
    "Devia para a vítima? ",
    "Já trabalhou com a vítima? "
]
respostas = []

for pergunta in perguntas:
    resposta = input(pergunta)
    respostas.append(resposta.lower() == "sim")
 

suspeita = respostas.count(True)
if  suspeita <= 1:
    resultado = "Inocente"
elif suspeita == 2:
    resultado = "Suspeito"
elif 3 <= suspeita <= 4:
    resultado = "Cúmplice"
else:
    resultado = "Assassino"


print(f"Você é classificado como: {resultado}")