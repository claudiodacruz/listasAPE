'''Faça um programa que armazene,em um vetor, um conjunto de nomes de pessoas. O programa deve permitir incluir
nomes no vetor e pesquisar por um nome existente e ainda listar todos os nomes.

MENU DE OPÇÕES:
1) Cadastrar nome
2) Pesquisar nome
3) Listar todos os nomes
0) Sair do programa
Digite sua escolha:___'''

''' ESCOLHENDO A OPÇÃO '''
print('MENU DE OPÇÕES:')
print('1) Cadastrar nome')
print('2) Pesquisar nome')
print('3) Listar todos os nomes')
print('0) Sair do programa')

v = []
p = []
cont = 0
opcao = int(input('Informe a sua escolha: '))

while opcao != 0:
            
# CADASTRAR NOME
    if opcao == 1:
        nome = input('Digite o nome a ser cadastrado: ')
        v.append(nome)
        cont += 1                           

# PESQUISAR NOME
    elif opcao == 2:
        sim = 0
        pesquisa = input('Digite o nome a ser pesquisado: ')
        for i in range(cont):
            if pesquisa == v[i]:
                p.append(pesquisa)
                sim = 1
        if sim == 1:
            resultado = "foi encontrado."
        else:
            resultado = "não foi encontrado."
        print('O nome',pesquisa,resultado)


# LISTAR TODOS OS NOMES
    elif opcao == 3:
        v = sorted(v)
        print(v)
    else:
        print('Oção inválida.')

# RETROALIMENTANDO O PROGRAMA        
    opcao = int(input('Informe sua opção: '))
print('Você saiu do programa.')

                    
