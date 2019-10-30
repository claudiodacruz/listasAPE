'''
7. Escreva um programa que leia as 3 notas de um aluno, determine e exiba a sua
média e seu conceito. O programa deve conter as seguintes funções:
 Uma função que recebe como parâmetros as 3 notas do aluno e retorne a sua
média (aritmética);
 Uma função que receba como parâmetro a média do aluno e retorne o seu conceito,
de acordo com a tabela abaixo:
MEDIA       CONCEITO  
>= 8,0         A
>=8,0 e <=5,0  B
< 5,0          C
'''

# definindo a funçao média
def media(n1, n2, n3):
    m = (n1 + n2 + n3)/3
    return m

# definindo a função conceito
def conceito(m):
    if m>= 8:
        return 'A'
    elif m > 5:
        return 'B'
    else:
        return 'C'

#Programa
nota1=float(input('Informe a primeira nota: '))
nota2=float(input('Informe a segunda nota: '))
nota3=float(input('Informe a terceira nota: '))
med = media(nota1,nota2,nota3)
conc = conceito(med)
print('Media: ',med)
print('Conceito: ',conc)
    

