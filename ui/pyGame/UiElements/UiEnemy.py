from pygame.pixelcopy import surface_to_array

from ui.pyGame.UiElements.UiElement import UiElement
from ui.pyGame.UiSystem.Animation import Animation
import pygame

class UiEnemy(UiElement):
    def __init__(self, x, y, target_width, animation_idle, animation_hit, animation_die):
        self.x = x
        self.y = y
        self.animation_idle = Animation(animation_idle, target_width)
        self.animation_hit = Animation(animation_hit, target_width)
        self.animation_die = Animation(animation_die, target_width)

        self.animation_rect = pygame.Rect(x, y, *self.animation_idle.rect_size)

        self.animation_list = [self.animation_idle, self.animation_hit, self.animation_die]

        self.clickable = False
        self.show = True

        self.animation_speed = 30
        self.counter = 0


        self.current_animation = self.animation_idle


    def draw(self, surface):
            surface.blit(self.current_animation.get_frame(), self.animation_rect)

    def change_to_hit(self):
        self.reset_all_animations()
        self.current_animation = self.animation_hit

    def change_to_die(self):
        self.reset_all_animations()
        self.current_animation = self.animation_die

    def reset_all_animations(self):
        for anim in self.animation_list:
            anim.reset_animation()

    def update(self):
        if self.counter >= self.animation_speed:
            self.current_animation.change_frame_to_next()
            self.counter = 0
            if self.current_animation != self.animation_idle and self.current_animation.is_last_frame():
                self.current_animation = self.animation_idle
        self.counter += 1