# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Client:
    def __init__(self, name):
        self._name = name
        self._addresses = []

    def insert_adress(self, street, number):
        self._addresses.append(Adress(street, number))

    def list_addresses(self):
        for address in self._addresses:
            print(address.street, address.number)

    def __del__(self):
        print("Deleting", self._name)

class Adress:
    def __init__(self, street, number):
        self.street = street
        self.number = number

    def __del__(self):
        print("Deleting", self.street, self.number)


client1 = Client("Rafael")
client1.insert_adress("Rua do Feijão", 67)
client1.insert_adress("Rua do Arroz", 42)
client1.list_addresses()

del client1
