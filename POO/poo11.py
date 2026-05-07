# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Person:

    CPF = '1234'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk_class_name(self):
        print("Class PERSON")
        print(self.name, self.age, self.__class__.__name__)

class Client(Person):
    def talk_class_name(self):
        print("Class CLIENT")
        print(self.name, self.age, self.__class__.__name__)

class Student(Person):
    CPF = 'student cpf'

c1 = Client("Rafael", 17)
c1.talk_class_name()

s1 = Student("Giovana", 17)
s1.talk_class_name()

print(c1.CPF)
print(s1.CPF)
