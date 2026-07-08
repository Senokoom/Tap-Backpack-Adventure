import pygame
import sys

from classes.AppController import AppController
from ui.pyGame.UiElements.UiTextBox import UiTextBox
from ui.ui_config import ImagePaths
from ui.pyGame.UiElements.UiAnimatedLogo import UiAnimatedLogo
from ui.pyGame.UiElements.UiButton import UiButton


class PyGameWindow:
    def __init__(self, app_controller: AppController, window=0):
        """
        :param window: текущее окно. 0 - Главное меню
        """
        pygame.init()
        self.AppController = app_controller
        self.screen = pygame.display.set_mode((800, 600))
        self.objects = []
        self.objects_on_screen = []
        self.window = window

        self.init_objects()
        self.init_objects_on_screen()

        self.main_loop()


    def init_objects(self):
        self.objects.append(UiAnimatedLogo(145, 20, pygame.image.load(ImagePaths.logo_path), 0))
        # self.objects.append(UiButton("testbutton", 100, 100, 50, 50, (0, 255, 0),
        #              pygame.font.SysFont('couriernew', 20), "TEST", 0, False, 0))
        self.objects.append(UiButton("NewGame", 315, 380, 180, 70, (153, 90, 8),
                                     pygame.font.Font(ImagePaths.game_font, 20), "New Game", 0,
                                     0, 0))
        self.objects.append(UiButton("LoadGame", 315, 480, 180, 70, (93, 150, 60),
                                     pygame.font.Font(ImagePaths.game_font, 20), "Load Game", 0,
                                     0, 0))
        self.objects.append(UiTextBox(273, 300, 250, 50, (205,205,205), pygame.font.Font(ImagePaths.game_font, 25), 0))

    def init_objects_on_screen(self):
        self.objects_on_screen = []
        for obj in self.objects:
            if obj.screen == self.window:
                self.objects_on_screen.append(obj)
        return self.objects_on_screen


    def main_loop(self):
        while True:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if clicked_obj and type(clicked_obj) == UiTextBox:
                        if event.key == pygame.K_BACKSPACE:
                            clicked_obj.inserted_text = clicked_obj.inserted_text[:-1]
                        elif event.key == pygame.K_RETURN:
                            clicked_obj.clicked = False
                        elif len(clicked_obj.inserted_text) < 20:
                            clicked_obj.inserted_text += event.unicode



                if event.type == pygame.MOUSEBUTTONUP:
                    clicked_obj = self.checkIntersection(pygame.mouse.get_pos())
                    for obj in self.objects_on_screen:
                        obj.clicked = False
                    if clicked_obj and type(clicked_obj) != UiButton:
                        clicked_obj.clicked = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_obj = self.checkIntersection(pygame.mouse.get_pos())
                    if clicked_obj:
                        clicked_obj.clicked = True
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()

    def draw(self):
        self.screen.fill((0, 0, 0))
        for obj in self.objects_on_screen:
            obj.draw(self.screen)


    def checkIntersection(self, mxy: tuple) -> UiButton | None:
        m_x, m_y = mxy
        for obj in self.objects_on_screen:
            if obj.x < m_x < obj.x + obj.width and m_y > obj.y and m_y < obj.y + obj.height:
                return obj
        return None