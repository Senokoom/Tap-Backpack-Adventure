import os
import pygame

class Animation:
    def __init__(self, image_folder, target_width, animation_speed):
        self.target_width = target_width
        self.animation_speed = animation_speed

        self.frames = []
        self.counter = 0

        self.current_frame = None

        for filename in sorted(os.listdir(image_folder)):
            img = pygame.image.load(os.path.join(image_folder, filename)).convert_alpha()

            ratio = img.get_height() / img.get_width()

            new_h = int(self.target_width * ratio)
            scaled_img = pygame.transform.smoothscale(img, (self.target_width, new_h))
            self.frames.append(scaled_img)

        if self.frames:
            max_w = max(f.get_width() for f in self.frames)
            max_h = max(f.get_height() for f in self.frames)

            uniform_frames = []
            for f in self.frames:
                canvas = pygame.Surface((max_w, max_h), pygame.SRCALPHA)
                canvas.fill((0, 0, 0, 0))

                x = (max_w - f.get_width()) // 2
                y = (max_h - f.get_height()) // 2
                canvas.blit(f, (x, y))
                uniform_frames.append(canvas)
            self.frames = uniform_frames
            self.rect_size = (max_w, max_h)
        else:
            self.rect_size = (0, 0)

    def update(self):
        pass

    def get_frame(self):
        pass