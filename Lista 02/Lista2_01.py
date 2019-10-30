#Escreva um programa que leia dois números e exiba-os em ordem crescente.
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if (num1 < num2):
    maior = num2
    menor = num1
else:
    maior = num1
    menor = num2
print(menor,maior)

