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
        self.cat_position = self.cat.set_random_position(-1)
        self.cat.display()

        # display mouse
        self.mouse = Character(self.number_line.circle_pos, "../Assets/mouse3.png", 50, 50, self.screen, self.cat.get_x_pos())
        self.mouse_position = self.mouse.set_random_position(self.cat_position)
        self.mouse.display()

    def loop(self, events):
        # draw UI
        self.ui.display(events)

        for event in events:
            if event.type == pygame.USEREVENT:
                if event.button_type == "go":
                    self.cat_position = self.cat.move(self.ui.user_input.get_input())
                    self.ui.user_input.clear()
                    if self.cat_position == self.mouse_position:
                        self.mouse_position = self.mouse.set_random_position(self.cat_position)
                        self.cat.display()
                        print("you caught the mouse!")

