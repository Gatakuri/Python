import json
caminho = "/home/usuario/Documentos/Python"
pessoas = {
    "nome": 'Rafael Coelho 2',
    "idade": 18,
    "endereços":[
        {"rua": 'Rodolfo galvão', "número": 92},
        {"rua": 'Conde de Bonfim', "número": 685},
    ],
    "DEV": True,
    "casado": True
}

with open("aula2.json", 'w', encoding='utf8') as arquivo:
    json.dump(pessoas, arquivo, ensure_ascii=False, indent=2)

     
with open("aula2.json", 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa['nome'])