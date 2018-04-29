#sources 
# Pygame spiral drawing function
# Copyright David Barker 2010
#PROGRamarcadegames.com
#https://inventwithpython.com/pygame/chapter2.html
#https://www.pygame.org/project/1649/2871
#http://www.pygame.org/project-DrawSpiral()+function-1649-.html



import pygame, sys, math
import random
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

# set up the window
screen = pygame.display.set_mode((1248, 750), 0, 32)
pygame.display.set_caption('Animation')

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'right'


def DrawSpiral(display, pos, radius, rotation = math.pi, numSpokes = 1, clockwise = True, startAngle = 0.0):
    """DrawSpiral(display, pos, radius, rotation = math.pi, numSpokes = 1, clockwise = True, startAngle = 0): return None
   Draws a spiral at the given position.
   Arguments:
       -display: the pygame.Surface object to draw to
       -pos: a tuple for the position of the centre of the spiral
       -radius: the radius of the spiral
       -rotation: the angle through which a single spoke will have turned by the time it reaches its end
       -numSpokes: the number of spokes to draw
       -clockwise: a boolean variable specifying which direction the spiral should turn in
       -startAngle: the starting angle of the first spoke
   """
    radius = 200.0
    resolution = radius / 2.0
    radiusIncrement = radius / resolution
    rotationIncrement = rotation / resolution
    spokeRotationIncrement = (math.pi * 2.0) / float(numSpokes)
    spokeRotation = startAngle
 
    if clockwise:
        direction = -1
    else:
        direction = 1
 
    for i in range(0, numSpokes):
        spoke = []
        spoke.append(pos)
 
        curAngle = spokeRotation
        curRadius = 0.0
 
        while curRadius <= radius:
            newx = curRadius * math.sin(curAngle)
            newy = curRadius * math.cos(curAngle)
            spoke.append((pos[0] + newx, pos[1] + (direction * newy)))
 
            curRadius += radiusIncrement
            curAngle += rotationIncrement
 
        pygame.draw.aalines(display, (0, 0, 255), False, spoke)
        
        spokeRotation += spokeRotationIncrement
 

curRad = 20.0
curRot = math.pi
startAngle = 0.0

    
background_image = pygame.image.load("FL_map.png").convert()




while True: # the main game loop
    background_position = [0, 0]
    
    screen.blit(background_image, background_position)
    
    DrawSpiral(screen, pos = pygame.mouse.get_pos(), radius = curRad, rotation = curRot, numSpokes = 5, clockwise = True, startAngle = startAngle)

    curRad += 2.0
    curRot += 0.1
    startAngle -= 0.05

    
    if direction == 'right':
        catx += 5
        if catx == 1100:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 600:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'

   

    screen.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(20)

