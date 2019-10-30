'''2. Escreva um programa que copie um arquivo texto (cujo nome será lido pelo
teclado) para um novo arquivo chamado COPIA.TXT, porém substituindo todos os
brancos contidos no arquivo pelo ponto.'''

nomearq = input("Informe o nome do arquivo: ")
arq = open(nomearq+'.txt','r')
copia = open('copia.txt','w')
texto = arq.read()
novotexto = texto.replace(' ','.')
copia.write(novotexto)
arq.close()
copia.close()
print('A cópia do arquivo foi gerada com sucesso.')

      

