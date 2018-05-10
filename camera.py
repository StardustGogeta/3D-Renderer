import math

class Camera(object):
    def __init__(self, x = 0, y = 0, z = 0, pan = 0, tilt = 0):
        self.location = [x, y, z]
        self.rotation = [pan, tilt]
        self.FOV = 2*math.pi/3
        self.camSpeed = 0.1
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
        ##print(triangle.coversCamera(self))
##        if triangle.coversCamera(self):
##            return False
        for point in triangle.points:
            a = math.atan((point[2] - self.z())/(point[0] - self.x()))
            ##print(a)
            if a > self.pan() - (self.FOV/2) and a < self.pan() + (self.FOV/2):
                if ((math.cos(self.pan()) < 0) == (point[0] - self.x()<0)) or ((math.sin(self.pan()) < 0) == (point[2] - self.z()<0)):
                    return True
        return False

    def getPointLocation(self, point, screen):
        ##the x y and z locations relative to the camera
        x, y, z = point[0] - self.x(), point[1] - self.y(), point[2] - self.z()
        w, h = screen.get_size()
        vertFOV = self.FOV * (h/w)
        theta = self.FOV/2
        theta2 = vertFOV/2
        n = w/2
        n2 = h/2
        pxDis = math.sin(theta)/n
        pxDis2 = math.sin(theta2)/n2

        angle = math.atan(z/x) - self.pan()
        scalar = math.cos(theta)/math.cos(angle)
        disX = round((scalar*math.sin(angle))/pxDis)
        pixelX = n - disX
        
        disFromScreen = math.sqrt(x*x + z*z)*math.cos(angle)
        angleVert = math.atan(y/disFromScreen) - self.tilt()
        scalarVert = math.cos(theta2)/math.cos(angleVert)
        disY = round((scalarVert*math.sin(angleVert))/pxDis2)
        pixelY = n2 - disY

        return [pixelX, pixelY]

    
    def moveForward(self):
        self.location[0] += math.cos(self.pan()) * self.camSpeed
        self.location[2] += math.sin(self.pan()) * self.camSpeed

    def moveLeft(self):
        self.location[0] += math.sin(self.pan()) * self.camSpeed
        self.location[2] += math.cos(self.pan()) * self.camSpeed

    def moveBack(self):
        self.location[0] -= math.cos(self.pan()) * self.camSpeed
        self.location[2] -= math.sin(self.pan()) * self.camSpeed

    def moveRight(self):
        self.location[0] -= math.sin(self.pan()) * self.camSpeed
        self.location[2] -= math.cos(self.pan()) * self.camSpeed




        
