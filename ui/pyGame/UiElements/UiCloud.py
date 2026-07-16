from ui.pyGame.UiElements.UiElement import UiElement
import pygame

class UiCloud(UiElement):
    def __init__(self, x, y, image, speed, max_x, scale, alpha):
        self.x = x
        self.y = y
        self.width, self.height = scale
        self.image = pygame.transform.smoothscale(image, scale)
        self.image.set_alpha(alpha)
        self.clickable = False
        self.speed = speed

        self.counter = 0
        self.max_x = max_x

        self.finished = False


    def update(self):
        self.counter += 1
        if self.counter % self.speed == 0:
            self.x -= 1
            self.counter = 0
        if self.x + self.width <= self.max_x:
            self.finished = True


    def draw(self, surface):
        if not self.finished:
            surface.blit(self.image, (self.x, self.y))
    
