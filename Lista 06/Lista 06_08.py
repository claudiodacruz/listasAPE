'''
8. Escreva um programa que leia do teclado o nome, o sexo e a idade de várias
pessoas e armazene esses dados em um arquivo texto chamado CADASTRO.TXT, sendo
uma pessoa por linha e os dados separados por vírgula.  Obs: a leitura do nome
vazio (string nula) encerra os dados de entrada.
'''
arq = open('cadastro.txt','w')
print('Digite os dados das pessoas')
print('Para encerrar, deixe o nome vazio')
n = 0
while True:
    nome = input('Nome: ')
    if nome == '':
        break
    sexo = input('Sexo(M/F): ')
    idade = int(input('Idade: '))
    linha = nome+','+sexo+','+str(idade)
    arq.write(linha+'\n')
    n = n+ 1
arq.close()
print('Arquivo gerado com sucesso. Foram gravados ',n,'registros.')


