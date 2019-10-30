'''
Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma certa
cidade, num determinado dia. Para cada casa visitada, é fornecido o número do
canal (5, 7, 10 ou 12) e o número de pessoas que o estavam assistindo naquela
casa. Faça um programa que:
a) leia um número indeterminado de dados, sendo que o flag corresponde ao canal igual a 0 (zero);
b) calcule e escreva a porcentagem de audiência de cada emissora.
'''
canal = 1
num = 0
canal5 = 0
canal7 = 0
canal10 = 0
canal12 = 0
total = 0
while canal != 0:
     
    if canal == 5:
        canal5 = canal5 + num
    elif canal == 7:
        canal7 = canal7 + num
    elif canal == 10:
        canal10 = canal10 + num
    else:
        canal12 = canal12 + num
    canal=int(input('Qual a emissora está sendo assistida? '))
    num=int(input('Quantas pessoas estão assistindo a emissora? '))
    total = total + num
emis5 = (canal5 / total) * 100
emis7 = (canal7 / total) * 100
emis10 = (canal10 / total) * 100
emis12 = (canal12 / total) * 100
print('A audiência da emissora 5 foi de {:.2f}%'.format(emis5))
print('A audiência da emissora 7 foi de {:.2f}%'.format(emis7))
print('A audiência da emissora 10 foi de {:.2f}%'.format(emis10))
print('A audiência da emissora 12 foi de {:.2f}%'.format(emis12))
