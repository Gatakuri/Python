class Car:
    def __init__(self, name):
        self.name = name

    def accelerate(self):
        print(f'{self.name} is accelerating...')

fusca = Car("Fusca")
print(fusca.name)
fusca.accelerate()

celta = Car("Celta")
print(celta.name)
celta.accelerate()