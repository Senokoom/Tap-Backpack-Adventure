from ui.pyGame.UiElements.UiElement import UiElement
import pygame

class UiAnimatedLogo(UiElement):
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pygame.transform.smoothscale(image, (450, 252))

        self.show = True

        self.clickable = False

        self.animation_speed = 6
        self.counter = 0
        self.up_border = self.y - 10
        self.down_border = self.y + 10
        self.bumped = False


        self.an_y = self.y


    def draw(self, surface):
        surface.blit(self.image, (self.x, self.an_y))


    def update(self):
        if self.counter % self.animation_speed == 0:
            if self.bumped and self.an_y > self.up_border:
                self.an_y -= 1
                if self.an_y <= self.up_border:
                    self.bumped = False
            elif not self.bumped and self.an_y < self.down_border:
                self.an_y += 1
                if self.an_y >= self.down_border:
                    self.bumped = True
            self.counter = 0
        self.counter += 1
