from re import X
import pygame

class knife:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.damage = 5
        self.attkDist = 30
        self.weight = 1
        self.stackability = 1
    def obtain(player1):
        player1.inventory["knife"] = 1
    def spawn(self, screen):
        return pygame.draw.rect(screen, (0,0,0), pygame.Rect(self.x,self.y, 30,30))

class meat:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.replenish = 5
        self.weight = 3
        self.stackability = 30
    def obtain(player1):
        player1.inventory["meat"] = 30

    def spawn(self, screen):
       return pygame.draw.rect(screen, (255,0,0), pygame.Rect(self.x,self.y, 30,30))

class pistol:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.damage = 30
        self.attkDist = 200
        self.weight = 7
        self.stackability = 1
    def obtain(player1):
        player1.inventory["pistol"] = 1

    def draw(self, screen):
       return pygame.draw.rect(screen, (0,255,0), pygame.Rect(self.x, self.y, 30, 30))
