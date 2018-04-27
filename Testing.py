
class Triangle(object):
    def __init__(self, point1, point2, point3):
        if len(point1) != 3 or len(point1) != 3 or len(point1) != 3:
            raise ValueError("Error: Triangle lacks correct point definition.")
        else:
            self.points = [point1, point2, point3];
    def area(self):
        Ax = self.points[0][0]
        Ay = self.points[0][1]
        Bx = self.points[1][0]
        By = self.points[1][1]
        Cx = self.points[2][0]
        Cy = self.points[2][1]
        return abs(/2)

testTriangle = Triangle((0,0),(0,1),(1,0))
print(testTriangle.area())
