# Exercício - Salve sua classe em JSON

# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

class People:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def say_name(self):
        return f'My name is {self.name} {self.surname}'
    
    def say_age(self):
        return f'My age is {self.age} years'
    
        
FILE_PATH = "POO/poo4.json"
p1 = People("Rafael", "Coelho", 17)
p2 = People("Aaron", "Carvalho", 18)
p3 = People("Giovana", "Simões", 18)
p4 = People("Isaac", "Pedro", 18)
data = [vars(p1), vars(p2), vars(p3), vars(p4)]

# print(p1.say_name())

def do_dump():
    with open(FILE_PATH, "w", encoding='utf8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    print('Main')
    do_dump()
