'''
Escreva um programa que leia o peso e a altura de uma pessoa, determine e mostre o seu grau de
obesidade, de acordo com a tabela seguinte. O grau de obesidade é determinado pelo índice de
massa corpórea, cujo cálculo é realizado dividindo-se o peso da pessoa pelo quadrado da sua
altura.
'''
peso = float(input('Informe o peso: '))
altura = float(input('Informe a altura: '))
imc = (peso / (altura ** 2))
if imc >= 30:
    clas = '"Obeso Mórbido"'
elif imc < 26:
    clas = '"Normal"'
else:
    clas = '"Obeso"'
print('O grau da massa corpórea é: {}.'.format(clas))

