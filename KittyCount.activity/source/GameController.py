import pygame
from source.Utilities import Utilities
from source.UI import UI
from source.NumberLine import NumberLine
from source.Character import Character


class GameController:

    def __init__(self, _screen):
        self.screen = _screen

        # setup variables
        self.w, self.h = Utilities.get_width_height()  # width and height of the screen
        self.screen = _screen

        # draw UI
        self.ui = UI(self.screen, self.w / 2 - 200, self.h / 2 + 150)

        # display Number Line
        self.number_line = NumberLine(self.screen, self.w, self.h)
        self.number_line.display()

        # display cat
        self.cat = Character(self.number_line.circle_pos, "../Assets/cat1.png", 100, 100, self.screen)
        self.cat.display()

        # display mouse
        self.mouse = Character(self.number_line.circle_pos, "../Assets/mouse3.png", 50, 50, self.screen, self.cat.get_x_pos())
        self.mouse.display()

    def loop(self, events):
        # draw UI
        self.ui.display(events)
