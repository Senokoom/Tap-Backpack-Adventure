from pygame import Rect

from ui.pyGame.UiElements.UiElement import UiElement


class UiDamage(UiElement):
    def __init__(self, x, y, width, height, font, number):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = font
        self.number = number

        self.default_color = (0, 0, 0)

        self.ended = False

        self.show = True
        self.clickable = False

        self.alpha = 255

        self.animation_speed = 5
        self.counter = 0

        self.speed_y = 3
        self.speed_x = 2
        self.speed_alpha = 10

        self.max_x = x + 10
        self.min_x = x - 10
        self.bounced = False

        self.text_box_rect = Rect(x, y, width, height)
        self.text_surface = font.render(str(number), True, self.default_color)

    def draw(self, surface):
        surface.blit(self.text_surface, self.text_box_rect)

    def update(self):
        if self.counter%self.animation_speed == 0:
            if self.bounced:
                self.x += self.speed_x
                if self.x >= self.max_x:
                    self.bounced = False
            else:
                self.x -= self.speed_x
                if self.x <= self.min_x:
                    self.bounced = True
            self.y -= self.speed_y
            self.alpha -= self.speed_alpha
            self.text_box_rect = Rect(self.x, self.y, self.width, self.height)
            self.text_surface = self.font.render(str(self.number), True, self.default_color)
            self.text_surface.set_alpha(self.alpha)
            self.counter = 0
        self.counter += 1
        if self.alpha == 0:
            self.ended = True