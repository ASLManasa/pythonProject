class polygon:
    def abstractc(self):
        raise NotImplementedError("Subclasses should implement this!")


class square(polygon):
    def __init__(self, a):
        self.a = a

    def areas(self):
        area = self.a * self.a
        print("area of a square=", area)


class rectangle(polygon):
    def __init__(self, l, b, h):
        self.l = l
        self.b = b
        self.h = h

    def arear(self):
        arear = self.l * self.b * self.h
        print("area of a rectangle", arear)


class triangle(polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def areat(self):
        areat = (self.base * self.height) * 0.5
        print("area of a triangle", areat)


p1 = polygon()
s1 = square(3)
s1.areas()
r1 = rectangle(2, 3, 4)
r1.arear()
t1 = triangle(2, 3)
t1.areat()
