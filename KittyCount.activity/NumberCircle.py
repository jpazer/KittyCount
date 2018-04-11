import pygame
from Utilities import Utilities


class NumberCircle:
    screen = 0  # screen object to draw to
    number = 0  # number this circle represents
    level = 1

    position = (0, 0)
    color = (0, 0, 0)
    radius = 10
    width = 0

    def __init__(self, position, number, screen):
        self.position = position
        self.number = number
        self.screen = screen

    def display(self):
        # draw circle
        pygame.draw.circle(self.screen, self.color, self.position, self.radius, self.width)
        # draw number beneath circle
        self.screen.blit(Utilities.make_text_surface(self.number * self.level, 12),
                         (self.position[0] - 5, self.position[1] + 15))
