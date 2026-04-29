import os

caminho_arquivo = "/home/usuario/Documentos/Pasta teste/aula90.txt"



with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write("Atenção\n")
    # arquivo.write('Eu amo a Giovana!!!\n')
    # arquivo.write('eu amo o rafinhaaa\n')
    arquivo.seek(0, 0)
    print(arquivo.read())
    
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())

# os.remove(caminho_arquivo)
# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())