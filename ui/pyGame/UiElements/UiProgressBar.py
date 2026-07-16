from pygame import Rect

from ui.pyGame.UiElements.UiElement import UiElement
import pygame

class UiProgressBar(UiElement):
    def __init__(self, x, y, width, height, progress_bar_color, outline_color, progress_bar_max, progress_bar_value, font, text_color = (0,0,0), back_color = (150, 150, 150), outline_width = 4):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.progress_bar_color = progress_bar_color
        self.outline_color = outline_color
        self.progress_bar_max = progress_bar_max
        self.progress_bar_value = progress_bar_value

        self.show = True

        self.clickable = False

        self.font = font
        self.text_color = text_color

        self.back_color = back_color
        self.outline_width = outline_width

        self.progress_bar_rect = Rect(x, y, width, height)

        self.text_surface = font.render(str(f"{self.progress_bar_value} / {progress_bar_max}"), True, self.text_color)
        self.text_rect = self.text_surface.get_rect()

        self.text_rect.center = self.progress_bar_rect.center


    def draw(self, surface):
        pygame.draw.rect(surface, self.back_color, self.progress_bar_rect, border_radius=2)

        current_progress_bar_rect = Rect(self.x, self.y,
                                         int(self.width*(self.progress_bar_value/self.progress_bar_max)), self.height)

        pygame.draw.rect(surface, self.progress_bar_color, current_progress_bar_rect, border_radius=2)

        pygame.draw.rect(surface, self.outline_color, self.progress_bar_rect, width=self.outline_width, border_radius=2)

        self.text_surface = self.font.render(str(f"{self.progress_bar_value} / {self.progress_bar_max}"), True, self.text_color)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = self.progress_bar_rect.center
        surface.blit(self.text_surface, self.text_rect)



    def update(self):
        pass