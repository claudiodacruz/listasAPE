'''
Em uma pesquisa foram coletados os seguintes dados de um conjunto de 100 pessoas:
nome, idade, sexo, estado civil e salário. Neste contexto, escreva um programa
que leia os dados coletados durante a pesquisa, determine e mostre:
a) A quantidade de mulheres entrevistadas
b) A quantidade de homens entrevistados
c) A quantidade de pessoas solteiras
d) A quantidade de pessoas casadas
e) O salário médio das mulheres entrevistadas
f) A idade média dos homens entrevistados
g) A quantidade de mulheres solteiras que ganham acima de R$ 2.000,00
h) A quantidade de homens com mais de 35 anos que ganham acima de R$ 2.000,00
'''
h = 0
m = 0
s = 0
c = 0
ms2 = 0
h35 = 0
soma = 0
somai = 0
for i in range (100):
    nome = str(input('Informe o nome: '))
    idade = int(input('Informe a idade: '))
    sexo = str(input('Informe o sexo M ou F: ')).upper()
    estcivil = str(input('informe o estado civil: C (casado) ou S (solteiro): ')).upper()
    sal = float(input('Informe o salário: '))
    if sexo == 'M':
        h = h + 1 # h+=1
        somai = somai + idade
        if idade > 35 and sal > 2000.0:
            h35 = h35 + 1
    elif sexo == 'F':
        m = m + 1
        soma = soma + sal
        if estcivil == 'S' and sal > 2000.0:
            ms2 = ms2 + 1
    if estcivil == 'C':
        c = c + 1
    else:
        s = s + 1
print(m,h)
salmed = soma / m
idamed = somai / h
print('A quantidade de mulheres entrevistadas é: ',m)
print('A quantidade de homens entrevistados é :',h)
print('A quantidade de pessoas solteiras é: ',s)
print('A quantidade de pessoas casadas é: ',c)
print('O salário médio das mulheres entrevistadas é: {:.2f}'.format(salmed))
print('A idade média dos homens entrevistados é: ',idamed)
print('A quantidade de mulheres solteiras que ganham acima de R$ 2.000,00 é: ',ms2)
print('A quantidade de homens com mais de 35 anos que ganham acima de R$ 2.000,00 é: ',h35)


    
