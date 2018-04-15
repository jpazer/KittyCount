import pygame
from Utilities import Utilities


class Button:
    color = (255, 255, 255)

    def __init__(self, screen, position, size, text, text_size, action, user_input=False):
        self.screen = screen
        self.position = position  # x, y of button and text
        self.size = size  # w, h of button
        self.text = text  # string
        self.text_size = text_size  # pt size of text
        self.action = action  # this function can be called once the button is clicked (not implemented)
        self.user_input = user_input

        # make the text surface
        self.text_surface = Utilities.make_text_surface(self.text, self.text_size)

        # calculate the padding needed to center the text
        text_w, text_h = self.text_surface.get_size()
        button_w, button_h = self.size
        self.padding_x = (button_w - text_w)/2
        self.padding_y = (button_h - text_h)/2

    def check_hover(self):
        # check if the mouse is in the bounds of this button
        x, y = pygame.mouse.get_pos()
        if x > self.position[0]:
            if x < self.position[0] + self.size[0]:
                if y > self.position[1]:
                    if y < self.position[1] + self.size[1]:
                        return True
        return False

    def display(self, events):
        # if the button is clicked toggle the color
        if self.check_button_pressed(events):
            if self.user_input != False:
                self.action(self.screen, self.user_input)
            if self.color == (200, 200, 200):
                self.color = (255, 255, 255)
            else:
                self.color = (200, 200, 200)

        # background of button
        pygame.draw.rect(self.screen, self.color,
                         (self.position[0] - self.padding_x,
                          self.position[1] - self.padding_y,
                          self.size[0], self.size[1]), 0)

        # border of button
        pygame.draw.rect(self.screen, (0, 0, 0),
                         (self.position[0] - self.padding_x,
                          self.position[1] - self.padding_y,
                          self.size[0], self.size[1]), 1)

        # draw button text to screen
        self.screen.blit(self.text_surface, self.position)

    def check_button_pressed(self, events):
        for event in events:
            # handle mouse click
            if event.type == pygame.MOUSEBUTTONUP:
                return self.check_hover()
        return False
