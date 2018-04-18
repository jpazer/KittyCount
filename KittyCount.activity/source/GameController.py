import pygame
from source.Utilities import Utilities
from source.UI import UI
from source.NumberLine import NumberLine
from source.Character import Character


class GameController:
    level = 1

    left_cat = "../assets/catLeft.png"
    right_cat = "../assets/catRight.png"

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
        self.cat = Character(self.number_line.circle_pos, self.left_cat, 100, 100, self.screen)
        self.cat_position = self.cat.set_random_position(-1)
        self.cat.display()

        # display mouse
        self.mouse = Character(self.number_line.circle_pos, "../assets/mouse.png", 50, 50, self.screen, self.cat.get_x_pos())
        self.mouse_position = self.mouse.set_random_position(self.cat_position)
        self.mouse.display()

        self.ui.update_level(self.level)

    def loop(self, events):
        # draw UI
        self.ui.display(events)

        for event in events:
            if event.type == pygame.USEREVENT:
                if event.button_type == "go":
                    self.cat_position = self.cat.move(int(self.ui.user_input.get_input()/self.level))
                    self.ui.user_input.clear()
                    if self.cat_position == self.mouse_position:
                        self.mouse_position = self.mouse.set_random_position(self.cat_position)
                        self.cat.display()
                        self.level += 1
                        self.ui.update_level(self.level)
                        self.number_line.next_level()
                        print("you caught the mouse!")
                if event.button_type == "add":
                    self.ui.user_input.add(1)
                if event.button_type == "sub":
                    self.ui.user_input.add(-1)

                if self.ui.user_input.get_input() < 0:
                    self.cat.set_display_image(self.left_cat)
                    self.cat.erase()
                    self.cat.display()
                    self.mouse.erase()
                    self.mouse.display()
                if self.ui.user_input.get_input() > 0:
                    self.cat.set_display_image(self.right_cat)
                    self.cat.erase()
                    self.cat.display()
                    self.mouse.erase()
                    self.mouse.display()







