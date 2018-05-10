import math

class Camera(object):
    def __init__(self, x = 0, y = 0, z = 0, pan = 0, tilt = 0):
        self.location = (x, y, z)
        self.rotation = (pan, tilt)
        self.FOV = 2*math.pi/3
        ##self.FOVv = 4*math.pi/9

    def x(self):
        return self.location[0]

    def y(self):
        return self.location[1]

    def z(self):
        return self.location[2]

    def pan(self):
        return self.rotation[0]

    def tilt(self):
        return self.rotation[1]

    def triangleInFrame(self, triangle):
        if triangle.coversCamera(self):
            return False
        for point in triangle.points:
            a = math.atan((point[2] - self.z())/(point[1] - self.x()))
            if (point[2]-self.z()<0):
                a += math.pi
            if a > self.pan() - (self.FOV/2) and a < self.pan() + (self.FOV/2):
                return True
        return False

    def getPointLocation(self, point, screen):
        ##the x y and z locations ralative to the camera
        x, y, z = point[0] - self.x(), point[1] - self.y(), point[2] - self.z()
        angle = math.atan(z/x) - self.pan()
        w, h = screen.get_size()
        theta = self.FOV/2
        n = w/2
        pxDis = sin(theta)/n
        scalar = cos(theta)/cos(angle)
        disX = math.round((scalar*sin(angle))/pixDis)
        pixelX = n - disX
        vertFOV = self.FOV * (h/w)
        disFromScreen = math.sqrt(x*x + z*z)
        angleVert = math.atan(y/disFromScreen) - self.pan()

    
        