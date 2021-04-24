import pygame


class Player(object):
    play_image = pygame.image.load("spaceship.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_change = 0
        self.state = "normal"

    def draw_player(self, x_pos, y_pos, screen):
        screen.blit(self.play_image, (x_pos, y_pos))
