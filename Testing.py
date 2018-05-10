import pygame
from triangle import Triangle
from camera import Camera

testCamera = Camera()
screen = pygame.display.set_mode((900,600))
screen.fill([50,50,50])
triangles = []
triangles.append(Triangle([10,-1,-1],[10,1,-1],[10,1,1]))
triangles.append(Triangle([10,-1,-1],[10,-1,1],[10,1,1]))
triangles.append(Triangle([11,-1,-1],[11,1,-1],[11,1,1]))
triangles.append(Triangle([11,-1,-1],[11,-1,1],[11,1,1]))
pygame.display.update()

def updateFrame(screen, camera, triangles):
    screen.fill([50,50,50])
    for triangle in triangles:
        ##print(triangle.render(camera, screen))
        ##print(triangle.active)
        triangle.setActive(camera.triangleInFrame(triangle))
        ##print(camera.triangleInFrame(triangle))
        if triangle.active:
            pygame.draw.polygon(screen, [255,255,255], triangle.render(camera, screen), 1)
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
    updateFrame(screen, testCamera, triangles)
    ##print(testCamera.x(), testCamera.z())

##    if gameEvent.key == 'space':
##        testCamera.moveUp(0.1)
##    if gameEvent.key == 'ctrl':
##        testCamera.moveDown(0.1)
##    if gameEvent.key == 'i':
##        testCamera.lookUp(0.1)
##    if gameEvent.key == 'j':
##        testCamera.lookLeft(0.1)
##    if gameEvent.key == 'k':
##        testCamera.lookDown(0.1)
##    if gameEvent.key == 'l':
##        testCamera.lookRight(0.1)
        
pygame.quit()
quit()
