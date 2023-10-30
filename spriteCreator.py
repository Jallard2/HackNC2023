import pygame
from utils import *

class SpriteCreator(pygame.sprite.Sprite):
    def __init__(self, height, width, imagePath, worldLocation: pygame.Vector2):
        super().__init__()

        self.height = height
        self.width = width

        self.worldLocation = worldLocation
        self.screenLocation = pygame.Vector2(0, 0)

        if imagePath != None:
            self.imageToUse = pygame.image.load(imagePath)
            self.imageToUse = pygame.transform.scale(self.imageToUse, (height, width))
            self.image = pygame.Surface([width, height])
            self.image.set_colorkey((0,0,0))
            self.image.blit(self.imageToUse, self.screenLocation)
        

            self.rect = self.image.get_rect()
            self.hasImage = True

        else:
            self.rect = pygame.Rect(0, 0, width, height)
            self.hasImage = False

        # pygame.draw.rect(self.image, (255,255,0), pygame.Rect(0,0, width, height))
        # pygame.draw.rect(self.image, (255,255,255), pygame.Rect(0,0, self.image.get_width(), self.image.get_height()))



    def update(self, backgroundX, backgroundY):
        self.screenLocation = worldToScreen(backgroundX, backgroundY, self.worldLocation.x, self.worldLocation.y)
        self.rect.center = self.screenLocation.x, self.screenLocation.y
