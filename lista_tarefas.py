
# Exercício - Lista de tarefas com desfazer e refazer

# todo = [] -> lista de tarefas


# todo = ['fazer café'] -> Adicionar fazer café


# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar


# desfazer = ['fazer café',] -> Refazer ['caminhar']


# desfazer = [] -> Refazer ['caminhar', 'fazer café']


# refazer = todo ['fazer café']


# refazer = todo ['fazer café', 'caminhar']
import os
import json

def limpar():
    os.system("clear")

def ler(tarefas, caminho):
    dados = []
    try:
        with open(caminho, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo não existe")
        salvar(tarefas, caminho)
    return dados

def salvar(tarefas, caminho):
    with open(caminho, 'w', encoding='utf8') as arquivo:
        json.dump(tarefas, arquivo, indent=2,\
        ensure_ascii=False)
    

CAMINHO_ARQUIVO = 'lista_tarefas.json'
tarefas_refazer = []
tarefas = ler([], CAMINHO_ARQUIVO)



def listar(lista):
    if len(lista) == 0:
        limpar()
        print('Não há nada para listar')
        return
    limpar()
    for i in lista:
        print(i)

def desfazer(tarefas, tarefas_refazer):
    if len(tarefas) == 0:
        limpar()
        print('Nada para desfazer')
        return
    
    tarefas_refazer.append(tarefas.pop())
    listar(tarefas)

def adicionar(lista_exibida, tarefa):
    if not tarefa:
        limpar()
        print('Não adicionou nada')
        return
    
    lista_exibida.append(tarefa)
    listar(lista_exibida)

def refazer(lista_exibida, refazer_lista):
    if len(refazer_lista) == 0:
        limpar()
        print('Nada para refazer')
        return
    
    lista_exibida.append(refazer_lista.pop())
    listar(lista_exibida)

while True:
    print('Comandos: adicionar | refazer | desfazer | parar | listar')
    comando = input('Digite um comando:').lower()
    
    
    if comando == 'adicionar':
        limpar()
        tarefa = input("Digite a tarefa: ").lower()
        adicionar(tarefas, tarefa)
    elif comando == 'desfazer':
        limpar()
        desfazer(tarefas, tarefas_refazer)
    elif comando == 'refazer':
        limpar()
        refazer(tarefas, tarefas_refazer)
    elif comando == 'parar':
        limpar()
        print("Parando...")
        break
    elif comando == 'listar':
        listar(tarefas)
    else:
        limpar()
        
        print("Esse comando não existe")
        continue

    salvar(tarefas, CAMINHO_ARQUIVO)