import json
from poo4 import FILE_PATH, People, do_dump

do_dump()

data = []
with open(FILE_PATH, 'r', encoding='utf8') as file:
    data = json.load(file)
    p1 = People(**data[0])
    p2 = People(**data[1])
    p3 = People(**data[2])
    p4 = People(**data[3])
    
# print(data)


pessoas = [p1, p2, p3, p4]

for p in pessoas:
    print(p.say_name())
    print(p.say_age())
    print(30*'-')
    