'''
Escreva um programa para calcular a conta final de um hóspede de um hotel, considerando que:
a) Serão lidos o nome do hóspede, o tipo do apartamento utilizado (A, B, C ou D), o número de diárias utilizadas
pelo hóspede e o valor do consumo interno do hóspede;
b) O valor da diária é determinado pela seguinte tabela:
    Apartamento tipo A: R$ 150,00
    Apartamento tipo B: R$ 100,00
    Apartamento tipo C: R$ 75,00
    Apartamento tipo D: R% 50,00
c) O valor total das diárias é calculado pela multiplicação do número de diárias utilizadas pelo valor da diária;
d) O subtotal é calculado pela soma do valor total das diárias e o valor do consumo interno;
e) O valor da taxa de serviço equivale a 10% do subtotal;
f) O total geral resulta da soma do subtotal com a taxa de serviço.
O programa deverá mostrar a conta final do hóspede, contendo: o nome do hóspede, o tipo do apartamento,
o número de diárias utilizadas, o valor unitário da diária, o valor total das diárias,
o valor do consumo interno, o subtotal, o valor da taxa de serviço e o total geral.
'''
nome = input('Informe o nome do hóspede: ')
tipo = input('Informe o tipo do apartamento (A, B, C ou D): ')
dias = int(input('Informe o número de diárias: '))
consumo = float(input('Informe o consumo interno do hóspede: '))
tipo = tipo.upper()
if tipo == 'A':
    diaria = 150.0
elif tipo == 'B':
    diaria = 100.0
elif tipo == 'C':
    diaria = 75.0
else:
    diária = 50.0
total_diarias = diaria * dias
subtotal = total_diarias + consumo
taxa_servico = subtotal * 0.1
total = subtotal + taxa_servico
print('Hópede:',nome)
print('Apartamento tipo:',tipo)
print('Número de diárias:',dias)
print('Valor das diárias: {:.2f}'.format(total_diarias))
print('Valor do consumo: {:.2f}'.format(consumo))
print('Subtotal: {:.2f}'.format(subtotal))
print('Taxa de serviço (10%): {:.2f}'.format(taxa_servico))
print('Total: {:.2f}'.format(total))

