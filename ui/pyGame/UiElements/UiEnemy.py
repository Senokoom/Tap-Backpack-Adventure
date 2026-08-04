import humanize

from classes.AppController import AppController
from ui.pyGame.UiElements.UiDamage import UiDamage
from ui.pyGame.UiElements.UiElement import UiElement
from ui.pyGame.UiElements.UiProgressBar import UiProgressBar
from ui.pyGame.UiSystem.Animation import Animation
import pygame

from ui.ui_config import UiConfig


class UiEnemy(UiElement):
    def __init__(self, x, y, target_width, animation_idle, animation_hit, animation_die, controller: AppController):
        self.x = x
        self.y = y
        self.animation_idle = Animation(animation_idle, target_width)
        self.animation_hit = Animation(animation_hit, target_width)
        self.animation_die = Animation(animation_die, target_width)

        self.controller = controller

        self.hp_bar = UiProgressBar(210, 30, 400, 30, (255, 0,0),
                                             (0,0,0), 500, 400, pygame.font.Font(UiConfig.game_font, 20))

        self.animation_rect = pygame.Rect(0, 0, *self.animation_idle.rect_size)

        self.animation_rect.midbottom = (x,y)


        self.animation_list = [self.animation_idle, self.animation_hit, self.animation_die]

        self.current_hp, self.max_hp = self.controller.get_enemy_hp_info()

        self.clickable = False
        self.show = True

        self.animation_speed = 30
        self.counter = 0

        self.damage_text_list = []

        self.current_animation = self.animation_idle

    def hit(self, mouse_pos):
        x,y = mouse_pos
        self.damage_text_list.append(UiDamage(x, y, 100, 100, pygame.font.Font(UiConfig.game_font, 20), int(self.controller.get_last_damage())))
        self.change_to_hit()

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), self.animation_rect, 1)
        pygame.draw.line(surface, (255, 0, 0), (0, self.y), (800, self.y), 2)
        surface.blit(self.current_animation.get_frame(), self.animation_rect)
        self.hp_bar.draw(surface)
        if self.damage_text_list:
            for damage in self.damage_text_list:
                damage.draw(surface)

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
        if self.damage_text_list:
            for damage in self.damage_text_list:
                damage.update()
                if damage.ended:
                    self.damage_text_list.remove(damage)
        if self.counter >= self.animation_speed:
            self.current_animation.change_frame_to_next()
            self.counter = 0
            if self.current_animation != self.animation_idle and self.current_animation.is_last_frame():
                self.current_animation = self.animation_idle
        self.counter += 1
        self.current_hp, self.max_hp = self.controller.get_enemy_hp_info()
        self.hp_bar.progress_bar_value, self.hp_bar.progress_bar_max = self.current_hp, self.max_hp
        if self.current_hp <= 0:
            self.change_to_die()