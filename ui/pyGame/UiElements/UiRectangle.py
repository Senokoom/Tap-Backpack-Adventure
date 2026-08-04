import pygame.draw
from pygame import Rect

from ui.pyGame.UiElements.UiElement import UiElement


class UiRectangle(UiElement):
    def __init__(self, x,y,width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.show = True
        self.clickable = False

        self.border_radius = 10

        self.rect = Rect(x, y, width, height)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=self.border_radius)

    def update(self):
        self.rect = Rect(self.x, self.y, self.width, self.height)
