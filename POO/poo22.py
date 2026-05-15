# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager

@contextmanager
def my_open(file_path, mode):
    print('Opening File')
    try:
        file = open(file_path, mode, encoding='utf8')
        yield file
    except:
        print('Error')
    finally:
        file.close()
    
with my_open('POO/poo22.txt', 'w') as file:
    file.write('Welcome!\n')
    file.write('Line 2\n')
    file.write('New!\n')