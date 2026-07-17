import os
import pygame

class Animation:
    def __init__(self, image_folder, target_width):
        self.target_width = target_width

        self.frames = []
        self.counter = 0

        self.current_frame = None

        for filename in sorted(os.listdir(image_folder)):
            img = pygame.image.load(os.path.join(image_folder, filename)).convert_alpha()

            ratio = img.get_height() / img.get_width()

            new_h = int(self.target_width * ratio)
            scaled_img = pygame.transform.scale(img, (self.target_width, new_h))
            self.frames.append(scaled_img)

        if self.frames:
            max_w = max(f.get_width() for f in self.frames)
            max_h = max(f.get_height() for f in self.frames)

            uniform_frames = []
            for f in self.frames:
                canvas = pygame.Surface((max_w, max_h), pygame.SRCALPHA)
                canvas.fill((0, 0, 0, 0))

                x = (max_w - f.get_width()) // 2
                y = max_h - f.get_height()

                canvas.blit(f, (x, y))
                uniform_frames.append(canvas)
            self.frames = uniform_frames
            self.rect_size = (max_w, max_h)
        else:
            self.rect_size = (0, 0)

    def is_last_frame(self):
        if self.counter >= len(self.frames)-1:
            return True
        else:
            return False

    def change_frame_to_next(self):
        if self.counter >= len(self.frames)-1:
            self.counter = 0
        else:
            self.counter += 1

    def reset_animation(self):
        self.counter = 0

    def get_frame(self):
        self.current_frame = self.frames[self.counter]
        return self.current_frame