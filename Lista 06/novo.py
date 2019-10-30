arquivo = open('teste.txt', 'r') # Abra o arquivo (leitura)
conteudo = arquivo.readlines()
conteudo.append('Nova linha')   # insira seu conteúdo

arquivo = open('teste.txt', 'w') # Abre novamente o arquivo (escrita)
arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.

arquivo.close()
