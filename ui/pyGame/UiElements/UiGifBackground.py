from ui.pyGame.UiElements.UiElement import UiElement
import pygame
import gif_pygame

class UiGifBackground(UiElement):
    def __init__(self, x,y, gif, size, screen):
        self.x = x
        self.y = y
        self.size = size
        self.screen = screen

        self.clickable = False

        scaled_frames_list = []
        for frame, duration in gif.frames:
            smooth_frame = pygame.transform.smoothscale(frame, size)
            scaled_frames_list.append([smooth_frame, duration])

        self.smooth_gif = gif_pygame.GIFPygame(scaled_frames_list)

    def draw(self, window):
        self.smooth_gif.render(window, (self.x, self.y))