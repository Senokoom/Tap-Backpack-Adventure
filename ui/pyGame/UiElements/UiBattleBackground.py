from ui.pyGame.UiElements.UiCloud import UiCloud
from ui.pyGame.UiElements.UiElement import UiElement
import pygame
from random import randint, choice


class UiBattleBackground(UiElement):
    def __init__(self, x, y, image, scale, clouds, screen, action):
        """
        clouds - Путь к картинкам
        """
        self.width, self.height = scale

        self.action = action

        self.enemy = 0

        self.x = x
        self.y = y
        self.image = pygame.transform.smoothscale(image, scale)

        self.show = True

        self.screen = screen
        self.clickable = True

        self.clicked = False

        self.cloud_min_y = self.y - int(self.height * 0.3)
        self.cloud_max_y = self.y + int(self.height * 0.2)

        self.cloud_max_x = self.x

        self.cloud_min_size = (150, 80)
        self.cloud_max_size = (220, 100)

        self.cloud_min_speed = 10
        self.cloud_max_speed = 15

        self.cloud_alpha_min = 100
        self.cloud_alpha_max = 200

        self.max_clouds = 6

        self.cloud_chance = 1 # /1000
        self.clouds = clouds

        self.can_generate = True
        self.wait_timer = 1000
        self.counter = 1

        self.clouds_list = []

    def execute(self):
        try:
            result = self.action()
            self.enemy.change_to_hit()
            return True if not result else result
        except Exception as e:
            print(f"Somehow an error accured:\n{e}")
            return False

    def draw(self, surface):
        if randint(0, 200) and self.can_generate:
            self.can_generate = False
            self.spawn_cloud()
        surface.blit(self.image, (self.x, self.y))
        if self.clouds_list:
            self.update()
            for cloud in self.clouds_list:
                cloud.draw(surface)
        if not self.can_generate:
            if self.counter % self.wait_timer == 0:
                self.can_generate = True
                self.counter = 0
            self.counter += 1

    def update(self):
        if self.clouds_list:
            for cloud in self.clouds_list:
                if cloud.finished:
                    self.clouds_list.remove(cloud)
                else:
                    cloud.update()


    def spawn_cloud(self):
        if len(self.clouds_list) < self.max_clouds:
            self.clouds_list.append(
                UiCloud(self.x + self.width, randint(self.cloud_min_y, self.cloud_max_y), choice(self.clouds),
                        randint(self.cloud_min_speed, self.cloud_max_speed),
                        self.cloud_max_x, (randint(self.cloud_min_size[0], self.cloud_max_size[0]), randint(self.cloud_min_size[1], self.cloud_max_size[1])),
                        randint(self.cloud_alpha_min, self.cloud_alpha_max))
            )