#10. Faça um Programa que utilize 4 variáveis como preferir e no final print uma mensagem amigável utilizando as variáveis criadas. Exemplos de variáveis: nome, idade, lugar, profissão.... Exemplo de retorno: Olá Maria,prazer te conhecer. Sou de São Paulo também e estou migrando de área. Lembrando que para o retorno vamos usar print com as variáveis criadas e este texto é somente um exemplo, utilizem a criatividade

nome = (input('Por favor, digite seu nome: '))
idade = (input('Por favor, digite sua idade: '))
estado = (input('Qual o estado que você reside: '))
email = 'brazil@pyladies.com'

print (f'Olá {nome}, você está com {idade} e reside no estado de {estado}. Envie um e-mail para {email} e saiba mais informações sobre o grupo PyLadies, um grupo com o propósito de ajudar mais e mais mulheres a se tornarem participantes ativas e líderes na comunidade open source Python' )