'''
Escreva um programa que leia os seguintes dados de um conjunto de alunos:
matrícula, nome e as duas notas que ele obteve em suas avaliações. A condição
de parada será a digitação de uma matrícula igual 0 (zero). O programa deverá
mostrar, para cada aluno, as seguintes informações: matrícula, nome, média e
situação (aprovado, se a média for igual ou superior a 7 e, reprovado, se a
média for inferior a 7).
'''
m = 'matricula'
while m != '0':
    m = input('Digite a matricula: ')
    n = input('Digite o nome do aluno: ')
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    me = (n1 + n2) / 2
    print(me)
    if me >= 7.0:
        r = 'aprovado'
    else:
        r = 'Reprovado'
    me = str(me)    
    mat = list(m)
    nome = list(n)
    media = list(me)
    resultado = list(r)
print(mat,end='')
print('// ',nome,end='')
print('// Média = ',media,end='')
print('// ',resultado,end='')
