import pygame
from source.Button import Button
from source.Utilities import Utilities


class StartScreen:

    def __init__(self, screen, x, y):
        # make UI
        self.x = x
        self.y = y
        self.w, self.h = Utilities.get_width_height()
        self.screen = screen

        self.button_start = Button(screen, (x-150, y), (300, 100), "Start", 60, 6)
        self.cat = pygame.image.load("../assets/cat1.png")
        self.mouse = pygame.image.load("../assets/mouse3.png")

    def display(self, events):
        # draw UI
        self.display_text("Kitty Count", self.x, self.y - 150, 70)
        self.display_text("Click to start!", self.x, self.y+110, 20)
        self.button_start.display(events)
        self.screen.blit(pygame.transform.scale(self.mouse, (70, 70)), (self.x - 300, self.y+30))
        self.screen.blit(pygame.transform.scale(self.cat, (170, 170)), (self.x + 200, self.y-70))

    def display_text(self, text, x, y, size):
        text_surface = Utilities.make_text_surface(text, size)
        text_w, text_h = text_surface.get_size()
        self.screen.blit(text_surface, (x - text_w/2, y))
