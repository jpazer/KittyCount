import pygame
from source.Button import Button
from source.Utilities import Utilities


class EndScreen:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        self.restart = Button(screen, (self.x - 150, self.y), (300, 100), "Restart", 50, 4)
        self.quit = Button(screen, (self.x - 150, self.y + 130), (300, 100), "Quit", 50, 5)

        self.cat = pygame.image.load("../assets/cat1.png")
        self.mouse = pygame.image.load("../assets/mouse3.png")

    def display(self, events):
        self.screen.fill((255, 255, 255))

        self.restart.display(events)
        self.quit.display(events)
        self.display_text("Congratulations! You Won!", self.x, self.y-150, 60)

        self.screen.blit(pygame.transform.scale(self.mouse, (70, 70)), (self.x - 300, self.y + 80))
        self.screen.blit(pygame.transform.scale(self.cat, (170, 170)), (self.x + 200, self.y + 20))

    def display_text(self, text, x, y, size):
        text_surface = Utilities.make_text_surface(text, size)
        text_w, text_h = text_surface.get_size()
        self.screen.blit(text_surface, (x - text_w/2, y))



