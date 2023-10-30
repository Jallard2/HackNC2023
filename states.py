import pygame
from utils import *
from player import Player
from spriteCreator import SpriteCreator
from farmland import FarmLand
from crop import Crop, DoneCrops
import random
import time
from ui import Button

# Abstract class for each State
class State():
    def __init__(self, game, screen: pygame.Surface):
        pass

    def draw(self):
        pass

    def update(self):
        pass

# The title screen state
class titleScreen(State):
    def __init__(self, game, screen: pygame.Surface):
        pass

    def draw(self):
        pass

    def update(self):
        pass

class mainGame(State):
    def __init__(self, game, screen: pygame.Surface, player: Player):
        self.game = game
        self.screen = screen
        self.player = player

        self.background = pygame.image.load(r"assets\mainState\HackNC_Background.png")
        self.background = pygame.transform.scale(self.background, (SCREEN_INFO))

        # self.soil = pygame.image.load(r"assets\mainState\soil.jpg")
        # self.soil = pygame.transform.scale(self.soil, (100,100))

        
        self.stateSpriteGroup = pygame.sprite.Group()
        y = 0
        for i in range(player.farmLand.numRows):
            x = 0
            for j in range(player.farmLand.numCols):
                if player.farmLand.land[i][j] == None:
                    self.soil = SpriteCreator(50, 50, r"assets\mainState\soil.jpg", pygame.Vector2(SCREEN_INFO[0] // 2 - 200 + x, 200 + y))
                elif player.farmLand.land[i][j].checkState() == "seed":
                    self.soil = SpriteCreator(50, 50, r"assets\mainState\soil.jpg", pygame.Vector2(SCREEN_INFO[0] // 2 - 200 + x, 200 + y))
                elif player.farmLand.land[i][j].checkState() == "growing":
                    self.soil = SpriteCreator(50, 50, r"assets\mainState\soil.jpg", pygame.Vector2(SCREEN_INFO[0] // 2 - 200 + x, 200 + y))
                elif player.farmLand.land[i][j].checkState() == "produce":
                    self.soil = SpriteCreator(50, 50, r"assets\mainState\soil.jpg", pygame.Vector2(SCREEN_INFO[0] // 2 - 200 + x, 200 + y))
                self.stateSpriteGroup.add(self.soil)
                x += 50
            y += 50
        self.stateSpriteGroup.add(player)
        


        self.backgroundX = 0
        self.backgroundY = 0

    def draw(self):
        self.screen.fill('black')
        self.screen.blit(self.background, (self.backgroundX, self.backgroundY))

    def update(self):
        # print(self.player.x, self.player.y)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.player.x - self.player.speed > 148:
            self.player.x -= self.player.speed
        if keys[pygame.K_d] and self.player.x + self.player.speed < 930:
            self.player.x += self.player.speed
        if keys[pygame.K_w] and self.player.y - self.player.speed > 112:
            self.player.y -= self.player.speed
        if keys[pygame.K_s] and self.player.y + self.player.speed < 586:
            self.player.y += self.player.speed

        self.stateSpriteGroup.update(self.backgroundX, self.backgroundY)
        self.stateSpriteGroup.draw(self.screen)

class overnightState(State):
    def __init__(self, game, screen: pygame.Surface, player: Player):
        self.game = game
        self.screen = screen
        self.player = player

        self.countDown = 3

        self.screen.fill('black')
        renderText("Overnight Report", 48, pygame.Color(255,255,255), self.screen, (SCREEN_INFO[0] // 2, 200))

        randomNumber = random.randrange(0, 100)
        if randomNumber < 30:
            bulletsLost = random.randrange(0, 5)
            foodLost = random.randrange(0, 5)
            player.bullets -= bulletsLost
            player.food -= foodLost
            renderText("You Were Raided in The Middle of the Night", 32, pygame.Color(255,255,255), self.screen, (SCREEN_INFO[0] // 2, 350))
            renderText(f"You Lost {bulletsLost} bullets and {foodLost} food", 32, pygame.Color(255,255,255), self.screen, (SCREEN_INFO[0] // 2, 385))
        
        elif randomNumber < 90:
            renderText("You Sleep Soundly As the Sun Comes Up", 32, pygame.Color(255,255,255), self.screen, (SCREEN_INFO[0] // 2, 350))
            
        else:
            renderText("The Sun Gently Wakes You Out of Bed", 32, pygame.Color(255,255,255), self.screen, (SCREEN_INFO[0] // 2, 350))
            renderText("Crops Have Grown 2x Their Normal Rate", 32, pygame.Color(255,255,255), self.screen, (SCREEN_INFO[0] // 2, 385))

        pygame.display.update()


    def draw(self):
        pass
    def update(self):
        time.sleep(1)
        self.countDown -= 1

        if (self.countDown == 0):
            self.game.state = mainGame(self.game, self.screen, self.player)
        

class StoreInterface(State):
    def __init__(self, game, screen, player):
        self.game = game
        self.screen = screen
        self.player = player

        self.backgroundX = 0
        self.backgroundY = 0

        self.inMenu = False

        self.stateSpriteGroup = pygame.sprite.Group()
    
        renderText("You Access the Store", 30, pygame.Color(255,255,255), self.screen, (SCREEN_INFO[0] // 2, 350))
        self.b = Button("Buy", 30, (255,255,255), self.screen, (100, 600), 100, 100, self.bFunction, r"assets\mainState\soil.jpg" )
        self.stateSpriteGroup.add(self.b.getSprite())
        # button.config(command=click)
        # button.config(font=('Ink Free',50,'bold'))

    def bFunction(self):
        print("Test")
        self.inMenu = False

    def draw(self):
        pass

    def update(self):
        mouse = pygame.mouse.get_pressed()
        if mouse[0] and not self.inMenu:
            if self.b.getSprite().rect.collidepoint(pygame.mouse.get_pos()):
                self.inMenu = True
                self.b.function()     
                
        self.stateSpriteGroup.update(self.backgroundX, self.backgroundY)
        self.stateSpriteGroup.draw(self.screen)
        

