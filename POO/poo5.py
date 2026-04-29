class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_50y_people(cls, name):
        return cls(name, 50)
    
p1 = People.create_50y_people("Guido")
print(p1.name, p1.age)