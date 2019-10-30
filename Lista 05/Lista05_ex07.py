'''
07 - Faça um programa que receba e armazene numa matriz o nome e as 3 notas dos
20 alunos de uma turma e:
a) calcule (e armazene na mesma matriz dos dados de entrada):
- a média aritmética de cada aluno;
- a situação de cada aluno; (aprovado se média superior ou igual a 7.0)
- o número de alunos aprovados;
- a média geral da turma;
b) exiba:
- o nome e a situação de cada aluno;
- o número de alunos aprovados;
- a média geral da turma;
- o nome e a média dos alunos com média superior ou igual à média geral da turma.

'''

# INICIALIZANDO AS VARIÁVEIS
m = []
lin = 4  '''Defini para 4 alunos para não ficar complicado de testar'''
col = 3
apv = 0
somamed = 0

# ALIMENTANDO A MATRIZ COM NOME E NOTAS E AVALIANDO O RESULTADO
for i in range(lin):
    soma = 0
    linha = []
    nome = (input('Informe o nome do aluno: '))
    linha.append(nome)       
    for j in range (col):
        nota = float(input('Informe nota: '))
        linha.append(nota)
        soma += nota
        
    '''Calculando a média'''
    media = soma / col
    linha.append(media)
    
    '''Analisando e arquivando o resultado do aluno'''
    if media >= 7:
        sit = 'Aprovado'
        apv += 1
    elif media < 4:
        sit = 'Reprovado'
    else:
        sit = 'Recuperação' 
    linha.append(sit)

    '''Armazenando os dados individuais na matriz'''
    m.append(linha)

# CALCULANDO A MÉDIA GERAL
    somamed += media
    print(somamed)
mediag = somamed / lin

# CRIANDO A MATRIZ COM RESULTADOS ACIMA DA MÉDIA    
n = []
contcol = 0
for i in range(lin):
    if m[i][4] >= mediag:
        linha = []
        linha.append(m[i][0])
        linha.append(m[i][4])
        n.append(linha)
        contcol +=1
    
# EXIBINDO OS RESULTADOS    
print('\nMatriz Geral')
for i in range(lin):
    print(m[i])
print('\nNúmero de alunos aprovados:',apv)
print('\nMédia Geral da Turma: {:.2f}.'.format(mediag))

print('\nMatriz Acima da Média')
for i in range(contcol):
    print(n[i])



                
        
