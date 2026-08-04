import pygame
from pygame import Rect

from ui.pyGame.UiElements.UiElement import UiElement


class UiLevelUp(UiElement):
    def __init__(self, x, y, width, height, font, text_color, points_amount, action):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.text_color = text_color
        self.font = font

        self.points_amount = points_amount

        self.clickable = True
        self.show = True

        self.animation_speed = 5
        self.alpha = 255

        self.min_alpha = 100
        self.max_alpha = 255

        self.alpha_speed = 20

        self.counter = 0

        self.bounced = True

        self.text_box_rect = Rect(x, y, width, height)
        self.text_surface = font.render(str(f"! {self.points_amount}"), True, self.text_color)

        self.action = action

    def draw(self, surface):
        # pygame.draw.rect(surface, (0, 255, 0), self.text_box_rect, 1)
        surface.blit(self.text_surface, self.text_box_rect)


    def execute(self):
        self.action()

    def update(self):
        if self.counter >= self.animation_speed:
            if self.bounced:
                self.alpha -= self.alpha_speed
                if self.alpha <= self.min_alpha:
                    self.bounced = False
            else:
                self.alpha += self.alpha_speed
                if self.alpha >= self.max_alpha:
                    self.alpha = 255
                    self.bounced = True
            self.text_box_rect = Rect(self.x, self.y, self.width, self.height)
            self.text_surface = self.font.render(str(f"! {self.points_amount}"), True, self.text_color)
            self.text_surface.set_alpha(self.alpha)
            self.counter = 0
        self.counter += 1
