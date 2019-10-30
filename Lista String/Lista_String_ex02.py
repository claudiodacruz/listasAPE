'''
2. Faça um programa que leia uma frase e a exiba sem os espaços em branco.
'''

s = input('Frase: ')
r = s.split()
print(r)
p = ''

for i in range(len(r)):
    p += r[i]
print(p)


'''
s = input('Frase: ')
s = s.replace(' ','')
print (s)
'''
