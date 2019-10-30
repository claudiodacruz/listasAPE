'''
11. Faça um programa que leia uma string S e um valor inteiro N, e exiba
na tela a string S com as suas vogais repetidas N vezes.
Exemplo:
Entrada: S: Hoje tem aula de Python
N: 3
Saída: Hooojeee teeem aaauuulaaa deee Pythooon
'''

frase = input('Informe a frase: ')
num = int(input('Informe um número inteiro de 2 a 5: '))
tam = len(frase)
vogais = 'AaEeIiOoUu'
nova = ''

for i in frase:
    if i in vogais:
        nova = nova + (i * num)
    else:
        nova = nova + i
print(nova)
