import math
from warnings import catch_warnings
from symbol import except_clause

class Camera(object):
    def __init__(self, x = 0, y = 0, z = 0, pan = 0, tilt = 0):
        self.location = [x, y, z]
        self.rotation = [pan, tilt]
        self.FOV = 2*math.pi/3
        self.camSpeed = 0.01
        self.camRotSpeed = math.pi/900
        
        ##self.FOVv = 4*math.pi/9
    @property
    def x(self):
        return self.location[0]

    @property
    def y(self):
        return self.location[1]

    @property
    def z(self):
        return self.location[2]

    @property
    def pan(self):
        return self.rotation[0]

    @property
    def tilt(self):
        return self.rotation[1]

    def triangleInFrame(self, triangle):
        ##print(triangle.coversCamera(self))
##        if triangle.coversCamera(self):
##            return False
        for point in triangle.points:
            try:
                a = math.atan((point[2] - self.z)/(point[0] - self.x))
            except:
                a = math.pi /2
                
            if point[0] - self.x < 0:
                a += math.pi
            ##print(a)
            if (a > self.pan - (self.FOV/2) and a < self.pan + (self.FOV/2)) or(a + (math.pi*2) > self.pan - (self.FOV/2) and a + (math.pi*2) < self.pan + (self.FOV/2)):
                ##if ((math.cos(self.pan()) < 0) == (point[0] - self.x()<0)) or ((math.sin(self.pan()) < 0) == (point[2] - self.z()<0)):
                    return True
        return False

    def getPointLocation(self, point, screen):
        ##the x y and z locations relative to the camera
        x, y, z = point[0] - self.x, point[1] - self.y, point[2] - self.z
        w, h = screen.get_size()
        vertFOV = self.FOV * (h/w)
        theta = self.FOV/2
        theta2 = vertFOV/2
        n = w/2
        n2 = h/2
        pxDis = math.sin(theta)/n
        pxDis2 = math.sin(theta2)/n2
        
        try:
            angle = math.atan(z/x) - self.pan
        except:
            angle = math.pi /2 -self.pan; 
        
        scalar = math.cos(theta)/math.cos(angle)
        disX = round((scalar*math.sin(angle))/pxDis)
        pixelX = n - disX
        
        if x < 0:
            y *= -1
        disFromScreen = math.sqrt(x*x + z*z)*math.cos(angle)
        try:
            angleVert = math.atan(y/disFromScreen) - self.tilt
        except:
            angleVert = math.pi/2 -self.tilt
        scalarVert = math.cos(theta2)/math.cos(angleVert)
        disY = round((scalarVert*math.sin(angleVert))/pxDis2)
        pixelY = n2 - disY
        return [pixelX, pixelY]

    
    def moveForward(self):
        self.location[0] += math.cos(self.pan) * self.camSpeed
        self.location[2] += math.sin(self.pan) * self.camSpeed

    def moveLeft(self):
        self.location[0] -= math.sin(self.pan) * self.camSpeed
        self.location[2] += math.cos(self.pan) * self.camSpeed

    def moveBack(self):
        self.location[0] -= math.cos(self.pan) * self.camSpeed
        self.location[2] -= math.sin(self.pan) * self.camSpeed

    def moveRight(self):
        self.location[0] += math.sin(self.pan) * self.camSpeed
        self.location[2] -= math.cos(self.pan) * self.camSpeed

    def moveUp(self):
        self.location[1] += self.camSpeed

    def moveDown(self):
        self.location[1] -= self.camSpeed

    def lookLeft(self):
        self.rotation[0] += self.camRotSpeed
        self.rotation[0] = self.rotation[0] % (math.pi*2)

    def lookRight(self):
        self.rotation[0] -= self.camRotSpeed
        self.rotation[0] = self.rotation[0] % (math.pi*2)

    def lookUp(self):
        if self.rotation[1] + self.camRotSpeed < math.pi/2:
            self.rotation[1] += self.camRotSpeed

    def lookDown(self):
        if self.rotation[1] - self.camRotSpeed > -math.pi/2:
            self.rotation[1] -= self.camRotSpeed

