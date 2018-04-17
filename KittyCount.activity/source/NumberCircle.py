import pygame
from source.Utilities import Utilities


class NumberCircle:
    color = (0, 0, 0)
    radius = 10
    width = 0

    def __init__(self, screen, position, number, level):
        self.screen = screen
        self.position = position
        self.number = number
        self.level = level

    def display(self):
        # draw circle
        pygame.draw.circle(self.screen, self.color, self.position, self.radius, self.width)
        # draw number beneath circle
        self.screen.blit(Utilities.make_text_surface(self.number * self.level, 12),
                         (self.position[0] - 5, self.position[1] + 15))
