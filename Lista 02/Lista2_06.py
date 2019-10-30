'''
Escreva um programa que leia a hora de início de um jogo e a hora do final do jogo (considerando
apenas horas inteiras), calcula a duração do jogo em horas, sabendo-se que o tempo máximo de
duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte. O
programa deve mostrar o resultado obtido.
'''
h1 = int(input('Qual o horário de início do jogo: '))
h2 = int(input('Qual o horário de término do jogo: '))
if h1 < h2:
    duracao = h2 - h1
else:
    duracao = (24 - h1) + h2
print('A duração do jogo foi de {} horas.'.format(duracao))
