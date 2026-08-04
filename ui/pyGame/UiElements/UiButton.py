import pygame
from pygame import Rect

from ui.pyGame.UiElements.UiElement import UiElement


class UiButton(UiElement):
    def __init__(self, name, x, y, width, height, color, font, text, back_image, action, text_color = (0,0,0), border_radius = 10):
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

        self.clickable = True

        self.show = True

        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.text_color = text_color

        self.text_surface = font.render(str(text), True, self.text_color)
        self.text_rect = self.text_surface.get_rect()

        self.button_rect = Rect(x,y,width, height)
        self.text_rect.center = self.button_rect.center
        self.back_image = back_image
        self.action = action

        self.border_radius = border_radius
        self.animation_offset = 5
        self.clicked = False

        self.animate = self.button_rect.y + self.animation_offset

    def execute(self):
        try:
            result = self.action()
            return True if not result else result
        except Exception as e:
            print(f"Somehow an error accured:\n{e}")
            return False


    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.button_rect, border_radius=self.border_radius)
        surface.blit(self.text_surface, self.text_rect)

    def update(self):
        if self.clicked:
            self.button_rect.y = self.animate
        else:
            self.button_rect.y = self.y
        self.text_rect.center = self.button_rect.center
