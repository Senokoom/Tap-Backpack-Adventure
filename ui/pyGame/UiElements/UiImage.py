from ui.pyGame.UiElements.UiElement import UiElement
import pygame

class UiImage(UiElement):
    def __init__(self, x, y, image, scale, screen):
        self.x = x
        self.y = y
        self.image = pygame.transform.smoothscale(image, scale)

        self.screen = screen

        self.show = True
        self.clickable = False

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def update(self):
        pass