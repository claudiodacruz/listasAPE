'''
Escreva um programa que leia a matrícula de um aluno, suas 3 notas obtidas em provas, a média
dos exercícios escolares (ME). O programa deverá calcular a média de aproveitamento (MA),
usando a expressão:
MA = (Nota1 + Nota2 x 2 + Nota3 x 3 + ME) / 7
O programa deverá determinar o conceito do aluno na disciplina, de acordo com a tabela
seguinte:
Média de Aproveitamento Conceito
9,0 A
7,5 e < 9,0 B
6,0 e < 7,5 C
4,0 e < 6,0 D
< 4,0 E
Ao final, mostrar a matrícula do aluno, a média de aproveitamento, o conceito correspondente e a
mensagem APROVADO (se o conceito for A, B ou C) ou REPROVADO (se o conceito for D ou E).

'''
mat = input('Informe a matrícula do aluno: ')
n1 = float(input('Informe a nota 1: '))
n2 = float(input('Informe a nota 2: '))
n3 = float(input('Informe a nota 3: '))
me = float(input('Informe a média dos exercícios: '))
ma = ((n1 + n2 * 2 + n3 * 3 + me)/7)
if ma > 9.0:
    conceito = 'A'
elif ma >= 7.5:
    conceito = 'B'
elif ma >= 6.0:
    conceito = 'C'
elif ma >= 4.0:
    conceito = 'D'
else:
    conceito = 'E'
if ma >= 6.0:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'
print('O aluno de matrícula {} obteve conceito {} e está {}.'.format(mat,conceito,situacao))

