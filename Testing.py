import pygame
from triangle import Triangle
from camera import Camera

testCamera = Camera()
screen = pygame.display.set_mode((900,600))
screen.fill([50,50,50])
triangles = []
##triangles.append(Triangle([10,-1,-1],[10,1,-1],[10,1,1], [255, 0, 255]))
##triangles.append(Triangle([10,-1,-1],[10,-1,1],[10,1,1]))
##triangles.append(Triangle([11,-1,-1],[11,1,-1],[11,1,1]))
##triangles.append(Triangle([11,-1,-1],[11,-1,1],[11,1,1]))
##triangles.append(Triangle([5, 0, 5],[6, 1, 6],[7, 4, 7]))
##for i in range(5):
##    triangles.append(Triangle([11+i,-1,-1],[11+i,1,-1],[11+i,1,1], [255 - 10*i, 255 - 10*i, 255 - 10*i]))
##    triangles.append(Triangle([11+i,-1,-1],[11+i,-1,1],[11+i,1,1], [255 - 10*i, 255 - 10*i, 255 - 10*i]))
##pygame.display.update()
WHITE = [255,255,255]
GREY = [127,127,127]
RED = [255,0,0]
GREEN = [0,255,0]
BLUE = [0,0,255]
YELLOW = [255,255,0]
BLACK = [0, 0 , 0 ]
PURPLE = [255, 0, 255]
'''triangles.append(Triangle([10,1,1], [10,1,-1], [10,-1,1],WHITE))
triangles.append(Triangle([10,-1,-1], [10,1,-1], [10,-1,1],WHITE))
triangles.append(Triangle([8,1,1], [8,1,-1], [8,-1,1],WHITE))
triangles.append(Triangle([8,-1,-1], [8,1,-1], [8,-1,1],WHITE))
triangles.append(Triangle([8,1,1], [10,1,1], [8,1,-1],RED))
triangles.append(Triangle([10,1,1], [10,1,-1], [8,1,-1],RED))
triangles.append(Triangle([8,-1,1], [10,-1,1], [8,-1,-1],RED))
triangles.append(Triangle([10,-1,1], [10,-1,-1], [8,-1,-1],RED))
triangles.append(Triangle([8,-1,-1], [10,-1,-1], [10,1,-1],BLUE))
triangles.append(Triangle([8,-1,-1], [8,1,-1], [10,1,-1],BLUE))
triangles.append(Triangle([8,-1,1], [10,-1,1], [10,1,1],BLUE))
triangles.append(Triangle([8,-1,1], [8,1,1], [10,1,1],BLUE))'''

##triangles.append(Triangle([0,0,0], [1,0,0], [0,1,0], WHITE))
'''triangles.append(Triangle([10,1,1], [10,1,-1], [10,-1,1],YELLOW))##Back
triangles.append(Triangle([10,-1,-1], [10,1,-1], [10,-1,1],YELLOW))
triangles.append(Triangle([1,0,1], [-1,0, 1], [1, 1,1],WHITE)) ##Front
triangles.append(Triangle([1,1,1], [-1,0, 1], [-1,1,1],WHITE)) 
triangles.append(Triangle([8,1,1], [10,1,1], [8,1,-1],RED)) ##Top
triangles.append(Triangle([10,1,1], [10,1,-1], [8,1,-1],RED))
triangles.append(Triangle([8,-1,1], [10,-1,1], [8,-1,-1],PURPLE)) ## Bottom
triangles.append(Triangle([10,-1,1], [10,-1,-1], [8,-1,-1],PURPLE))
triangles.append(Triangle([8,-1,-1], [10,-1,-1], [10,1,-1],BLUE)) ## Right side
triangles.append(Triangle([8,-1,-1], [8,1,-1], [10,1,-1],BLUE))
triangles.append(Triangle([8,-1,1], [10,-1,1], [10,1,1],GREEN)) ##Left Side
triangles.append(Triangle([8,-1,1], [8,1,1], [10,1,1],GREEN))'''


def updateFrame(screen, camera, triangles):
    triangles = sorted(triangles, key = lambda triangle: -triangle.avgDis(camera))
    screen.fill([50,50,50])
    for triangle in triangles:
        ##print(triangle.render(camera, screen))
        ##print(triangle.active)
        triangle.setActive(camera.triangleInFrame(triangle))
        ##print(camera.triangleInFrame(triangle))
        if triangle.active:
            pygame.draw.polygon(screen, triangle.color, triangle.render(camera, screen), 0)
    pygame.display.update()

gameExit = False

while gameExit != True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        gameEvent = event
        if gameEvent.type == pygame.QUIT:
            gameExit = True
    
    if keys[pygame.K_w]:
        testCamera.moveForward()
    if keys[pygame.K_a]:
        testCamera.moveLeft()
    if keys[pygame.K_s]:
        testCamera.moveBack()
    if keys[pygame.K_d]:
        testCamera.moveRight()
    if keys[pygame.K_SPACE]:
        testCamera.moveUp()
    if keys[pygame.K_LCTRL]:
        testCamera.moveDown()
    if keys[pygame.K_q]:
        testCamera.lookLeft()
    if keys[pygame.K_e]:
        testCamera.lookRight()
    if keys[pygame.K_i]:
        testCamera.lookUp()
    if keys[pygame.K_k]:
        testCamera.lookDown()
    ##print(testCamera.rotation[0])
    updateFrame(screen, testCamera, triangles)
    ##print(testCamera.x(), testCamera.z())
        
pygame.quit()
quit()
