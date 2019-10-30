'''
6. O Brasil possui 26(vinte e seis) estados e um distrito. Escreva um programa
para cadastrar todos os estados e o distrito. Depois do cadastro, o programa
deverá obter de vários usuários qual é o estado que ele acha mais interessante.
O programa encerra quando for informado um estado que não foi previamente
cadastrado. Ao final, o programa deverá exibir qual foi o estado mais votado,
considere o empate.
'''

# VETOR COM OS ESTADOS E DISTRITO FEDERAL
v = ['ACRE','ALAGOAS','AMAPÁ','AMAZONAS','BAHIA','CEARÁ','DISTRITO FEDERAL',
    'ESPÍRITO SANTO','GOIÁS','MATO GROSSO','MATO GROSSO DO SUL','MARANHÃO',
    'MINAS GERAIS','PARÁ','PARAÍBA','PARANÁ','PERNAMBUCO','PIAUÍ',
    'RIO DE JANEIRO','RIO GRANDE DO NORTE','RIO GRANDE DO SUL','RONDÔNIA',
    'RORAIMA','SANTA CATARINA','SÃO PAULO','SERGIPE','TOCANTINS']

# LENDO AS OPÇÕES
w = []
z = []
opc = 'ACRE'
while opc in v:
    opc = (input('Qual o seu Estado preferido? ')).upper()
    
    if opc in v:
        w.append(opc)
        if opc not in z:
            z.append(opc)    
z.sort()      

print('Os estados selecionados foram:',z)

# COMPUTANDO OS VOTOS
votos = []
tam1 = len(z)
tam2 = len(w)
for i in range(tam1):
    cont = 0
    for j in range(tam2):
        if z[i] == w[j]:
            cont +=1
    votos.append(cont)
print('O número de votos de cada Estado selecionado foi:',votos)

# ANALISANDO O MAIS VOTADO
maior = max(votos)
ind = votos.index(maior)
count = votos.count(maior)
mvotos = []
if count == 1:
    print('O Estado mais votado foi:',z[ind])
else:
    for i in range(tam1):
        if votos[i] == maior:
            mvotos.append(z[i])
    print('Os Estados mais votados foram:',mvotos)

    
