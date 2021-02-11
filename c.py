class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def display(self):
        print("( ", self.x, " , ", self.y, " )")


class Location(Point):
    def __init__(self, x, y):
        Point.__init__(self, x, y)

    def distance(self, target):
        dist = (((target.x - self.x) ** 2) + ((target.y - self.y) ** 2)) ** 0.5
        print("Distance between two points is: ", dist)


source = Location(9, 7)
source.display()
destination = Location(3, 2)
destination.display()
source.distance(destination)
