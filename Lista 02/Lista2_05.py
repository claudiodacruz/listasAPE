'''
Um banco concederá um crédito especial aos seus clientes, de acordo com o saldo médio de cada
cliente no último ano. Escreva um programa que leia o nome e o saldo médio de um cliente e
calcule o valor do crédito de acordo com a tabela abaixo.
Saldo médio (R$) Percentual
de 0 a 200 Nenhum crédito
de 201 a 400 20% do valor do saldo médio
de 401 a 600 30% do valor do saldo médio
acima de 601 40% do valor do saldo médio
O programa deverá exibir uma mensagem informando o nome do cliente, seu saldo médio e o
valor do crédito disponibilizado.
'''
nome = input('Informe o nome do cliente: ')
saldo = int(input('Informe o saldo médio: '))
if saldo > 200:
    if saldo > 600:
        credito = 0.4 * saldo
    elif saldo > 400:
        credito = 0.3 * saldo
    else:
        credito = 0.2 * saldo
else:
    credito = 0
print('O crédito de {} é R$ {:.2f}.'.format(nome,credito))
