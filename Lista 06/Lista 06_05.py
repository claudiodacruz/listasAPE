'''
5. Escreva um programa que leia do teclado o nome de um arquivo texto e uma
string, abra o arquivo e inclua no início dele a string lida.
'''

nome_arq = input('Informe o nome do arquivo:\n')
string = input('Digite a nova informação:\n')

arq = open(nome_arq+'.txt','r+')
arq.seek(0)
arq.write(string)

arq.close()

print('Inclusão realizada com sucesso.')
               
