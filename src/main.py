#!/bin/python3
import items
running = True


class player:
    def __init__(self, x, y, color, xSize, ySize, xVel, yVel, movementSpeed):
        self.x = x
        self.y = y
        self.color = color
        self.xSize = xSize
        self.ySize = ySize
        self.xVel = xVel
        self.yVel = yVel
        self.movementSpeed = movementSpeed
        self.inventory = {"knife": 0, "meat":0, "pistol":0}
        self.maxweightCarry = 100
        self.sprite = None

    def draw(self, screen):
        self.x += self.xVel
        self.y += self.yVel

        if self.x < 0:
            self.x = 0
        if self.x > WIDTH-self.xSize:
            self.x = WIDTH-self.xSize

        if self.y < 0:
            self.y = 0
        if self.y > HIGHT-self.ySize:
            self.y = HIGHT-self.ySize

        self.sprite = pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.xSize, self.ySize))

#variables
AQUA = ( 0, 255, 255)
BLACK = ( 0, 0, 0)
BLUE = ( 0, 0, 255)
FUCHISIA = (255, 0, 255)
GRAY = (128, 128, 128)
GREEN = ( 0, 128, 0)
LIME = ( 0, 255, 0)
MAROON = (128, 0, 0)
NAVYBLUE = ( 0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
SILVER = (192, 192, 192)
TEAL = ( 0, 128, 128)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BG = (30,30,30)

#items intialization
PISTOL = items.pistol(100, 70)
MEAT = items.meat(400,500)
KNIFE = items.knife(500,300)

item = [PISTOL, MEAT,KNIFE]

player1 = player(10,10,BLUE, 50, 50, 0, 0, 0.3)
visibleSprites=[player1, PISTOL, KNIFE, MEAT]
def updateScreen(visibleSprites):
    for i in visibleSprites:
        i.draw(screen)

#pygame setup
import pygame

def itemGetCheck(itemtocheck, player1):
    if pygame.Rect.colliderect(itemtocheck.sprite, player1.sprite):
        itemtocheck.obtain(player1)

def debug(player1):
    print(player1.inventory)

if __name__ == "__main__":
    HIGHT = 700
    WIDTH = 700
    pygame.init()
    screen = pygame.display.set_mode((HIGHT, WIDTH))
    pygame.display.set_caption("Game")
    clock = pygame.time.Clock()
    while running:#gameloop
        #event handling
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

        
        screen.fill(BG)
        updateScreen(visibleSprites)
        for i in item:
            itemGetCheck(i, player1)
        pygame.display.update()
        debug(player1)
        clock.tick(500)
