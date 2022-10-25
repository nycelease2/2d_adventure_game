import pygame
from main import *

def MainGame(pygame, player1, screen, colors, item, visibleSprites, clock):#main game scene
    while True:#main gameloop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            #controls
            if event.type == pygame.KEYDOWN:
                #X axis
                if event.key == pygame.K_a:
                    player1.xVel -= player1.movementSpeed
                if event.key == pygame.K_d:
                    player1.xVel += player1.movementSpeed

                #Y axis
                if event.key == pygame.K_w:
                    player1.yVel -= player1.movementSpeed
                if event.key == pygame.K_s:
                    player1.yVel += player1.movementSpeed

            if event.type == pygame.KEYUP:
                #X axis
                if event.key == pygame.K_a:
                    player1.xVel = 0
                if event.key == pygame.K_d:
                    player1.xVel = 0

                #Y axis
                if event.key == pygame.K_w:
                    player1.yVel = 0
                if event.key == pygame.K_s:
                    player1.yVel = 0
        screen.fill(colors["BG"])
        updateScreen(visibleSprites, screen)
        for i in item:
            itemGetCheck(i, player1)
        pygame.display.update()
        debug(player1)
        clock.tick(500)

def MainMenu(pygame):
    while True:
        pass
