'''
10. Faça um programa que leia o nome de uma pessoa e exiba-o conforme o exemplo
abaixo.
Obs: Suponha que o nome lido não possua nenhuma preposição, artigo, etc.
Exemplo:
Entrada: FLAVIO RIBEIRO COUTINHO
Saída: COUTINHO, F. R.
'''
nome = input('Informe o nome sem artigos ou preposições: ').upper()
novo = nome.split()
tam = len(novo)
saida = novo[tam-1] + ', '

for i in range(tam - 1):
    saida = saida + novo[i][0] + '. '
    
print(saida)
