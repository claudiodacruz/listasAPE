'''
7. Faça um programa que leia o email de uma pessoa e mostre, separadamente,
qual o login e qual o domínio. 
Por exemplo, suponha que o email seja "fulano@provedor.com.br", então o login
será "fulano" e o domínio será "provedor.com.br".
'''

email = input('Informe o seu e-mail: ')
ref = email.replace('@',' ')
v = ref.split()
print('O login é {}.'.format(v[0]))
print('O domínio é {}.'.format(v[1]))

      
