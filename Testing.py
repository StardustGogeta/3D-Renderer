import pygame
from triangle import Triangle
from camera import Camera

testCamera = Camera()
screen = pygame.display.set_mode((900,600))
screen.fill([50,50,50])
triangles = []
triangles.append(Triangle([10,-1,-1],[10,1,-1],[10,1,1], [255, 0, 255]))
triangles.append(Triangle([10,-1,-1],[10,-1,1],[10,1,1]))
triangles.append(Triangle([11,-1,-1],[11,1,-1],[11,1,1]))
triangles.append(Triangle([11,-1,-1],[11,-1,1],[11,1,1]))
for i in range(5):
    triangles.append(Triangle([11+i,-1,-1],[11+i,1,-1],[11+i,1,1]))
    triangles.append(Triangle([11+i,-1,-1],[11+i,-1,1],[11+i,1,1]))
pygame.display.update()

def updateFrame(screen, camera, triangles):
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
    ##print(testCamera.rotation[0])
    updateFrame(screen, testCamera, triangles)
    ##print(testCamera.x(), testCamera.z())
        
pygame.quit()
quit()
