import numpy as np
import math

class Triangle(object):
    def __init__(self, point1, point2, point3, color = [255, 255, 255]):
        if len(point1) != 3 or len(point1) != 3 or len(point1) != 3:
            raise ValueError("Error: Triangle lacks correct point definition.")
        else:
            self.points = [point1, point2, point3];
        self.active = True
        self.color = color
        
    def __str__(self):
        return "Triangle"
    
    def setActive(self, active):
        self.active = active
        
    def givePoints2D(self):
        a = self.points
        return [[a[0][0],a[0][2]],[a[1][0],a[1][2]],[a[2][0],a[2][2]]]

    def checkActive(self, camera):
        self.active = camera.triangleInFrame(self)

    def coversCamera(self, camera):
        a, b, c = angleTo((self.points[0][0]-camera.x(), self.points[0][2]-camera.z())), angleTo((self.points[1][0]-camera.x(), self.points[1][2]-camera.z())), angleTo((self.points[2][0]-camera.x(), self.points[2][2]-camera.z()))
        return containsOrigin(a, b, c)

    def render(self, camera, screen):
        return [camera.getPointLocation(self.points[0], screen), camera.getPointLocation(self.points[1], screen), camera.getPointLocation(self.points[2], screen)]
    
def containsOrigin(a, b, c):
    return withinRange(a,b,c) or withinRange(b,c,a)

def reflect(a):
    a % math.pi * 2
    if a > math.pi:
        a -= math.pi
    return a

def withinRange(a, a2, c):
    if abs(a2 - a) < math.pi:
        a, a2 = min(a, a2), max(a, a2)
    else:
        a2, a = min(a, a2), max(a, a2)
    b = reflect(a)
    b2 = reflect(a2)
    return b2 >= c >= b

def angleTo(pt):
    angle = np.angle(pt[0]+pt[1]*1.0j)
    return angle
