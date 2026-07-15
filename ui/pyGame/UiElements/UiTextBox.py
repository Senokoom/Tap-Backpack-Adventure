import pygame
from pygame import Rect
from ui.pyGame.UiElements.UiElement import UiElement

class UiTextBox(UiElement):
    def __init__(self, x, y, width, height,color, font, text_color, text_limit = 12, default_text_color = (90, 90, 90), default_text = "Введите имя..."):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.show = True

        self.clickable = True

        self.text_color = text_color

        self.default_text_color = default_text_color
        self.text_limit = text_limit

        self.text = ""

        self.font = font
        self.default_text = default_text
        self.text_box_rect = Rect(x, y, width, height)

        self.text_surface = font.render(str(default_text), True, self.default_text_color)
        self.text_rect = self.text_surface.get_rect(topleft=(self.text_box_rect.x + 5, self.text_box_rect.y + 10))

        self.animation_time = 100
        self.counter = 0
        self.clicked = False
        self.appear = False

    def draw(self, surface):
        if self.clicked:
            self.text_surface = self.font.render(str(f"{self.text}{'|' if self.appear else ''}"), True, self.text_color)
            self.text_rect = self.text_surface.get_rect(topleft=(self.text_box_rect.x + 5, self.text_box_rect.y + 10))
            if self.counter%self.animation_time==0:
                if self.appear:
                    self.appear = False
                else:
                    self.appear = True
                self.counter = 0
        else:
            self.text_surface = self.font.render(str(f"{self.default_text if self.text == "" else self.text}"), True, self.default_text_color if self.text == "" else self.text_color)
            self.text_rect = self.text_surface.get_rect(topleft=(self.text_box_rect.x + 5, self.text_box_rect.y + 10))
        pygame.draw.rect(surface, self.color, self.text_box_rect, border_radius=5)
        surface.blit(self.text_surface, self.text_rect)
        self.counter += 1


    def update(self):
        pass

    def handle_event(self, event):
        if self.clicked:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                self.clicked = False
            elif len(self.text) < self.text_limit:
                self.text += event.unicode

