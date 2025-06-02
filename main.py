''' [Make sure to fill out the program header as follows.]

Student Name: Rohan
Program Title: Graphics game 
Program Description: Halo 2600 8 bit recreation
Date Modified/Created: 2025-05-15
Course: ICD201-80

'''

import pygame, sys
from pygame.locals import *

pygame.init()

WINDOW = pygame.display.set_mode((1000, 880))
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LBLUE = (206, 255, 255)

FPS = 60

fpsClock = pygame.time.Clock()

pygame.display.set_caption("Hello World!")

x = 200
y = 200

while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    WINDOW.fill(LBLUE)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x = x - 2

    if keys[pygame.K_RIGHT]:
        x = x + 2

    if keys[pygame.K_UP]:
        y = y - 2

    if keys[pygame.K_DOWN]:
        y = y + 2

    if keys[pygame.K_a]:
        x = x - 2

    if keys[pygame.K_d]:
        x = x + 2

    if keys[pygame.K_w]:
        y = y - 2

    if keys[pygame.K_s]:
        y = y + 2

    img = pygame.image.load("halo standing.png")

    WINDOW.blit(img, (x, y))

    pygame.display.update()

    fpsClock.tick(FPS)

    # create the character and basic movement
    # create the first screen with walls
    # import character with animation
    # program all the key functionalities
    # add the ability to get to the next screen
    # create a gun that the character equips and fires with control
    # add trees and boxes for the player to hide behind
    # create a lives counter
    # create a menu screen
    # create enemies
    # have enemies follow player and shoot after the player shoots
    # add alternate inputs allowing the usage of wasd and mouse instead of arrow keys and ctrl
    # create a hud with the lives displayed
    # add powerups to protect the player from 1-2 projectiles