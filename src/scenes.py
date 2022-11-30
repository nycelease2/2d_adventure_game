import pygame
from main import *

def MainGame(pygame, player1, screen, colors, item, visibleSprites, clock, curscreen, scenesList):#main game scene
    while curscreen==scenesList[0]:#main gameloop
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

                #MainMenu
                if event.key == pygame.K_ESCAPE:
                    print("Main Menu Starting")
                    curscreen=scenesList[1]

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
        # debug(player1)
        clock.tick(500)

def MainMenu(pygame, player1, screen, colors, item, visibleSprites, clock, curscreen, scenesList):
    while True:
        pass
