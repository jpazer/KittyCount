import pygame
from source.Utilities import Utilities
from source.UI import UI
from source.StartScreen import StartScreen
from source.EndScreen import EndScreen
from source.NumberLine import NumberLine
from source.Character import Character


class GameController:

    level = 1
    game_state = "start"
    
    # Error messages constants
    CAT_TOO_FAR_MESSAGE = " moves the cat off of the number line. Try Again!"
    EMPTY_BOX_MESSAGE = "Please type a number and try again."
    NOT_ON_THE_NUMBER_LINE_MESSAGE = " is not on this number line. Try Again."
    
    # max level for the game.
    MAX_LEVEL = 50

    # constants for cat and mouse pictures.
    LEFT_CAT = "../assets/catLeft.png"
    RIGHT_CAT = "../assets/catRight.png"
    MOUSE = "../assets/mouse.png"

    ADD = pygame.USEREVENT + 1
    SUB = pygame.USEREVENT + 2
    GO = pygame.USEREVENT + 3
    RESTART = pygame.USEREVENT + 4
    QUIT = pygame.USEREVENT + 5
    START = pygame.USEREVENT + 6

    def game_display(self):
        self.screen.fill((255, 255, 255))

        # draw number line
        self.number_line.display()
        self.number_line.display_numbers()
        self.number_line.change_level(self.level)

        # position and draw cat
        self.cat_position = self.cat.set_random_position(-1)
        self.cat.display()

        # position and draw mouse
        self.mouse_position = self.mouse.set_random_position(self.cat_position)
        self.mouse.display()

        # draw level on screen
        self.ui.display_all_help_text()
        self.ui.update_level(self.level)

    def __init__(self, _screen):
        self.screen = _screen

        # setup variables
        self.w, self.h = Utilities.get_width_height()  # width and height of the screen
        self.screen = _screen

        # make start screen
        self.start_screen = StartScreen(self.screen, self.w / 2, self.h / 2)

        # make end screen
        self.end_screen = EndScreen(self.screen, self.w / 2, self.h / 2)

        # make UI
        self.ui = UI(self.screen, self.w / 2, self.h/2 + 50)

        # make Number Line
        self.number_line = NumberLine(self.screen, self.w, self.h)

        # make cat
        self.cat = Character(self.number_line.circle_pos, self.LEFT_CAT, 100, 100, self.screen)
        self.cat_position = -1

        # make mouse
        self.mouse = Character(self.number_line.circle_pos, self.MOUSE, 50, 50, self.screen, self.cat.get_x_pos())
        self.mouse_position = -1

        self.end = False

    def loop(self, events):
        # draw UI
        if self.game_state == "start":
            self.start_screen.display(events)
        if self.game_state == "play":
            self.ui.display(events)
        if self.game_state == "end":
            self.end_screen.display(events)

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

                                if self.cat_position == self.mouse_position:
                                    self.mouse_position = self.mouse.set_random_position(self.cat_position)
                                    self.cat.display()
                                    self.level += 1

                                    if self.level > self.MAX_LEVEL:
                                        self.game_state = "end"
                                    else:
                                        self.ui.update_level(self.level)
                                        self.number_line.change_level(self.level)
                            else:
                                Utilities.show_error(self.screen, str(input_num) + self.CAT_TOO_FAR_MESSAGE)
                        else:
                            Utilities.show_error(self.screen, str(input_num) + self.CAT_TOO_FAR_MESSAGE)
                    else:
                        equation = ""
                        if self.ui.user_input.get_input() > 0:
                            equation = str(self.cat_position * self.level) + " + " + str(self.ui.user_input.get_input())
                        else:
                            equation = str(self.cat_position * self.level) + " - " + str(self.ui.user_input.get_input())[1:]
                        Utilities.show_error(self.screen, equation + self.NOT_ON_THE_NUMBER_LINE_MESSAGE)
                else:
                    Utilities.show_error(self.screen, self.EMPTY_BOX_MESSAGE)

            if event.type == self.ADD:
                self.ui.user_input.add(1)
            if event.type == self.SUB:
                self.ui.user_input.add(-1)

            if event.type == self.START:
                self.game_state = "play"
                self.game_display()

            if event.type == self.RESTART:
                self.level = 1
                self.game_state = "play"
                self.game_display()

            if event.type == self.QUIT:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

            if self.ui.user_input.get_input() is not None and self.ui.user_input.get_input() < 0:
                self.cat.set_display_image(self.LEFT_CAT)
                self.cat.erase()
                self.cat.display()
                self.mouse.erase()
                self.mouse.display()
            if self.ui.user_input.get_input() is not None and self.ui.user_input.get_input() > 0:
                self.cat.set_display_image(self.RIGHT_CAT)
                self.cat.erase()
                self.cat.display()
                self.mouse.erase()
                self.mouse.display()
