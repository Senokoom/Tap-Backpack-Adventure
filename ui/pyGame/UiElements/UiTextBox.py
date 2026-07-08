import pygame
from pygame import Rect
from ui.pyGame.UiElements.UiElement import UiElement

class UiTextBox(UiElement):
    def __init__(self, x, y, width, height,color, font, screen, text = "Введите имя..."):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.inserted_text = ""

        self.screen = screen
        self.font = font
        self.text = text
        self.text_box_rect = Rect(x, y, width, height)

        self.text_surface = font.render(str(text), True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect(topleft=(self.text_box_rect.x + 5, self.text_box_rect.y + 10))

        self.animation_time = 250
        self.counter = 0
        self.clicked = False
        self.appear = False

    def draw(self, surface):
        if self.clicked:
            if self.counter%self.animation_time==0:
                if not self.appear:
                    self.text_surface = self.font.render(str(f"{self.inserted_text}|"), True, (0,0,0))
                    self.text_rect = self.text_surface.get_rect(topleft=(self.text_box_rect.x + 5, self.text_box_rect.y + 10))
                    self.appear = True
                else:
                    self.text_surface = self.font.render(str(self.inserted_text), True, (0, 0, 0))
                    self.text_rect = self.text_surface.get_rect(
                        topleft=(self.text_box_rect.x + 5, self.text_box_rect.y + 10))
                    self.appear = False
        elif not self.clicked and self.inserted_text == "":
            self.text_surface = self.font.render(str(self.text), True, (0, 0, 0))
            self.text_rect = self.text_surface.get_rect(topleft=(self.text_box_rect.x + 5, self.text_box_rect.y + 10))
        if not self.clicked and self.inserted_text != "":
            self.text_surface = self.font.render(str(self.inserted_text), True, (0, 0, 0))
            self.text_rect = self.text_surface.get_rect(topleft=(self.text_box_rect.x + 5, self.text_box_rect.y + 10))
        pygame.draw.rect(surface, self.color, self.text_box_rect, border_radius=5)
        surface.blit(self.text_surface, self.text_rect)
        self.counter += 1

