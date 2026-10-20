import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y)**2)


class Vector(Point):
    def __str__(self):
        return f"Vector <{self.x}, {self.y}>"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

print(Point(1,2))
print(Point(3,4))
print(Point(1,2)==Point(3,4))
print(Point(1,2).distance(Point(3,4)))

print(Vector(1,2))
print(Vector(3,4))
print(Vector(1,2)==Vector(1,2))
print(Vector(1,2).distance(Vector(3,4)))
print(Vector(1,2)+Vector(3,4))

print(type(Vector(1,2)).__name__)