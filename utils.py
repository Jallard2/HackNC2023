import pygame

# Screen size 
SCREEN_INFO = (1080, 720)

# Converting from a pygame location to a screen location 
def worldToScreen(backgroundX: int, backgroundY: int, x: int, y: int) -> pygame.Vector2:
    screenLocation = pygame.Vector2(x + backgroundX + 20, y + backgroundY - 20)
    return screenLocation


def renderText(text: str, size: int, color, screen: pygame.Surface, screenLocation: tuple[int , int]):
    font = pygame.font.Font('freesansbold.ttf', size)
    text: pygame.Surface = font.render(text, True, color)
    textRect: pygame.Rect = text.get_rect()
    textRect.center = screenLocation
    # textRect.center = (textRect.topleft[0] - textRect.width / 2, textRect.topleft[1])
    screen.blit(text, textRect)

