'''
9. Escreva uma função login que exclua da string de um email toda a parte referente
ao domínio, deixando apenas a parte referente ao login.
Por exemplo, suponha que o parâmetro email receba "fulano@provedor.com.br",
então deverá ficar apenas "fulano".
Faça também um programa para testar a função.
'''

def email(n):
    nova = n.split("@")
    p = nova[0]
    return p

e = "fulato.detal@provedor.com"
login = email(e)
print(login)
