import pygame
from spriteCreator import SpriteCreator
from utils import *
class Button:
    def __init__(self, text, size, color, screen: pygame.Surface, screenLocation, height, width, function, image):
        self.function = function
        self.im = SpriteCreator(height, width, image, pygame.Vector2(screenLocation[0], screenLocation[1]) )

        renderText(text, size, color, screen, screenLocation)
    
    def getSprite(self):
        return self.im
    