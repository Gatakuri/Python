# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class MyString(str):
    def upper(self):
        print("Called Upper")
        my_return = super(MyString, self).upper()
        return my_return

# string = MyString("Rafael")
# print(string.upper())

class A:
    def __init__(self, atribute):
        self.atribute = atribute

    atribute_a = 'A value'

    def method(self):
        print('A')

class B(A):
    def __init__(self, atribute, other):
        super().__init__(atribute)
        self.other = other

    atribute_b = 'B value'

    def method(self):
        print('B')

class C(B):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    atribute_c = 'C value'

    def method(self):
        super(B, self).method()
        super().method()
        print('C')

c = C('atribute', "other")
# print(c.atribute_a)
# print(c.atribute_b)
# print(c.atribute_c)
# c.method()
print(C.mro())
print(c.atribute)
print(c.other)
