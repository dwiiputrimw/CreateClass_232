from math import sqrt
class Point:
    x=0
    y=0
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __str__(self):
        return str(self.x)+","+str(self.y)
    def distance_from_origin(self):
        return sqrt((self.x**2)+(self.y**2))
    def distance(self, other_point):
        dx=self.x-other_point.x
        dy = self.y-other_point.y
        return sqrt(dx*dx+dy*dy)
