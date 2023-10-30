import pygame
from sys import exit

from utils import *
from states import *
from player import Player


class Game():
    def __init__(self):
        # Initializing pygame library
        pygame.init()
        pygame.display.set_caption("NC Hackathon 2023")

        # The clock of the game
        self.clock = pygame.time.Clock()

        # The Screen to render to
        self.screen: pygame.Surface = pygame.display.set_mode(SCREEN_INFO)

        # Player initialization
        player = Player(35, 25)

        # The state of the game (its a state class)
        # self.state = mainGame(self, self.screen, player)
        # self.state: State = overnightState(self, self.screen, player)
        self.state = StoreInterface(self, self.screen, player)


        # Should the game be running
        self.runner = True

    # Checks if the user asked to quit the game
    def checkForExit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    # Main event loop of the game
    def run(self):
        while self.runner:
            self.checkForExit()

            self.state.draw()
            self.state.update()

            pygame.display.update()

            # print(pygame.mouse.get_pos())

            self.clock.tick(60)
        



        

if __name__ == "__main__":
    x = Game()
    x.run()
    pygame.quit()