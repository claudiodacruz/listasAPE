'''
Escreva um programa que solicite ao usuário uma senha de 8 caracteres.
Caso a senha digitada esteja correta, o programa deverá mostrar senha
correta. Caso contrário, o programa deverá mostrar senha incorreta e
pedir para o usuário tentar novamente digitar a senha correta. Mas, se
o usuário fornecer três senhas incorretas, o programa deverá encerrar
a sua execução.
(Sugestão: Defina a senha como uma constante).
'''
pin = '12345678'
for i in range(3,0,-1):
    senha = input('Informe a senha correta: ')
    if senha == pin:
        print('Você digitou a senha coreta.')
        break
    elif i > 1:
        print('Você digitou a senha incorreta. Você tem agora mais',i-1,'tentativa(s).')
    else:
        print('Você excedeu o limite de tentativas, sua senha foi bloqueada.')
