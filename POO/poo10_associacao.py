# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).

class Writer:
    def __init__(self, name):
        self.name = name
        self._write_tool = None

    @property
    def write_tool(self):
        return self._write_tool

    @write_tool.setter
    def write_tool(self, tool):
        self._write_tool = tool

class WriteTool:
    def __init__(self, name):
        self.name = name

    def write(self):
        return f'{self.name} is writing...'
    
writer1 = Writer('Rafael')
pen = WriteTool('Pen')
writer1.write_tool = pen

print(writer1.name)
print(writer1.write_tool.name)
print(writer1.write_tool.write())