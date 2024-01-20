'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma 
mensagem caso o valor seja inválido e continue pedindo até que o usuário 
informe um valor válido.
'''
while True:
    user_input = int(input("Digite um número entre 0 e 10: "))
    
    if user_input < 0:
        print("Esse número é menor que 0, por favor, digite novamente: ") # Verificamos se o valor é menor que 0;
        continue
    if user_input > 10:
        print("Esse número é maior que 10, por favor, digite novamente: ") # Verificamos se o valor é maior que 10;
        continue
    else: # Se o valor não é menor que 0 ou maior que dez então é válido
        print("Valor corresponte ao intervalo determinado\n")
        break
         

print('Loop while foi interrompido após inserção de valor esperado')
        