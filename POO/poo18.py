# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str
class point:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    # def __str__(self):
    #     return f'({self.x}, {self.y}) {self.z}'
    
    def __repr__(self):
        class_name = type(self)
        return f'({self.x!r}, {self.y!r}), {self.z!r}'


p1 = point(10, 20)
print(p1)