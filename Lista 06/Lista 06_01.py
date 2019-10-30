'''1. Escreva um programa que exiba na tela um arquivo texto cujo nome
será lido pelo teclado.'''

nomearq = input('Informe o nome do arquivo:\n')
arq = open(nomearq+'.txt','r')
print('\nConteúdo do Arquivo:\n')
print(arq.read())
arq.close()


        
