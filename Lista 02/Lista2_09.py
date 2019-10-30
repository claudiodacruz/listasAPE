'''
O departamento que controla o índice de poluição do meio ambiente mantém 3 grupos de
indústrias que são altamente poluentes do meio ambiente. O índice de poluição aceitável varia de
5 até 25. Se o índice sobe para 30, as indústrias do 1º grupo são intimadas a suspenderem suas
atividades; se o índice cresce para 40, as indústrias do 1º e 2º grupos são intimadas a
suspenderem suas atividades; e, se o índice atingir 50, todos os 3 grupos devem ser notificados a
paralisarem suas atividades. Escreva um programa que leia o índice de poluição medido e emita a
notificação adequada aos diferentes grupos de indústrias.
'''
ip = int(input('Informe o índice de poluição: '))

if ip >= 50:
    intim = '1º, 2º e 3º'
elif ip >= 40:
    intim = '1º e 2º'
elif ip >= 30:
    intim = '1º'
if ip <30:
    print('Nenhuma intimação será emitida')
else:    
    print('Intime-se o(s) {} grupo(s).'.format(intim))
