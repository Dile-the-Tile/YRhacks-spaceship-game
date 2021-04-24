import pygame


class Enemy(object):
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.x_change = 20
        self.y_change = 70
        self.image = image

    def draw_enemy(self, x_pos, y_pos, screen):
        screen.blit(self.image, (x_pos, y_pos))

    def move(self):
        self.x += self.x_change
        if self.x >= 1400 - 64:
            self.x_change = -7
            if self.y < 1400 - 64:
                self.y += self.y_change
            else:
                self.y = 1400 - 64
        elif self.x <= 0:
            self.x_change = 7
            if self.y < 1400 - 64:
                self.y += self.y_change
            else:
                self.y = 1400 - 64

