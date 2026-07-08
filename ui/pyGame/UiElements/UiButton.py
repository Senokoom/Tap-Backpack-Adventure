import pygame
from pygame import Rect

from ui.pyGame.UiElements.UiElement import UiElement


class UiButton(UiElement):
    def __init__(self, name, x, y, width, height, color, font, text, back_image, action, screen):
        """
        :param x:
        :param y:
        :param width:
        :param height:
        :param color:
        :param text: font.render из pygame
        :param back_image: картинка, что будет позади текста, мб полупрозрачная
        :param action: функция из AppController.
        :param screen: ЯВЛЯЕТСЯ ТО, НА КАКОМ ЭКРАНЕ ДОЛЖНА ПОЯВИТСЯ КНОПКА
        """
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.text_surface = font.render(str(text), True, (0,0,0))
        self.text_rect = self.text_surface.get_rect()

        self.button_rect = Rect(x,y,width, height)
        self.text_rect.center = self.button_rect.center
        self.back_image = back_image
        self.action = action
        self.screen = screen

        self.border_radius = 10
        self.animation_offset = 5
        self.clicked = False

        self.animate = self.button_rect.y + self.animation_offset

    def draw(self, surface):
        if self.clicked:
            self.button_rect.y = self.animate
        else:
            self.button_rect.y = self.y
        self.text_rect.center = self.button_rect.center
        pygame.draw.rect(surface, self.color, self.button_rect, border_radius=self.border_radius)
        surface.blit(self.text_surface, self.text_rect)
