#!/bin/python3
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

    def draw(self):
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

        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.xSize, self.ySize))

#scene setup
class sceneBase:
   def __init__(self):
       self.next = self

   def ProcessInput(self, events):
       print("processInput")
   def update(self):
       print("update")
   def render(self, screen):
       print("render")
   def switchToNextScreen(self, next_scene):
       self.next = next_scene

class gameScene(sceneBase):
    def __init__(self):
        sceneBase.__init__(self)
    def ProcessInput(self, player1,pressed_keys):
        #pressed
        #x axis
        if pressed_keys[pygame.K_a]:
            player1.xVel -= player1.movementSpeed
        if pressed_keys[pygame.K_d]:
            player1.xVel += player1.movementSpeed

        #Y axis
        if pressed_keys[pygame.K_w]:
            player1.yVel -= player1.movementSpeed
        if pressed_keys[pygame.K_s]:
            player1.yVel += player1.movementSpeed

        #unpressed
        #X axis
        if not pressed_keys[pygame.K_a]:
            player1.xVel = 0
        if not pressed_keys[pygame.K_d]:
            player1.xVel = 0

        #Y axis
        if not pressed_keys[pygame.K_w]:
            player1.yVel = 0
        if not pressed_keys[pygame.K_s]:
            player1.yVel = 0
    def update(self):
        pass
    def render(self, player1):
        player1.draw()



def debug(player1):
    print("x",player1.x)
    print("y",player1.y)

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

player1 = player(10,10,BLUE, 50, 50, 0, 0, 1)

#pygame setup
import pygame

if __name__ == "__main__":
    active_scene = gameScene()
    HIGHT = 700
    WIDTH = 700
    pygame.init()
    screen = pygame.display.set_mode((HIGHT, WIDTH))
    pygame.display.set_caption("Game")
    while running:#gameloop
        pressed_keys=pygame.key.get_pressed()
        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        active_scene.ProcessInput(player1, pressed_keys)
        active_scene.update()
        active_scene.render(player1)
        # debug(player1)
        
        pygame.display.update()
