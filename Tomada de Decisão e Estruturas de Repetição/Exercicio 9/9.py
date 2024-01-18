# 9. O programa deve calcular e apresentar a quantidade de números pares e ímpares inseridos.
# O processo de leitura deve ser encerrado quando o usuário informar o valor zero.
# Certifique-se de incluir validações para garantir que apenas números positivos sejam
# considerados na contagem e cálculos.


#Contadores
pares = 0 
impares = 0

while True:
        num = int(input("Digite um número / Digite 0 para encerrar o programa: "))
        
        if num == 0:
            break
        
        # Verificar se o número é positivo
        if num > 0:
            # Verificar se o número é par ou ímpar
            if num % 2 == 0:
                pares += 1
            else:
                impares += 1
        else:
            print("Digite apenas números positivos")


print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
