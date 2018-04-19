import pygame
from source.Utilities import Utilities


class NumberCircle:
    color = (0, 0, 0)
    radius = 10
    width = 0

    def __init__(self, screen, position):
        self.screen = screen
        self.position = position

    def display(self):
        # draw circle
        pygame.draw.circle(self.screen, self.color, self.position, self.radius, self.width)
