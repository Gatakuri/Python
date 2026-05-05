# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Car:
    def __init__(self, name):
        self.name = name
        self._engine = None
        self._maker = None

    @property
    def engine(self):
        return self._engine
    
    @engine.setter
    def engine(self, engine):
        self._engine = engine

    @property
    def maker(self):
        return self._maker
    
    @maker.setter
    def maker(self, maker):
        self._maker = maker

class Engine:
    def __init__(self, name):
        self.name = name

class Maker:
    def __init__(self, name):
        self.name = name
        self._cars = []

    def add_cars(self, *cars):
        for car in cars:
            car.maker = self
            self._cars.append(car)
            

    def list_cars(self):
        print()
        for car in self._cars:
            engine_name = car.engine.name if car.engine else "No engine"
            maker_name = car.maker.name
            print(f'{car.name} with {engine_name} engine from {maker_name}')
        print()

#Cars       
mercedes = Car("Mercedes")
ferrari = Car("Ferrari")
fusca = Car("Fusca")
#Engines
engine_v8 = Engine("V8")
engine_v4 = Engine("V4")
#Makers
maker_1 = Maker("Rafael")
maker_2 = Maker("Giovana")

#Operations
mercedes.engine = engine_v8
ferrari.engine = engine_v8
fusca.engine = engine_v4

maker_1.add_cars(mercedes, ferrari)
maker_1.list_cars()

maker_2.add_cars(fusca)
maker_2.list_cars()