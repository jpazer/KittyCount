import pygame
import sys
from source.Utilities import Utilities
from source.UI import UI
from source.NumberLine import NumberLine
from source.Character import Character


class GameController:
    level = 50

    left_cat = "../assets/catLeft.png"
    right_cat = "../assets/catRight.png"

    ADD = pygame.USEREVENT + 1
    SUB = pygame.USEREVENT + 2
    GO = pygame.USEREVENT + 3
    RESTART = pygame.USEREVENT + 4
    QUIT = pygame.USEREVENT + 5
    def __init__(self, _screen):
        self.screen = _screen

        # setup variables
        self.w, self.h = Utilities.get_width_height()  # width and height of the screen
        self.screen = _screen

        # draw UI
        self.ui = UI(self.screen, self.w / 2, self.h / 2 + 150)

        # display Number Line
        self.number_line = NumberLine(self.screen, self.w, self.h)
        self.number_line.display()
        self.number_line.display_numbers()
        self.number_line.change_level(self.level)

        # display cat
        self.cat = Character(self.number_line.circle_pos, self.left_cat, 100, 100, self.screen)
        self.cat_position = self.cat.set_random_position(-1)
        self.cat.display()

        # display mouse
        self.mouse = Character(self.number_line.circle_pos, "../assets/mouse.png", 50, 50, self.screen, self.cat.get_x_pos())
        self.mouse_position = self.mouse.set_random_position(self.cat_position)
        self.mouse.display()

        self.ui.update_level(self.level)

        self.end = False
    def loop(self, events):
        # draw UI
        self.ui.display(events, self.end)

        for event in events:

            if event.type == self.GO or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
                Utilities.show_error(self.screen, "")  # clear previous error
                input_num = self.ui.user_input.get_input()

                if input_num is not None:

                    if input_num % self.level == 0:
                        new_position = int(input_num/self.level)

                        if self.cat_position + new_position >= 0:

                            if self.cat_position + new_position < self.number_line.num_of_points:
                                self.cat_position = self.cat.move(new_position)
                                self.ui.user_input.clear()

                                # debug print statements
                                print("New Position: " + str(new_position))
                                print("Cat Position: " + str(self.cat_position))
                                print("Mouse Position: " + str(self.mouse_position))

                                if self.cat_position == self.mouse_position:
                                    self.mouse_position = self.mouse.set_random_position(self.cat_position)
                                    self.cat.display()
                                    self.level += 1

                                    if self.level > 50:
                                        self.level = 1
                                        self.end = True
                                    else :
                                        self.ui.update_level(self.level)
                                        self.number_line.change_level(self.level)
                            else:
                                Utilities.show_error(self.screen, str(input_num) +
                                                     " moves the cat off of the number line. Try Again!")
                        else:
                            Utilities.show_error(self.screen, str(input_num) +
                                                 " moves the cat off of the number line. Try Again!")
                    else:
                        Utilities.show_error(self.screen, str(self.ui.user_input.get_input()) +
                                             " moves the cat to a number that is not on the number line.")
                else:
                    Utilities.show_error(self.screen, "Please type a number and try again!")

            if event.type == self.ADD:
                    self.ui.user_input.add(1)
            if event.type == self.SUB:
                    self.ui.user_input.add(-1)

            if event.type == self.RESTART:
                self.screen.fill((255,255,255))
                self.end = False
                self.cat.set_random_position(-1)
                self.mouse.set_random_position(self.cat_position)
                self.ui.update_level(self.level)
                self.number_line.change_level(self.level)
                self.number_line.display();
                

            if self.ui.user_input.get_input() is not None and self.ui.user_input.get_input() < 0:
                self.cat.set_display_image(self.left_cat)
                self.cat.erase()
                self.cat.display()
                self.mouse.erase()
                self.mouse.display()
            if self.ui.user_input.get_input() is not None and self.ui.user_input.get_input() > 0:
                self.cat.set_display_image(self.right_cat)
                self.cat.erase()
                self.cat.display()
                self.mouse.erase()
                self.mouse.display()





