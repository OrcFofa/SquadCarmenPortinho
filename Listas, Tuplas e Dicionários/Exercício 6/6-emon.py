nome = input('Digite seu nome e tenha uma surpresa: ')

i = 0

#enquanto houver elementos no input, vão ser impressos na tela do último ao primeiro
while i < len(nome): 
    print(nome[-1 - i].upper(), end="") #end = "" significa que o comando print vai terminar assim que a letra for impressa, ao invés de terminar com \n
    i +=1

print() #pula uma linha após a impressão completa do nome
