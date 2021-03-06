import pygame
from source.Utilities import Utilities
from libraries.pygame_textinput.pygame_textinput import TextInput


class UserInput:
    input = ""
    font_size = 80
    padding_x = 30
    padding_y = 20

    def __init__(self, screen, position, width, height):
        self.screen = screen
        self.text_input = TextInput(font_size=self.font_size, max_chars=4)
        self.position = position
        self.height = height
        self.width = width
        # set starting value
        self.clear()

    def display(self, events):
        # background of text box (refreshes)
        pygame.draw.rect(self.screen, (255, 255, 255),
                         (self.position[0],
                          self.position[1],
                          self.width, self.height), 0)
        # border of text box
        pygame.draw.rect(self.screen, (0, 0, 0),
                         (self.position[0],
                          self.position[1],
                          self.width, self.height), 1)

        # Feed it with events every frame
        self.text_input.update(events)

        # Blit its surface onto the screen
        self.screen.blit(self.text_input.get_surface(), (self.position[0] + self.padding_x, self.position[1] + self.padding_y))

    def validate_input(self, string):
        try:
            int(string)
            return True
        except ValueError:
            return False

    def get_input(self):
        # not yet implemented to test
        string = str(self.text_input.get_text())
        if self.validate_input(string):
            return int(string)

    def add(self, num):
        if self.get_input() is None:
            self.text_input.input_string = str(num)
            self.text_input.cursor_position = len(str(num))
        else:
            self.text_input.input_string = str(int(self.text_input.input_string) + num)
            self.text_input.cursor_position = len(self.text_input.input_string)

    def clear(self):
        self.text_input.input_string = ""
        self.text_input.cursor_position = 0
