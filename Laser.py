import pygame

class Laser(object):
    laser_img = pygame.image.load("bullet2.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.y_change = 45



