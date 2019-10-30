'''
9. Faça um programa que leia uma frase e a exiba criptografada. O método de
criptografia será baseado na seguinte regra: trocar alguns caracteres por
outros, conforme a tabela abaixo:
'''

f = input('Informe a frase a ser criptografada: ').upper()
tam = len(f)
s = []
v = ['A','E','I','O','U',' ']
c = [' ','U','O','I','E','A']

#GERANDO UM VETOR COM TODOS OS CARACTERES DA FRASE
for i in range(tam):
    s.append(f[i])

#FAZENDO A CRIPTOGRAFIA DO VETOR
for i in range(tam):
    if s[i] in v:
        count = 0
        for j in range(6):
            if s[i] == v[j] and count < 1:
                s[i] = c[j]
                count += 1

#IMPRIMINDO A MENSAGEM CRIPTOGRAFADA
for i in range(tam):
    print(s[i],end='')


