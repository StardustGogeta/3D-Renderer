import pygame
from triangle import Triangle
from camera import Camera


        
        


testTriangle = Triangle((10,0,0),(0,10,0),(10,10,10))
testCamera = Camera()
print(testTriangle)
print(testCamera.triangleInFrame(testTriangle))
screen = pygame.display.set_mode((900,600))
screen.fill([50,50,50])
pygame.draw.polygon(screen, [255,255,255], testTriangle.givePoints2D(), 1)
pygame.display.update()
testCamera.getPointLocation(testTriangle.points[2], screen)
