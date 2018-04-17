import pygame
from source.Utilities import Utilities
from libraries.pygame_textinput.pygame_textinput import TextInput


class UserInput:
    input = ""
    width = 200
    height = 90
    font_size = 80
    padding_x = 50
    padding_y = 20
    max_characters = 3

    def __init__(self, screen, position):
        self.screen = screen
        self.text_input = TextInput(font_size=self.font_size)
        self.position = position
        # set starting value
        self.clear()

    def display(self, events):
        # background of text box (refreshes)
        pygame.draw.rect(self.screen, (255, 255, 255),
                         (self.position[0]-self.padding_x,
                          self.position[1]-self.padding_y,
                          self.width, self.height), 0)
        # border of text box
        pygame.draw.rect(self.screen, (0, 0, 0),
                         (self.position[0] - self.padding_x,
                          self.position[1] - self.padding_y,
                          self.width, self.height), 1)

        # Feed it with events every frame
        self.text_input.update(events)

        # Blit its surface onto the screen
        self.screen.blit(self.text_input.get_surface(), self.position)



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
        else:
            Utilities.show_error(self.screen, "The input must be a number")

    def add(self, num):
        self.text_input.input_string = str(int(self.text_input.input_string) + num)
        self.text_input.cursor_position = len(self.text_input.input_string)

    def clear(self):
        self.text_input.input_string = "0"
        self.text_input.cursor_position = 1
