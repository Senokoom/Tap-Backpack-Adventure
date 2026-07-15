from pygame import Rect

from ui.pyGame.UiElements.UiElement import UiElement
import pygame

class UiLabel(UiElement):
    def __init__(self, x, y, width, height, font, text, text_color):
        self.x = x
        self.y = y
        self.font = font
        self.text = text
        self.text_color = text_color

        self.clickable = False

        self.show = True

        self.text_box_rect = Rect(x, y, width, height)
        self.text_surface = font.render(str(text), True, self.text_color)

    def draw(self, surface):
        surface.blit(self.text_surface, self.text_box_rect)

    def update(self):
        pass

    def handle_event(self):
        pass

