'''
08 -Faça um programa que, a partir da digitação do infinitivo de um verbo regular, faça a
conjugação do mesmo no presente do indicativo para as pessoas do singular e plural.
'''

v = input('Qual verbo deseja conjugar? ')
v = v.lower()
t = len(v)
r = v[:t-2]

pe = ['Eu','Tu','Ele','Nós','Vós','Eles']
ar = ['o','as','a','amos','ais','am']
ir = ['o','es','e','imos','is','em']
er = ['o','es','e','emos','eis','em']

for i in range(6):
        if v[-2] == 'a':
            print(pe[i], r + ar[i])
        elif v[-2] == 'e':
            print(pe[i], r + er[i])
        elif v[-2] == 'i':
            print(pe[i], r + ir[i])

        
