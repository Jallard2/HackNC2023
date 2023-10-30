import pygame
from utils import *
from farmland import FarmLand

class Player(pygame.sprite.Sprite):
    def __init__(self, height: int, width: int):
        super().__init__()
        self.height = height
        self.width = width

        self.x = SCREEN_INFO[0] // 2
        self.y = SCREEN_INFO[1] // 2

        self.image = pygame.Surface([width, height]) 
        self.image.fill('white') 
        self.image.set_colorkey('white') 

        pygame.draw.rect(self.image, 'black', pygame.Rect(0, 0, width, height)) 

        self.farmLand: FarmLand = FarmLand()

        self.rect = self.image.get_rect() 
        self.rect.center = (self.x, self.y)
        # self.rect.center = (SCREEN_INFO[0] // 2 - self.height // 2 + self.y, SCREEN_INFO[1] // 2 - self.x)

        self.speed = 2  

        self.money = 100
        self.food = 0
        self.bullets = 0

        self.hasImage = True

        self.day = 1

    def update(self, backgroundX, backgroundY):
        self.rect.center = (self.x, self.y)